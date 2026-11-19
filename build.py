#!/usr/bin/env python3
"""Builds the three Cabins in the Ozarks sites into dist/.

  dist/hub/                 -> cabinsintheozarks.com
  dist/little-switzerland/  -> littleswitzerlandarkansas.com
  dist/morwood-house/       -> morwoodhouse.com

All content lives in data.py. Edit there, run `python3 build.py`, redeploy.
"""
import json, shutil
from pathlib import Path
from html import escape as e
from data import *

ROOT = Path(__file__).parent
SRC, DIST = ROOT / "src", ROOT / "dist"

def P(pid):
    return f"https://uc.orez.io/f/{pid}"

FONTS = {
    "ls": "family=Archivo:wdth,wght@62..125,500..900&family=Source+Serif+4:ital,opsz,wght@0,8..60,400;0,8..60,600;1,8..60,400",
    "mw": "family=Gloock&family=Instrument+Sans:wght@400..700",
    "hub": "family=Archivo:wdth,wght@62..125,700..900&family=Gloock&family=Instrument+Sans:wght@400..700",
}

CROSS = '<svg class="cross" viewBox="0 0 32 32" aria-hidden="true"><rect width="32" height="32" fill="#d52b1e"/><path d="M13 6h6v7h7v6h-7v7h-6v-7H6v-6h7z" fill="#fff"/></svg>'
CROSS_WHITE = '<svg class="cross" viewBox="0 0 32 32" aria-hidden="true"><path d="M12 2h8v10h10v8H20v10h-8V20H2v-8h10z" fill="#fff"/></svg>'


def page(site, *, title, desc, canonical, body, schema, depth=0, og_image=None, theme_color="#000"):
    up = "../" * depth
    ld = "\n".join(f'<script type="application/ld+json">{json.dumps(s, ensure_ascii=False)}</script>' for s in schema)
    og = f'<meta property="og:image" content="{og_image}">' if og_image else ""
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<link rel="canonical" href="{canonical}">
<meta name="theme-color" content="{theme_color}">
<meta property="og:type" content="website">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:url" content="{canonical}">
{og}
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="preconnect" href="https://uc.orez.io">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?{FONTS[site]}&display=swap">
<link rel="stylesheet" href="{up}assets/base.css">
<link rel="stylesheet" href="{up}assets/theme.css">
{ld}
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
{body}
<div class="lightbox" role="dialog" aria-modal="true" aria-label="Photo viewer">
  <button class="lb-close" aria-label="Close photos">&times;</button>
  <button class="lb-prev" aria-label="Previous photo">&#8249;</button>
  <img alt="">
  <button class="lb-next" aria-label="Next photo">&#8250;</button>
  <span class="lb-count"></span>
</div>
<script src="{up}assets/site.js" defer></script>
</body>
</html>
"""


def gallery(photos, alt_base):
    items = "".join(
        f'<button type="button" data-full="{P(p)}"><img src="{P(p)}" alt="{e(alt_base)}, photo {i+1}" loading="lazy" decoding="async"></button>'
        for i, p in enumerate(photos))
    return f'<div class="gallery">{items}</div>'


def orez_slot(kind, prop_ids, title, note, fallback_url, fallback_label):
    """Placeholder that the OwnerRez widget snippet replaces.
    Paste the widget code from OwnerRez > Settings > Widgets inside this div and add data-live."""
    return f"""<!-- OWNERREZ WIDGET SLOT: type={kind} properties={','.join(prop_ids)} -->
<div class="orez-slot" data-orez-widget="{kind}" data-orez-properties="{','.join(prop_ids)}">
  <p class="slot-title">{e(title)}</p>
  <p class="slot-note">{e(note)}</p>
  <a class="btn btn-primary" href="{fallback_url}">{e(fallback_label)}</a>
</div>"""


def faq_html(items):
    return '<div class="faq">' + "".join(
        f"<details><summary>{e(q)}</summary><div><p>{a}</p></div></details>" for q, a in items) + "</div>"


def faq_schema(items):
    import re
    return {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": re.sub(r"<[^>]+>", "", a)}}
        for q, a in items]}


def footer(brand_html, site_name, links, extra=""):
    lis = "".join(f'<li><a href="{u}">{e(t)}</a></li>' for t, u in links)
    return f"""<footer class="site-footer">
  <div class="wrap">
    <div class="cols">
      <div>
        <p class="brand" style="margin-bottom:1rem">{brand_html}</p>
        <p>{e(ADDRESS_LINES[site_name])}</p>
      </div>
      <div>
        <h3>Talk to Matt</h3>
        <ul>
          <li><a href="tel:{PHONE_TEL}">{PHONE}</a></li>
          <li><a href="sms:{PHONE_TEL}">Text us</a></li>
          <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
        </ul>
      </div>
      <div>
        <h3>Our places</h3>
        <ul>{lis}</ul>
      </div>
    </div>
    {extra}
    <p class="fine">&copy; 2026 Cabins in the Ozarks, Jasper, Arkansas.</p>
  </div>
</footer>"""


def review_figs(reviews, cls="review"):
    out = []
    for r in reviews:
        tag = f'<span class="tag" style="--c:{r["color"]}">{e(r["place"])}</span>' if r.get("color") else ""
        out.append(f'<figure class="{cls}">{tag}<blockquote><p>{e(r["text"])}</p></blockquote><figcaption>{e(r["who"])}</figcaption></figure>')
    return "".join(out)


def area_list(items):
    return '<ul class="area-list">' + "".join(f"<li><b>{e(n)}</b>{e(d)}</li>" for n, d in items) + "</ul>"


def lodging_schema(name, url, desc, geo, address, image, extra=None):
    s = {"@context": "https://schema.org", "@type": "LodgingBusiness", "name": name, "url": url, "description": desc,
         "telephone": PHONE_TEL, "email": EMAIL, "image": image,
         "address": {"@type": "PostalAddress", **address},
         "geo": {"@type": "GeoCoordinates", "latitude": geo[0], "longitude": geo[1]},
         "checkinTime": "16:00", "checkoutTime": "11:00",
         "parentOrganization": {"@type": "Organization", "name": "Cabins in the Ozarks", "url": HUB_URL}}
    if extra:
        s.update(extra)
    return s


# ---------------------------------------------------------------------------
# LITTLE SWITZERLAND
# ---------------------------------------------------------------------------
def ls_header(depth=0):
    up = "../" * depth
    return f"""<header class="site-header">
  <div class="wrap">
    <a class="brand" href="{up}">{CROSS}<span>Little Switzerland</span></a>
    <button class="nav-toggle" aria-expanded="false" aria-controls="nav">Menu</button>
    <nav class="nav" id="nav" aria-label="Main">
      <a href="{up}#cabins">Cabins</a>
      <a href="{up}#grounds">Grounds</a>
      <a href="{up}#history">Since 1891</a>
      <a href="{up}#area">Nearby</a>
      <a href="{up}#faq">FAQ</a>
      <a class="btn btn-primary" href="{up}#dates">Check dates</a>
    </nav>
  </div>
</header>"""


def ls_footer():
    return footer(CROSS + "<span>Little Switzerland</span>", "ls",
                  [("Cabins in the Ozarks", HUB_URL), ("Morwood House", MW_URL)] +
                  [(u["name"], f'{LS_URL}/{u["slug"]}/') for u in LS_UNITS])


def build_ls():
    out = DIST / "little-switzerland"
    rows = []
    for u in LS_UNITS:
        group = '<p class="group">Cabin 3, the three room mini motel</p>' if u["slug"].startswith("room") else ""
        meta = "".join(f"<li>{e(m)}</li>" for m in u["meta"])
        rows.append(f"""<article class="unit-row">
  <div class="unit-num" aria-hidden="true">{u['num']}</div>
  <a class="pic" href="{u['slug']}/"><img src="{P(u['hero'])}" alt="{e(u['name'])} at Little Switzerland" loading="lazy" decoding="async"></a>
  <div class="info">
    {group}
    <h3>{e(u['name'])}</h3>
    <p class="sub">{e(u['tagline'])}</p>
    <ul class="meta">{meta}</ul>
    <p class="rate">From ${u['rate']} <small>a night</small></p>
    <div class="actions"><a class="btn btn-primary" href="{u['slug']}/">See {e(u['name'])}</a><a class="btn btn-ghost" href="{u['slug']}/#book">Check dates</a></div>
  </div>
</article>""")

    g = LS_GROUNDS
    body = f"""{ls_header()}
<main id="main">
<section class="ls-hero" aria-label="Welcome">
  <div class="field">
    {CROSS_WHITE}
    <h1><span>Little</span><span>Switzerland</span></h1>
    <p class="lede">Five cabins and suites 2&frac12; miles north of Jasper on Scenic Byway 7. Travelers have been stopping here since 1891.</p>
    <div class="actions">
      <a class="btn btn-white" href="#cabins">See the cabins</a>
      <a class="btn btn-line" href="#dates">Check dates</a>
    </div>
  </div>
  <figure class="photo" style="margin:0"><img src="{P(LS_HERO)}" alt="Cabin 1 at Little Switzerland among the oaks" fetchpriority="high"><figcaption>Cabin 1, from the drive</figcaption></figure>
</section>

<dl class="facts">
  <div><dt>5</dt><dd>cabins and suites</dd></div>
  <div><dt>2 to 4</dt><dd>guests each, 14 in all</dd></div>
  <div><dt>$85</dt><dd>a night, lowest rate</dd></div>
  <div><dt>4.7</dt><dd>on Airbnb, about 600 reviews</dd></div>
</dl>

<section class="section" id="cabins">
  <div class="wrap">
    <div class="sec-head"><h2>The cabins</h2><p>Every unit has its own bath, a queen or king bed, Wifi, a mini fridge, microwave and coffee maker. None has a full kitchen, so plan on the grills out back or dinner in Jasper, five minutes down the hill.</p></div>
    <div class="units">{''.join(rows)}</div>
    <p class="note-cabin3">Traveling with another couple? Rooms 3 and 4 share an interior door, so you can book both and open them into one suite.</p>
  </div>
</section>

<section class="section grounds" id="grounds">
  <div class="wrap">
    <div class="copy">
      <h2>Out back</h2>
      <ul>
        <li>The Hollow, a red roofed pavilion with picnic tables and grills</li>
        <li>A fire pit for evenings, with firewood on hand</li>
        <li>A porch swing under the old oaks</li>
        <li>Porches and balconies on every cabin</li>
        <li>Free parking on site</li>
      </ul>
    </div>
    <div class="grid">
      <figure class="g1"><img src="{P(g[0])}" alt="The Hollow, the covered picnic pavilion out back" loading="lazy"></figure>
      <figure class="g2"><img src="{P(g[1])}" alt="Picnic tables and grills under the pavilion" loading="lazy"></figure>
      <figure class="g3"><img src="{P(g[2])}" alt="The porch swing in the yard" loading="lazy"></figure>
    </div>
  </div>
</section>

<section class="section history" id="history">
  <div class="wrap">
    <div class="sec-head"><h2>Since 1891</h2><p>Two Swiss families settled this bend in the road. The trip from Jasper to Harrison took three days by wagon, and Little Switzerland was the first stop before the mountains.</p></div>
    <ol class="timeline">
      <li><span class="yr">1891</span><p>Swiss settlers build the homestead. Travelers rest here and fill their water barrels before the climb north.</p></li>
      <li><span class="yr">1930s</span><p>The first rental cabins open for tourists. No electricity and no plumbing, just the outhouse and the view.</p></li>
      <li><span class="yr">1960s</span><p>Word spreads. Couples honeymoon here and kids spend their first mountain vacations here. Some still stop by to say hi.</p></li>
      <li><span class="yr">Today</span><p>New owners are renovating cabin by cabin. Cabin 2 reopened in December 2025 with a king bed, granite and all new furniture.</p></li>
    </ol>
  </div>
</section>

<section class="section" id="dates">
  <div class="wrap">
    <div class="sec-head"><h2>Open dates</h2><p>All five units on one calendar. Find a gap that fits and book it here direct, without the app fees.</p></div>
    {orez_slot("ribbon-calendar", [u['orez'] for u in LS_UNITS], "Live calendar for all five units", "Synced with Airbnb and VRBO, so what you see is what's open.", LS_HOSTED + "/availability", "See open dates")}
  </div>
</section>

<section class="section" id="reviews" style="padding-top:0">
  <div class="wrap">
    <div class="sec-head"><h2>Guests say</h2><p>The same things come up again and again: location, clean rooms, and hosts who answer fast.</p></div>
    <div class="scores">
      <div><b>4.77</b><span>Room 5 on Airbnb, 173 reviews</span></div>
      <div><b>4.69</b><span>Cabin 1 on Airbnb, 223 reviews</span></div>
      <div><b>4.9</b><span>check in and communication scores</span></div>
    </div>
    <div class="review-grid">{review_figs(LS_REVIEWS)}</div>
    {orez_slot("reviews", [u['orez'] for u in LS_UNITS], "More reviews", "Recent reviews from every channel load here.", LS_HOSTED + "/reviews", "Read all reviews")}
  </div>
</section>

<section class="crosssell" aria-label="Morwood House">
  <div class="wrap">
    <div><h2>Bringing more than four?</h2><p>Morwood House sleeps 8 on 15 private acres with a hot tub and a game room, 3&frac12; miles down Highway 7. Book it with a few of our cabins and fit up to 22.</p></div>
    <a class="btn btn-primary" href="{MW_URL}">See Morwood House</a>
  </div>
</section>

<section class="section" id="area">
  <div class="wrap">
    <div class="sec-head"><h2>Nearby</h2><p>You're in the middle of the Buffalo River country. Here's where guests spend their days.</p></div>
    {area_list(AREA)}
  </div>
</section>

<section class="section" id="faq" style="background:var(--mist)">
  <div class="wrap">
    <div class="sec-head"><h2>Good to know</h2><p>Still wondering about something? Call or text Matt at <a href="tel:{PHONE_TEL}">{PHONE}</a>.</p></div>
    {faq_html(LS_FAQ)}
  </div>
</section>
</main>
<div class="book-bar"><span class="price">From $85 a night<small>5 cabins, sleeps 2 to 4</small></span><a class="btn btn-white" style="background:#fff;color:var(--red)" href="#dates">Check dates</a></div>
{ls_footer()}"""

    schema = [lodging_schema("Little Switzerland Cabins", LS_URL + "/", LS_DESC, LS_GEO, LS_ADDRESS, P(LS_HERO), {
        "priceRange": "$85 to $110 per night", "petsAllowed": True,
        "amenityFeature": [{"@type": "LocationFeatureSpecification", "name": n, "value": True} for n in LS_AMENITIES],
        "containsPlace": [{"@type": "Accommodation", "name": u["name"], "url": f'{LS_URL}/{u["slug"]}/'} for u in LS_UNITS],
        "foundingDate": "1891"}), faq_schema(LS_FAQ)]
    (out).mkdir(parents=True, exist_ok=True)
    (out / "index.html").write_text(page("ls", title="Little Switzerland Cabins | Historic cabins near Jasper, Arkansas",
        desc=LS_DESC, canonical=LS_URL + "/", body=body, schema=schema, og_image=P(LS_HERO), theme_color="#d52b1e"))

    for u in LS_UNITS:
        others = "".join(
            f'<a href="../{o["slug"]}/"><span class="n">{o["num"]}</span><img src="{P(o["hero"])}" alt="" loading="lazy"><b>{e(o["name"])}</b><br><span>From ${o["rate"]}</span></a>'
            for o in LS_UNITS if o is not u)
        details = "".join(f'<section><h3>{e(h)}</h3><ul>{"".join(f"<li>{e(x)}</li>" for x in items)}</ul></section>' for h, items in u["details"])
        ubody = f"""{ls_header(1)}
<main id="main">
<section class="unit-hero">
  <div class="field">
    <span class="big" aria-hidden="true">{u['num']}</span>
    <h1>{e(u['name'])}</h1>
    <p class="sub">{e(u['tagline'])}</p>
    <p class="sub">{e(' / '.join(u['meta']))}</p>
    <p class="rate">From ${u['rate']} a night</p>
  </div>
  <figure class="photo" style="margin:0"><img src="{P(u['hero'])}" alt="{e(u['name'])}" fetchpriority="high"></figure>
</section>
<div class="wrap crumbs"><a href="../">Little Switzerland</a> / {e(u['name'])}</div>
<section class="section" style="padding-top:1rem">
  <div class="wrap">
    <div class="sec-head"><h2>Inside</h2><p>{e(u['desc'])}</p></div>
    {gallery(u['photos'], u['name'])}
  </div>
</section>
<section class="section" style="padding-top:0">
  <div class="wrap"><div class="details">{details}</div></div>
</section>
<section class="section" id="book" style="background:var(--mist)">
  <div class="wrap book-split">
    <div>
      <h2 style="font-size:clamp(2.6rem,6vw,5rem);font-weight:900;margin-bottom:1.5rem">Book {e(u['name'])}</h2>
      {orez_slot("booking", [u['orez']], f"Pick your dates for {u['name']}", "Live availability and pricing. Book direct and skip the Airbnb service fee.", LS_HOSTED + "/" + u['hosted'] + "#availability", "See open dates and book")}
    </div>
    <div class="details" style="grid-template-columns:1fr">
      <section><h3>Check in and out</h3><ul><li>Check in after 4 PM</li><li>Check out by 11 AM</li><li>Self check in</li></ul></section>
      <section><h3>Pets</h3><ul><li>Dogs welcome, $25 per pet per stay</li></ul></section>
      <section><h3>Questions</h3><ul><li><a href="tel:{PHONE_TEL}">Call {PHONE}</a></li><li><a href="sms:{PHONE_TEL}">Text Matt</a></li></ul></section>
    </div>
  </div>
</section>
<section class="section">
  <div class="wrap">
    <div class="sec-head"><h2>The other cabins</h2><p>Coming with family or friends? Book two side by side.</p></div>
    <div class="others">{others}</div>
  </div>
</section>
</main>
<div class="book-bar"><span class="price">{e(u['name'])}, from ${u['rate']}<small>{e(u['meta'][0])}</small></span><a class="btn" style="background:#fff;color:var(--red)" href="#book">Check dates</a></div>
{ls_footer()}"""
        uschema = [{"@context": "https://schema.org", "@type": "VacationRental", "name": f"{u['name']} at Little Switzerland",
                    "url": f'{LS_URL}/{u["slug"]}/', "description": u["desc"], "image": [P(p) for p in u["photos"][:8]],
                    "identifier": u["orez"],
                    "address": {"@type": "PostalAddress", **LS_ADDRESS},
                    "geo": {"@type": "GeoCoordinates", "latitude": LS_GEO[0], "longitude": LS_GEO[1]},
                    "containsPlace": {"@type": "Accommodation", "additionalType": "EntirePlace", "occupancy": {"@type": "QuantitativeValue", "value": u["sleeps"]},
                                      "numberOfBathroomsTotal": 1, "numberOfBedrooms": u.get("bedrooms", 1), "petsAllowed": True,
                                      "amenityFeature": [{"@type": "LocationFeatureSpecification", "name": n, "value": True} for n in LS_AMENITIES]},
                    "checkinTime": "16:00", "checkoutTime": "11:00",
                    "containedInPlace": {"@type": "LodgingBusiness", "name": "Little Switzerland Cabins", "url": LS_URL + "/"}}]
        d = out / u["slug"]
        d.mkdir(parents=True, exist_ok=True)
        (d / "index.html").write_text(page("ls", depth=1, title=f"{u['name']} | Little Switzerland Cabins, Jasper AR",
            desc=f"{u['name']} at Little Switzerland: {u['tagline'].lower()}. {u['meta'][0]}, from ${u['rate']} a night, 2.5 miles north of Jasper, Arkansas.",
            canonical=f'{LS_URL}/{u["slug"]}/', body=ubody, schema=uschema, og_image=P(u["hero"]), theme_color="#d52b1e"))
    return out


# ---------------------------------------------------------------------------
# MORWOOD HOUSE
# ---------------------------------------------------------------------------
def inlay(woods, labels=True):
    spans = "".join(f'<span style="--w:{c};--t:{t}">' + (f"<em>{e(n)}</em>" if labels else "") + "</span>" for n, c, t in woods)
    return f'<div class="inlay" role="img" aria-label="Wood species inlaid in the game room: {e(", ".join(n for n, _, _ in woods))}">{spans}</div>'


def build_mw():
    out = DIST / "morwood-house"
    M = MW_PHOTOS
    woods_li = "".join(f'<li><i style="--w:{c}"></i>{e(n)}</li>' for n, c, _ in WOODS)
    amen = "".join(f'<div><h3>{e(h)}</h3><ul>{"".join(f"<li>{e(x)}</li>" for x in items)}</ul></div>' for h, items in MW_AMENITIES)
    body = f"""<header class="site-header">
  <div class="wrap">
    <a class="brand" href="./">Morwood House</a>
    <button class="nav-toggle" aria-expanded="false" aria-controls="nav">Menu</button>
    <nav class="nav" id="nav" aria-label="Main">
      <a href="#house">The house</a>
      <a href="#game-room">Game room</a>
      <a href="#evenings">Hot tub</a>
      <a href="#photos">Photos</a>
      <a href="#area">Nearby</a>
      <a class="btn btn-primary" href="#book">Check dates</a>
    </nav>
  </div>
</header>
<main id="main">
<section class="mw-hero">
  <img src="{P(M['hero'])}" alt="The hot tub on Morwood House's back deck at sunset, with the Ozark ridgeline behind" fetchpriority="high">
  <div class="wrap">
    <h1>Twenty-seven kinds of wood. One hot tub facing the sunset.</h1>
    <p class="lede">A 2,400 square foot mountaintop home on 15 private acres, one mile south of Jasper. Three bedrooms, a game room built by hand, and room for eight.</p>
    <div class="actions"><a class="btn btn-primary" href="#book">Check dates</a><a class="btn btn-ghost" href="#photos">See all photos</a></div>
  </div>
</section>
{inlay(WOODS)}

<section class="section" id="house">
  <div class="wrap intro">
    <div class="measure">
      <h2>A house named for its wood</h2>
      <p>The game room floor is local hickory with black walnut inlay. The ceiling is whitewashed maple, patterned in walnut. The walls are slabs of dogwood, catalpa, sweet gum, black locust, mimosa, persimmon, osage orange and cypress, with walnut set between every one.</p>
      <p>Outside, it's 15 acres of Ozark woods, a deck that looks west over the hills, and a fire pit in the yard. Town is a mile away. It doesn't feel like it.</p>
      <p>Just updated: new flooring, new furniture, and fresh felt on the pool table.</p>
    </div>
    <dl class="facts">
      <div><dt>8</dt><dd>guests, 3 queen bedrooms plus a sleeper sofa</dd></div>
      <div><dt>2</dt><dd>full bathrooms</dd></div>
      <div><dt>15</dt><dd>private acres</dd></div>
      <div><dt>2,400</dt><dd>square feet</dd></div>
      <div><dt>1 mi</dt><dd>to downtown Jasper</dd></div>
      <div><dt>$205</dt><dd>a night and up</dd></div>
    </dl>
  </div>
</section>

<section class="section" id="game-room" style="background:var(--surface)">
  <div class="wrap spread">
    <div class="pics">
      <img class="big" src="{P(M['game'][0])}" alt="The game room with pool table, slab wood walls and hickory floor" loading="lazy">
      <img class="sm" src="{P(M['game'][1])}" alt="Ping pong and pool table in the game room" loading="lazy">
      <img class="sm" src="{P(M['living'][0])}" alt="Living room with fireplace" loading="lazy">
    </div>
    <div>
      <h2>The game room</h2>
      <p>Pool table, ping pong table, and walls you'll keep touching. This is where rainy days and late nights end up. Kids love it. So do the adults who swear they're only playing one game.</p>
      <ul class="woods">{woods_li}<li><i style="--w:repeating-linear-gradient(90deg,#8a6a4a 0 4px,#5a3e28 4px 8px)"></i>and about sixteen more</li></ul>
    </div>
  </div>
</section>

<section class="section evening" id="evenings">
  <div class="wrap">
    <div class="wide"><img src="{P(M['sunset'])}" alt="Sunset over the Ozark hills from Morwood House" loading="lazy"></div>
    <div class="three">
      <div><img src="{P(M['tub'])}" alt="Hot tub on the deck with towels ready" loading="lazy"><h3>Hot tub</h3><p>On the back deck, facing west. Built for after a day of hiking.</p></div>
      <div><img src="{P(M['deck'])}" alt="The upper deck with a view over the hills" loading="lazy"><h3>Two decks</h3><p>Coffee in the morning, the grill at night, and a long view either way.</p></div>
      <div><img src="{P(M['fire'])}" alt="Stone fire pit in the yard below the house" loading="lazy"><h3>Fire pit</h3><p>Down in the yard under the pines. Bring marshmallows.</p></div>
    </div>
  </div>
</section>

<section class="section" id="sleeping">
  <div class="wrap">
    <h2 class="h2">Where everyone sleeps</h2>
    <p class="lead">Three bedrooms with queen beds and a sleeper sofa in the living room. Two full baths, one with a clawfoot tub.</p>
    <div class="rooms">
      <figure><img src="{P(M['beds'][0])}" alt="Bedroom one with queen bed and deck door" loading="lazy"><figcaption><b>Bedroom 1</b>Queen bed, door to the deck</figcaption></figure>
      <figure><img src="{P(M['beds'][1])}" alt="Bedroom two with queen bed" loading="lazy"><figcaption><b>Bedroom 2</b>Queen bed</figcaption></figure>
      <figure><img src="{P(M['beds'][2])}" alt="Bedroom three with queen bed" loading="lazy"><figcaption><b>Bedroom 3</b>Queen bed</figcaption></figure>
      <figure><img src="{P(M['sofa'])}" alt="Living room with sleeper sofa" loading="lazy"><figcaption><b>Living room</b>Sleeper sofa for guests 7 and 8</figcaption></figure>
    </div>
  </div>
</section>

<section class="section" style="background:var(--surface)">
  <div class="wrap spread flip">
    <div class="pics">
      <img class="big" src="{P(M['kitchen'][0])}" alt="Open kitchen and long dining table" loading="lazy">
      <img class="sm" src="{P(M['kitchen'][1])}" alt="Kitchen with granite island" loading="lazy">
      <img class="sm" src="{P(M['kitchen'][2])}" alt="Dining table for eight" loading="lazy">
    </div>
    <div>
      <h2>A real kitchen</h2>
      <p>Full size fridge, stove and oven, a granite island, and a dining table that seats the whole group. Pots, pans, spices and coffee are already here. There's a gas grill on the deck and a washer and dryer for the trip home.</p>
    </div>
  </div>
</section>

<section class="section" id="photos">
  <div class="wrap">
    <h2 class="h2">Every photo</h2>
    <p class="lead">Tap any photo to see it full size.</p>
    {gallery(M['all'], "Morwood House")}
  </div>
</section>

<section class="section" id="book" style="background:var(--surface)">
  <div class="wrap book-split">
    <div>
      <h2 class="h2">Check dates</h2>
      <p class="lead">Live availability and pricing. Book direct and skip the Airbnb service fee.</p>
      {orez_slot("booking", [MW_OREZ], "Pick your dates for Morwood House", "Synced with Airbnb and VRBO, so what you see is what's open.", MW_HOSTED + "/#availability", "See open dates and book")}
    </div>
    <div class="policy">
      <dl>
        <dt>Rate</dt><dd>$205 to $235 a night</dd>
        <dt>Sleeps</dt><dd>Up to 8</dd>
        <dt>Check in</dt><dd>After 4 PM, lockbox</dd>
        <dt>Check out</dt><dd>By 11 AM</dd>
        <dt>Renter</dt><dd>21 or older</dd>
        <dt>Smoking</dt><dd>Not allowed</dd>
        <dt>Pets</dt><dd>Ask before you book</dd>
        <dt>Questions</dt><dd><a href="tel:{PHONE_TEL}">{PHONE}</a></dd>
      </dl>
    </div>
  </div>
</section>

<section class="section" id="reviews">
  <div class="wrap">
    <div class="score"><b>9.6</b><span>out of 10 on VRBO, from 222 reviews. Perfect 10s for check in and communication.</span></div>
    <div class="review-grid">{review_figs(MW_REVIEWS)}</div>
    {orez_slot("reviews", [MW_OREZ], "More reviews", "Recent reviews from every channel load here.", MW_HOSTED + "/reviews", "Read all reviews")}
  </div>
</section>

<section class="section celebrate">
  <div class="wrap">
    <div>
      <h2>Birthdays, reunions, the whole crew</h2>
      <p>Guests have thrown 50th birthdays here and brought three generations for a long weekend. Need more beds? Little Switzerland's five cabins are 3&frac12; miles up Highway 7. Book them together and you can fit up to 22.</p>
    </div>
    <div style="display:flex;flex-wrap:wrap;gap:.75rem"><a class="btn btn-primary" href="tel:{PHONE_TEL}">Call about a group</a><a class="btn btn-ghost" href="{LS_URL}">See Little Switzerland</a></div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <h2 class="h2">What's here</h2>
    <div class="amen">{amen}</div>
  </div>
</section>

<section class="section" id="area" style="background:var(--surface)">
  <div class="wrap">
    <h2 class="h2">Nearby</h2>
    <p class="lead">You're a few minutes from the Buffalo National River and the Arkansas Grand Canyon overlook.</p>
    {area_list(AREA)}
  </div>
</section>

<section class="section" id="faq">
  <div class="wrap">
    <h2 class="h2">Good to know</h2>
    {faq_html(MW_FAQ)}
  </div>
</section>
</main>
<div class="book-bar"><span class="price">From $205 a night<small>Sleeps 8, 15 acres, hot tub</small></span><a class="btn btn-primary" href="#book">Check dates</a></div>
{footer("Morwood House", "mw", [("Cabins in the Ozarks", HUB_URL), ("Little Switzerland", LS_URL)], inlay(WOODS[:8], labels=False).replace('class="inlay"', 'class="inlay" style="height:18px;margin-top:2rem;border-width:2px"'))}"""
    schema = [{"@context": "https://schema.org", "@type": "VacationRental", "name": "Morwood House", "url": MW_URL + "/",
               "description": MW_DESC, "image": [P(p) for p in M["all"][:10]], "identifier": MW_OREZ,
               "address": {"@type": "PostalAddress", **MW_ADDRESS},
               "geo": {"@type": "GeoCoordinates", "latitude": MW_GEO[0], "longitude": MW_GEO[1]},
               "telephone": PHONE_TEL, "email": EMAIL, "checkinTime": "16:00", "checkoutTime": "11:00",
               "containsPlace": {"@type": "Accommodation", "additionalType": "EntirePlace",
                                 "occupancy": {"@type": "QuantitativeValue", "value": 8},
                                 "numberOfBedrooms": 3, "numberOfBathroomsTotal": 2,
                                 "floorSize": {"@type": "QuantitativeValue", "value": 2400, "unitCode": "FTK"},
                                 "bed": [{"@type": "BedDetails", "typeOfBed": "Queen", "numberOfBeds": 3}, {"@type": "BedDetails", "typeOfBed": "Sofa bed", "numberOfBeds": 1}],
                                 "amenityFeature": [{"@type": "LocationFeatureSpecification", "name": n, "value": True} for n in MW_AMENITY_FLAT]},
               "parentOrganization": {"@type": "Organization", "name": "Cabins in the Ozarks", "url": HUB_URL}},
              faq_schema(MW_FAQ)]
    out.mkdir(parents=True, exist_ok=True)
    (out / "index.html").write_text(page("mw", title="Morwood House | Hot tub, game room, 15 private acres near Jasper, Arkansas",
        desc=MW_DESC, canonical=MW_URL + "/", body=body, schema=schema, og_image=P(M["hero"]), theme_color="#1b140f"))
    return out


# ---------------------------------------------------------------------------
# HUB: CABINS IN THE OZARKS
# ---------------------------------------------------------------------------
def route_svg():
    # A simplified strip map of Scenic Byway 7, north at top. Not to scale.
    road = "M150 20 C 180 90, 110 150, 140 220 S 200 320, 160 390 S 100 470, 150 540 S 210 640, 170 720"
    return f"""<svg class="route" viewBox="0 0 520 760" role="img" aria-labelledby="route-t route-d">
  <title id="route-t">Map of Scenic Byway 7 through Jasper, Arkansas</title>
  <desc id="route-d">Little Switzerland sits 2.5 miles north of Jasper and Morwood House 1 mile south, both on Highway 7. The Buffalo National River crosses the highway north of both.</desc>
  <path class="river" d="M10 150 C 90 130, 200 175, 300 150 S 450 120, 515 150"/>
  <text class="river-label" x="330" y="128">Buffalo National River</text>
  <path class="road draw" d="{road}"/>
  <path class="road-dash" d="{road}"/>
  <text class="town" x="180" y="30">to Harrison</text>
  <a href="{LS_URL}">
    <circle cx="175" cy="300" r="13" fill="#d52b1e" stroke="#fff" stroke-width="4"/>
    <text class="ls-label" x="203" y="300">Little Switzerland</text>
    <text class="sub" x="204" y="322">2&#189; miles north of Jasper</text>
  </a>
  <circle cx="136" cy="430" r="8" fill="#13231b" stroke="#e2e1da" stroke-width="3"/>
  <text class="town" x="156" y="436">Jasper</text>
  <a href="{MW_URL}">
    <circle cx="137" cy="520" r="13" fill="#d9a21b" stroke="#1b140f" stroke-width="4"/>
    <text class="mw-label" x="172" y="522">Morwood House</text>
    <text class="sub" x="173" y="545">1 mile south of Jasper</text>
  </a>
  <text class="town" x="214" y="664">Arkansas Grand Canyon overlook</text>
  <text class="town" x="198" y="740">to Russellville</text>
  <text class="sub" x="10" y="752" style="font-size:11px;opacity:.6">Not to scale</text>
</svg>"""


def build_hub():
    out = DIST / "hub"
    L, M = LS_UNITS, MW_PHOTOS
    inlay_mini = "".join(f'<i style="--w:{c}"></i>' for _, c, _ in WOODS)
    # Chooser data rendered as static HTML, toggled by a few lines of JS
    choices = []
    for i, (key, label, picks, note) in enumerate(CHOOSER):
        cards = "".join(
            f'<a class="match" style="--c:{c}" href="{url}"><img src="{P(img)}" alt="" loading="lazy"><div><b>{e(name)}</b><span>{e(why)}</span></div></a>'
            for name, why, url, img, c in picks)
        choices.append(f'<div class="answer-set" data-for="{key}"{"" if i == 0 else " hidden"}><div class="answer">{cards}</div><p class="answer-note">{e(note)}</p></div>')
    buttons = "".join(f'<button type="button" data-pick="{k}" aria-pressed="{"true" if i == 0 else "false"}">{e(l)}</button>' for i, (k, l, _, _) in enumerate(CHOOSER))

    units_all = [(u["name"], "#d52b1e") for u in L] + [("Morwood House", "#d9a21b")]
    ribbon = '<div class="ribbon-preview" aria-hidden="true"><span></span>' + "".join(
        f'<span class="h{" wk2" if d > 7 else ""}">{d}</span>' for d in range(1, 15))
    for n, c in units_all:
        ribbon += f'<span class="u"><i style="--c:{c}"></i>{e(n)}</span>' + "".join(f'<span class="d{" wk2" if d > 7 else ""}"></span>' for d in range(1, 15))
    ribbon += "</div>"

    body = f"""<header class="site-header">
  <div class="wrap">
    <a class="brand" href="./">Cabins in the Ozarks</a>
    <button class="nav-toggle" aria-expanded="false" aria-controls="nav">Menu</button>
    <nav class="nav" id="nav" aria-label="Main">
      <a href="{LS_URL}">Little Switzerland</a>
      <a href="{MW_URL}">Morwood House</a>
      <a href="#choose">Which one?</a>
      <a href="#area">Nearby</a>
      <a href="#faq">FAQ</a>
      <a class="btn btn-primary" href="#dates">Check dates</a>
    </nav>
  </div>
</header>
<main id="main">
<section class="hub-hero">
  <div class="wrap">
    <div>
      <h1>Two places to stay on Scenic Byway 7.</h1>
      <p class="lead lede">Historic cabins north of Jasper and a mountaintop house to the south, minutes from the Buffalo National River. Sleep 2 or sleep 22. Book direct with the owner.</p>
      <div class="actions"><a class="btn btn-primary" href="#choose">Find your stay</a><a class="btn btn-ghost" href="#dates">See open dates</a></div>
    </div>
    {route_svg()}
  </div>
  <div class="doors">
    <a class="door door-ls" href="{LS_URL}">
      <div class="img"><img src="{P(LS_HERO)}" alt="Cabin 1 at Little Switzerland" loading="lazy"></div>
      <div class="body">
        <h2>Little Switzerland</h2>
        <p>Five cabins and suites on a homestead settled by Swiss families in 1891. Porches, a picnic pavilion, a fire pit, and Jasper five minutes away.</p>
        <ul class="meta"><li>5 units</li><li>Sleeps 2 to 4 each</li><li>From $85</li><li>Dogs welcome</li></ul>
        <span class="go">See the cabins</span>
      </div>
    </a>
    <a class="door door-mw" href="{MW_URL}">
      <div class="img"><img src="{P(M['hero'])}" alt="Morwood House hot tub at sunset" loading="lazy"></div>
      <div class="body">
        <div class="inlay-mini" aria-hidden="true">{inlay_mini}</div>
        <h2>Morwood House</h2>
        <p>A 2,400 square foot home on 15 private acres with a west facing hot tub and a game room built from 27 kinds of wood.</p>
        <ul class="meta"><li>3 bedrooms</li><li>Sleeps 8</li><li>From $205</li><li>Hot tub</li></ul>
        <span class="go">See the house</span>
      </div>
    </a>
  </div>
</section>

<section class="section chooser" id="choose">
  <div class="wrap">
    <h2>Who's coming?</h2>
    <p class="lead">Tell us who's in the car and we'll point you to the right place.</p>
    <div class="pick" role="group" aria-label="Group size">{buttons}</div>
    <div aria-live="polite">{''.join(choices)}</div>
  </div>
</section>

<section class="section cal" id="dates">
  <div class="wrap">
    <h2 class="h2">Everything that's open</h2>
    <p class="lead">All six places on one calendar, synced with Airbnb and VRBO.</p>
    {orez_slot("ribbon-calendar", [u['orez'] for u in L] + [MW_OREZ], "Live calendar for all six places", "Pick a place to see exact dates and pricing.", LS_HOSTED + "/availability", "Little Switzerland dates").replace("</a>\n</div>", f'</a> <a class="btn btn-ghost" style="color:#e2e1da;margin-left:.5rem" href="{MW_HOSTED}/#availability">Morwood House dates</a>\n</div>')}
  </div>
</section>

<section class="section" id="reviews">
  <div class="wrap">
    <h2 class="h2">From our guests</h2>
    <p class="lead">Morwood holds a 9.6 on VRBO across 222 reviews. The Little Switzerland cabins average 4.7 on Airbnb across about 600.</p>
    <div class="review-grid">{review_figs(HUB_REVIEWS)}</div>
  </div>
</section>

<section class="section" id="area" style="background:var(--surface)">
  <div class="wrap area">
    <div>
      <h2 class="h2">The Buffalo River country</h2>
      <p class="lead">Jasper is the county seat of Newton County, a small town in the middle of some of the best hiking, floating and scenery in Arkansas. Branson and Eureka Springs are each about an hour away.</p>
    </div>
    {area_list(AREA)}
  </div>
</section>

<section class="section" id="faq">
  <div class="wrap">
    <h2 class="h2">Questions people ask</h2>
    {faq_html(HUB_FAQ)}
  </div>
</section>

<section class="contact">
  <div class="wrap">
    <div><h2>Talk to the owner</h2><p style="margin:.75rem 0 0;max-width:52ch">Planning a group trip or not sure which place fits? Call or text Matt. You'll get a real answer, usually within the hour.</p></div>
    <div style="display:flex;flex-wrap:wrap;gap:.75rem"><a class="btn btn-primary" href="tel:{PHONE_TEL}">Call {PHONE}</a><a class="btn btn-ghost" href="sms:{PHONE_TEL}">Text</a></div>
  </div>
</section>
</main>
<div class="book-bar"><span class="price">2 places, 6 stays<small>From $85 a night</small></span><a class="btn btn-primary" href="#choose">Find your stay</a></div>
{footer("Cabins in the Ozarks", "hub", [("Little Switzerland", LS_URL), ("Morwood House", MW_URL)])}
<script>
document.querySelectorAll('[data-pick]').forEach(b => b.addEventListener('click', () => {{
  document.querySelectorAll('[data-pick]').forEach(x => x.setAttribute('aria-pressed', x === b));
  document.querySelectorAll('.answer-set').forEach(s => s.hidden = s.dataset.for !== b.dataset.pick);
}}));
</script>"""
    schema = [{"@context": "https://schema.org", "@type": "Organization", "name": "Cabins in the Ozarks", "url": HUB_URL + "/",
               "telephone": PHONE_TEL, "email": EMAIL, "description": HUB_DESC,
               "areaServed": "Jasper, Arkansas", "founder": {"@type": "Person", "name": "Matt Mowen"},
               "subOrganization": [{"@type": "LodgingBusiness", "name": "Little Switzerland Cabins", "url": LS_URL + "/"},
                                   {"@type": "LodgingBusiness", "name": "Morwood House", "url": MW_URL + "/"}]},
              faq_schema(HUB_FAQ)]
    out.mkdir(parents=True, exist_ok=True)
    (out / "index.html").write_text(page("hub", title="Cabins in the Ozarks | Cabins near the Buffalo River in Jasper, Arkansas",
        desc=HUB_DESC, canonical=HUB_URL + "/", body=body, schema=schema, og_image=P(M["hero"]), theme_color="#13231b"))
    return out


# ---------------------------------------------------------------------------
def write_meta(out, url, name, summary, pages):
    """robots.txt (AI crawlers welcome), sitemap.xml, llms.txt"""
    (out / "robots.txt").write_text(
        "User-agent: *\nAllow: /\n\n" +
        "".join(f"User-agent: {b}\nAllow: /\n\n" for b in ["GPTBot", "OAI-SearchBot", "ChatGPT-User", "PerplexityBot", "ClaudeBot", "Claude-User", "Claude-SearchBot", "Google-Extended", "Bingbot"]) +
        f"Sitemap: {url}/sitemap.xml\n")
    (out / "sitemap.xml").write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' +
        "".join(f"  <url><loc>{url}{p}</loc><changefreq>weekly</changefreq></url>\n" for p, _ in pages) + "</urlset>\n")
    (out / "llms.txt").write_text(f"# {name}\n\n> {summary}\n\n" + LLMS_COMMON + "\n## Pages\n\n" +
        "".join(f"- [{t}]({url}{p})\n" for p, t in pages))


def main():
    if DIST.exists():
        shutil.rmtree(DIST)
    for key, fn in [("little-switzerland", build_ls), ("morwood-house", build_mw), ("hub", build_hub)]:
        out = fn()
        (out / "assets").mkdir(exist_ok=True)
        shutil.copy(SRC / "shared/base.css", out / "assets/base.css")
        shutil.copy(SRC / "shared/site.js", out / "assets/site.js")
        shutil.copy(SRC / key / "theme.css", out / "assets/theme.css")
    write_meta(DIST / "little-switzerland", LS_URL, "Little Switzerland Cabins", LS_DESC,
               [("/", "Little Switzerland home")] + [(f'/{u["slug"]}/', f'{u["name"]}: {u["tagline"]}, sleeps {u["sleeps"]}, from ${u["rate"]}') for u in LS_UNITS])
    write_meta(DIST / "morwood-house", MW_URL, "Morwood House", MW_DESC, [("/", "Morwood House home")])
    write_meta(DIST / "hub", HUB_URL, "Cabins in the Ozarks", HUB_DESC, [("/", "Cabins in the Ozarks home")])
    print("built:", ", ".join(p.name for p in DIST.iterdir()))


if __name__ == "__main__":
    main()
