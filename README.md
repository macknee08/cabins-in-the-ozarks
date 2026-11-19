# Cabins in the Ozarks

Three sites for Matt Mowen's rentals in Jasper, Arkansas. Built by Upstream Media.

| Folder | Domain | What |
|---|---|---|
| `dist/hub` | cabinsintheozarks.com | Landing page connecting both properties |
| `dist/little-switzerland` | littleswitzerlandarkansas.com | 5 historic cabins and suites, a page per unit |
| `dist/morwood-house` | morwoodhouse.com | 3 bed home on 15 acres |

## Edit and rebuild

All content (rates, photos, reviews, FAQs) lives in `data.py`.

```
python3 build.py     # builds dist/ (production, real domains)
python3 preview.py   # packs dist/ into preview/ with cross links that work on one host
```

`docs/` is the published GitHub Pages preview (a copy of `preview/`).

## OwnerRez widgets

Every booking calendar, ribbon calendar and reviews block is an `.orez-slot` div marked with an
`OWNERREZ WIDGET SLOT` comment listing the property IDs (ORP471942 to ORP471947). Until the widget code
is pasted in, each slot links to Matt's existing OwnerRez hosted booking page so bookings still work.

## AI search

Each site ships `llms.txt`, a `robots.txt` that allows GPTBot, OAI-SearchBot, PerplexityBot and ClaudeBot,
a `sitemap.xml`, and JSON-LD (LodgingBusiness, VacationRental, FAQPage) on every page.
