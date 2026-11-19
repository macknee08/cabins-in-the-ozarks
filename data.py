"""All site content in one place. Facts come from Matt's OwnerRez account,
his Airbnb/VRBO listings, Google Maps, and the original littleswitzerlandarkansas.com."""

HUB_URL = "https://cabinsintheozarks.com"
LS_URL = "https://littleswitzerlandarkansas.com"
MW_URL = "https://morwoodhouse.com"

# Existing OwnerRez hosted booking pages: used as working fallbacks until widgets are placed
LS_HOSTED = "https://little-switzerland.hosted.ownerrez.com"
MW_HOSTED = "https://morwoodhouse.hosted.ownerrez.com"

PHONE = "(870) 416-2383"
PHONE_TEL = "+18704162383"
EMAIL = "mmowen213@gmail.com"

LS_GEO = (36.0331993, -93.1628646)
MW_GEO = (35.9977125, -93.1868248)
LS_ADDRESS = {"streetAddress": "Scenic Byway 7 (Highway 7 North)", "addressLocality": "Jasper", "addressRegion": "AR", "postalCode": "72641", "addressCountry": "US"}
MW_ADDRESS = {"streetAddress": "Highway 7 South", "addressLocality": "Jasper", "addressRegion": "AR", "postalCode": "72641", "addressCountry": "US"}
ADDRESS_LINES = {
    "ls": "Scenic Byway 7, 2.5 miles north of Jasper, Arkansas 72641",
    "mw": "Highway 7 South, 1 mile south of Jasper, Arkansas 72641",
    "hub": "Jasper, Arkansas 72641, on Scenic Byway 7",
}

LS_DESC = ("Historic cabins and suites on Scenic Byway 7, 2.5 miles north of Jasper, Arkansas, near the Buffalo National River. "
           "Five units sleeping 2 to 4, from $85 a night. Dogs welcome. Book direct.")
MW_DESC = ("Morwood House is a 3 bedroom, 2 bath mountaintop home on 15 private acres one mile south of Jasper, Arkansas. "
           "Sleeps 8, with a hot tub, game room and full kitchen near the Buffalo National River. Book direct.")
HUB_DESC = ("Cabins in the Ozarks: Little Switzerland's historic cabins and Morwood House, two places to stay on Scenic Byway 7 "
            "in Jasper, Arkansas, near the Buffalo National River and the Arkansas Grand Canyon.")

# --- Little Switzerland -----------------------------------------------------
LS_HERO = "d2a29ffa704245cd948221a467b5b3c3"
LS_GROUNDS = ["65e173d50b0c41aabb12b6a398830171", "9ad965304b7040c6bf49c7c4d3aa553d", "85869a5c886a48b9b2dcbca53dcc0c5e"]
LS_AMENITIES = ["Wifi", "TV", "Air conditioning", "Mini fridge", "Microwave", "Coffee maker", "Outdoor grill", "Fire pit",
                "Covered picnic pavilion", "Free parking", "Pet friendly", "Self check in"]

LS_UNITS = [
    {"slug": "cabin-1", "num": "1", "name": "Cabin 1", "orez": "ORP471942", "rate": 100, "sleeps": 4, "bedrooms": 2,
     "hosted": "little-switzerland-a-newton-co-landmark-cabin-1-orp5b73386x",
     "tagline": "The two story cabin with a big balcony",
     "meta": ["Sleeps 4", "2 bedrooms", "2 queen beds", "1 bath"],
     "desc": "The original two story cabin. A queen bed and full bath downstairs, a second queen with its own vanity and sink upstairs, a front porch for morning coffee and a large balcony up top.",
     "hero": "d2a29ffa704245cd948221a467b5b3c3",
     "photos": ["d2a29ffa704245cd948221a467b5b3c3", "26d633a131604fbab90c1c4da67cb7bf", "33460caa7afa4941b9e542ba628e7c63", "7c8b253939e74be0b1835ea73be59aec",
                "250c5523ebe940119e7870d072a43171", "2aec86439b9d467e9bdf542d36996287", "141fdc432f894bc3a28c6547287d65de", "92f9b9b053e645ad9200709333250974",
                "5aa2a908de34400fb3539e367bc95296", "65e173d50b0c41aabb12b6a398830171", "9ad965304b7040c6bf49c7c4d3aa553d", "85869a5c886a48b9b2dcbca53dcc0c5e",
                "f226365c2a5e40cebd105789c1a71b4c"],
     "details": [("Sleeping", ["Queen bed downstairs", "Queen bed upstairs", "Upstairs vanity and sink"]),
                 ("Bath", ["Full bath downstairs", "Custom tiled shower and tub", "Towels, soap and shampoo"]),
                 ("In the cabin", ["Mini fridge, microwave, coffee maker", "Wifi and TV", "Air conditioning", "No full kitchen"]),
                 ("Outside", ["Front porch", "Large private balcony", "Shared pavilion, grills and fire pit"])]},
    {"slug": "cabin-2", "num": "2", "name": "Cabin 2", "orez": "ORP471943", "rate": 110, "sleeps": 2, "bedrooms": 1,
     "hosted": "little-switzerland-cabin-2-newly-renovated-orp5b73387x",
     "tagline": "Newly renovated, with a king bed",
     "meta": ["Sleeps 2", "King bed", "1 bath", "Renovated Dec 2025"],
     "desc": "Our first fully renovated cabin, reopened in December 2025. A pillow top king, new granite, new floors, paint, lighting, furniture and appliances. The split level layout puts a sitting area on one floor and the bedroom on the next, with a front porch and a private balcony.",
     "hero": "d87ac77e8d1f432f8223d151f1dd26e3",
     "photos": ["d87ac77e8d1f432f8223d151f1dd26e3", "4d938eff1f0646648489484643a58ad3", "1523f13d36774ce0ab0be660fb690146", "4e026bfd92564926abd1639aee33d0cd",
                "a026501b3f954c51aeb7e28ae4dd8b62", "49c64c38490e4e558b93ca38c7b9dbcb", "d67eab96e0024a05aed639a8b9ce2fbe", "7bd18f64c7734253855945581d4ea0ed",
                "2410557905d941a283fa2decd8550946", "ea38ac7ddd8c4765a7293b4b5dd19073", "6d369792f84646ad8b763012a43f81ae"],
     "details": [("Sleeping", ["New pillow top king bed", "Sitting area on the entry level"]),
                 ("Bath", ["Full bath", "New fixtures and lighting"]),
                 ("In the cabin", ["Granite counter", "Mini fridge, microwave, coffee maker", "Wifi and TV", "No full kitchen"]),
                 ("Outside", ["Front porch", "Private balcony", "Shared pavilion, grills and fire pit"])]},
    {"slug": "room-3", "num": "3", "name": "Room 3", "orez": "ORP471944", "rate": 85, "sleeps": 2, "bedrooms": 1,
     "hosted": "cabin-3-room-3-historic-little-switzerland-orp5b73388x",
     "tagline": "Queen suite that connects to Room 4",
     "meta": ["Sleeps 2", "Queen bed", "1 bath", "Connects to Room 4"],
     "desc": "A bright, hotel style suite in Cabin 3 with a queen bed, full bath and lots of window light. An interior door opens into Room 4, so two couples or a family can share without sharing a bathroom.",
     "hero": "f33c68409d7f442ca21dc1d4e1ea8ee3",
     "photos": ["f33c68409d7f442ca21dc1d4e1ea8ee3", "de58a434417443ed8b1d2a1723052f5c", "01c21e874a57431e8e20395434c5a2f8", "ea4f834b20e74ca1a487e3eb918c9567",
                "185fcefd1671412bb2f0ed1ac96e3412", "1c287ceb0424469c9fcd8fed3384675f", "402f498557fb4443949df78cd2f4a439", "d072187db4ff459a82f513e4bea879f3",
                "edbd5c10bd2c4c34a1ad9f79ededfe68", "5172f8dca98f4da194072373cd5a6dd1", "28012fccbf354ac4bd1e4f7943f5c29d", "882d32ae0fbb4ad19bcdc786a8491220"],
     "details": [("Sleeping", ["Queen bed", "Small seating area"]),
                 ("Bath", ["Full bath with tub and shower"]),
                 ("In the room", ["Mini fridge, microwave, coffee maker", "Wifi and TV", "Air conditioning", "No full kitchen"]),
                 ("Good to know", ["Interior door to Room 4", "Ground floor of Cabin 3", "Shared pavilion, grills and fire pit"])]},
    {"slug": "room-4", "num": "4", "name": "Room 4", "orez": "ORP471945", "rate": 90, "sleeps": 2, "bedrooms": 1,
     "hosted": "cabin-3-room-4-historic-little-switzerland-orp5b73389x",
     "tagline": "Queen suite that connects to Room 3",
     "meta": ["Sleeps 2", "Queen bed", "1 bath", "Connects to Room 3"],
     "desc": "Room 3's twin next door in Cabin 3. A queen bed, full bath and a seating corner, with an interior door you can open when you book both rooms together.",
     "hero": "96e4e4bd4bb74091be326f6e725c7f58",
     "photos": ["96e4e4bd4bb74091be326f6e725c7f58", "d51aba755259460bbbb1a6b351e0a00a", "b97ff4859e55422d88e0b1f222a46e7b", "ad77edde2ab34e4b9a7a318486ea3134",
                "5590847645964649afb11ce5d915ee62", "18b6f348c8cf42078113c8a80855aebd", "dd9a7ce3803f4b5e8444bb7fe51d12ce", "857ca61ddffd445d8cbc23c06d82efba",
                "9ec475bb86f3481e854a1c7a8ffcab55", "b66ca7540e444425b8c9626e43ab107a", "7bd41dcca5494d328070b28a1d3f8c7e", "2582bd87aadb49f585492b3992555bcc"],
     "details": [("Sleeping", ["Queen bed", "Seating corner"]),
                 ("Bath", ["Full bath with tub and shower"]),
                 ("In the room", ["Mini fridge, microwave, coffee maker", "Wifi and TV", "Air conditioning", "No full kitchen"]),
                 ("Good to know", ["Interior door to Room 3", "Fire pit right outside", "Shared pavilion and grills"])]},
    {"slug": "room-5", "num": "5", "name": "Room 5", "orez": "ORP471946", "rate": 95, "sleeps": 4, "bedrooms": 1,
     "hosted": "cabin-3-room-5-historic-little-switzerland-orp5b7338ax",
     "tagline": "Upstairs suite with a private balcony",
     "meta": ["Sleeps 4", "Queen + 2 twins", "1 bath", "Private balcony"],
     "desc": "The whole top floor of Cabin 3. A big room with a queen bed, two twin day beds, a dining table for four and a private balcony over the trees. It has the privacy of its own cabin.",
     "hero": "861ac5f33ae24eb39727f001a4610848",
     "photos": ["861ac5f33ae24eb39727f001a4610848", "33c5922bf8c9406387e0d1624a99fc92", "1527527eb4cf4941a20a5127630a0b67", "079f3bca702a4f7f875b7eeedd05822d",
                "9292fa36b288429faf800132c7b568b4", "f9c8a82d434b42beb3005d50f3055662", "cd09e9f4a41d4fda9a93e7122c9a8bc8", "362ad1c6dbcc47399b796a37e6b939a9",
                "db8df961349b43479b586b972f1d48e3", "2414accaddb44def9a15b609e2b7333f", "af5aaed7332045968adcb7b9bde754cf"],
     "details": [("Sleeping", ["Queen bed", "Two twin day beds"]),
                 ("Bath", ["Full bath with tub and shower"]),
                 ("In the room", ["Dining table for four", "Mini fridge, microwave, coffee maker", "Wifi and TV", "No full kitchen"]),
                 ("Outside", ["Private balcony", "Shared pavilion, grills and fire pit"])]},
]

LS_REVIEWS = [
    {"text": "The room was nice and clean. I was very happy with the experience.", "who": "Nick P., stayed 3 nights, October 2024, via VRBO"},
    {"text": "This place is nice and clean, the owners very helpful.", "who": "Lisa S., stayed 3 nights, September 2024, via VRBO"},
    {"text": "It was a quaint little cabin, we enjoyed our vacation. Lots to see in the area and experience, hiking etc.", "who": "Trudie W., stayed 4 nights, via VRBO"},
]

LS_FAQ = [
    ("Do the cabins have kitchens?", "No full kitchens. Every unit has a mini fridge, microwave and coffee maker, and there's a covered pavilion with charcoal grills and picnic tables out back. Jasper's restaurants are about five minutes away. If you need a full kitchen, Morwood House has one."),
    ("Are dogs allowed?", "Yes. Dogs are welcome for $25 per pet per stay. Let us know when you book."),
    ("What are check in and check out times?", "Check in is after 4 PM and check out is by 11 AM. Check in is self serve, and we send instructions before you arrive."),
    ("Where exactly are you?", "On Scenic Byway 7 (Highway 7), 2.5 miles north of Jasper, Arkansas, on the way to Harrison. The Buffalo National River crossing at Pruitt is a short drive north."),
    ("Can we book several cabins for a group?", "Yes. The five units sleep 14 together, and Rooms 3 and 4 connect through an interior door. Add Morwood House, 3.5 miles south, and you can fit 22. Call or text Matt to hold everything at once."),
    ("Is there Wifi?", "Yes, in every unit, along with a TV and air conditioning."),
    ("Why book here instead of Airbnb or VRBO?", "Same cabins, same calendar, but you book straight with the owner and skip the app's service fee."),
]

# --- Morwood House ------------------------------------------------------------
MW_OREZ = "ORP471947"
_mw = ["bcfe726a0bd449cbbc9f8c12313c51cb", "3dc657c38dcf460080e1bd9563fd40eb", "686f70a4140441269146a44282c11f68", "54661ec7f8c84341a68be14ae76bf6c3",
       "cbf8c0eb11564501b5f2f4c8c1d607e0", "6f117aead3bd44f0aa1fcdcad351a419", "a9ffe5960dc7458b9c8559ef1397462e", "b80b6a9040714fa3830772ae377e4421",
       "4508089b1f6e477ebdc16b277389f3fb", "088d9f5c854a4582b3095ff14edb8527", "75f5bda3e28b41dc943cdd7cb8446935", "951bd70349a148d1adc2f3d0cc7770a7",
       "5d404af63fe44c33a8e5b48d567b46b1", "4f38d80846d141d18575e9722d320f01", "7510a38e1dd341e1b7cbca4dafdb98ed", "5622cdb13cda4e2598b84bb6051901ab",
       "dd66d4e3a0c347e59ddcc3973c49353b", "e8a4ed5386c84f1f97955d0d9d2b45d6", "aa3cc266d2ba4d868e5b636573ab0a7b", "cc389a1599584f51a1c46e5e7b622c4d",
       "28323e57b9d540df86b834e6b13873d5", "83e96ec00770433f97c7a9635a0e004f", "38f394cb5951400fb72d324315ae55c7"]
MW_PHOTOS = {
    "hero": _mw[3], "tub": _mw[0], "sunset": _mw[20], "deck": _mw[16], "fire": _mw[5],
    "game": [_mw[6], _mw[7]], "living": [_mw[8]], "sofa": _mw[9],
    "kitchen": [_mw[10], _mw[13], _mw[14]], "beds": [_mw[12], _mw[17], _mw[18]], "bath": _mw[15],
    "all": [_mw[i] for i in [3, 1, 0, 16, 20, 21, 22, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 12, 17, 18, 15, 19]],
}

# (name, wood tone, label color) for the inlay band. Species named in Matt's own listing.
WOODS = [
    ("Hickory", "#b8895a", "#1b140f"), ("Black walnut", "#4a2e1e", "#efe4d3"), ("Whitewashed maple", "#e9dcc5", "#1b140f"),
    ("Dogwood", "#c7a27c", "#1b140f"), ("Catalpa", "#a98458", "#1b140f"), ("Sweet gum", "#8e5d43", "#efe4d3"),
    ("Black locust", "#a38f45", "#1b140f"), ("Mimosa", "#74502f", "#efe4d3"), ("Persimmon", "#3d2b22", "#efe4d3"),
    ("Osage orange", "#d9a21b", "#1b140f"), ("Cypress", "#c58f5f", "#1b140f"),
]

MW_AMENITIES = [
    ("Kitchen", ["Full fridge, stove and oven", "Microwave and toaster", "Coffee maker", "Pots, pans, dishes, spices", "Dining table for 8"]),
    ("Living", ["Fireplace", "TV", "Wifi and a laptop friendly workspace", "Central heat and air", "Washer and dryer"]),
    ("Game room", ["Pool table, new felt", "Ping pong table", "Hand inlaid hardwood"]),
    ("Outside", ["Hot tub", "Gas grill", "Two decks", "Fire pit", "15 private acres", "EV charger and free parking"]),
]
MW_AMENITY_FLAT = ["Hot tub", "Game room", "Pool table", "Ping pong table", "Fireplace", "Full kitchen", "Washer and dryer", "Wifi",
                   "Air conditioning", "Gas grill", "Fire pit", "Deck", "EV charger", "Free parking", "Mountain view"]

MW_REVIEWS = [
    {"text": "Our family likes to hike in Arkansas and my teenagers love to play games so this house was perfect for all of us. The hot tub was very relaxing after hiking nearby. The views were amazing.", "who": "Verified guest, March 2025, via VRBO"},
    {"text": "Just had our 50th Birthday party there for all 8 of our friends who have known each other since High School. The house was so great, and the views off the decks are amazing!", "who": "Brent R., Google review"},
    {"text": "If you sit in the hot tub, which I'm sure you will if you stay here, you can look up at the stars. It's a beautiful place.", "who": "Teri, Google review"},
]

MW_FAQ = [
    ("How many people does Morwood House sleep?", "Up to 8: three bedrooms with queen beds plus a sleeper sofa in the living room. There are two full bathrooms."),
    ("Is there a hot tub?", "Yes. It's on the back deck facing west over the hills, so you get the sunset from the water."),
    ("Does it have a full kitchen?", "Yes. Full size fridge, stove, oven, microwave, toaster, coffee maker, cookware, dishes and basic spices, plus a gas grill on the deck and a dining table for eight."),
    ("Where is it?", "One mile south of downtown Jasper, Arkansas, just off Highway 7 (Scenic Byway 7), on 15 private acres. The Arkansas Grand Canyon overlook is a few minutes further south."),
    ("Can we bring a dog?", "Ask before you book and we'll let you know what works for your dates."),
    ("Is there an age requirement?", "The person booking must be 21 or older. Children are welcome. Smoking is not allowed."),
    ("Can we use it for a birthday or reunion?", "Plenty of guests do. Overnight guests are capped at 8. For bigger groups, add cabins at Little Switzerland, 3.5 miles north, and call Matt before planning a gathering."),
    ("Is there EV charging?", "Yes, there's an EV charger on site and free parking."),
]

# --- Shared -------------------------------------------------------------------
AREA = [
    ("Buffalo National River", "America's first national river. Float, swim and fish from accesses like Pruitt, Ozark and Kyle's Landing."),
    ("Arkansas Grand Canyon", "The overlook on Highway 7 south of Jasper, with miles of Ozark ridges below. Best near sunset."),
    ("Lost Valley Trail", "An easy hike near Ponca to Eden Falls and a cave you can walk into."),
    ("Elk in Boxley Valley", "Wild elk graze the fields near Ponca, most often at dawn and dusk."),
    ("Hawksbill Crag", "A rock ledge over the upper Buffalo valley and one of the most photographed spots in Arkansas."),
    ("Downtown Jasper", "Ozark Cafe, Pizza on the Square, and the Cliff House Inn restaurant on the canyon rim."),
    ("Mystic Caverns", "Guided cave tours on Highway 7 north toward Harrison."),
    ("Branson and Eureka Springs", "Each about an hour away for shows, shops and a day trip."),
]

def _u(slug):
    return next(u for u in LS_UNITS if u["slug"] == slug)

CHOOSER = [
    ("two", "Just the two of us", [
        ("Cabin 2", "Renovated, king bed, private balcony. From $110.", f"{LS_URL}/cabin-2/", _u("cabin-2")["hero"], "#d52b1e"),
        ("Room 3 or Room 4", "Quiet queen suites. From $85.", f"{LS_URL}/room-3/", _u("room-3")["hero"], "#d52b1e"),
        ("Morwood House", "The whole house and the hot tub to yourselves. From $205.", MW_URL, MW_PHOTOS["hero"], "#d9a21b"),
    ], "Cabin 2 is our newest renovation and the one couples book first."),
    ("family", "Family of four", [
        ("Cabin 1", "Two bedrooms over two floors, porch and balcony. From $100.", f"{LS_URL}/cabin-1/", _u("cabin-1")["hero"], "#d52b1e"),
        ("Room 5", "Queen plus two twins, table for four, balcony. From $95.", f"{LS_URL}/room-5/", _u("room-5")["hero"], "#d52b1e"),
        ("Morwood House", "If you want a full kitchen and a game room for the kids.", MW_URL, MW_PHOTOS["game"][0], "#d9a21b"),
    ], "The Little Switzerland cabins have mini fridges and microwaves but no full kitchen. Morwood has a full one."),
    ("eight", "Up to eight", [
        ("Morwood House", "3 bedrooms, sleeper sofa, 2 baths, hot tub, game room.", MW_URL, MW_PHOTOS["hero"], "#d9a21b"),
        ("All of Cabin 3", "Rooms 3, 4 and 5 together sleep 8. Rooms 3 and 4 connect.", f"{LS_URL}/#cabins", _u("room-5")["hero"], "#d52b1e"),
    ], "Morwood is one big house. Cabin 3 gives everyone their own room and bath."),
    ("crew", "The whole crew", [
        ("Morwood House", "Sleeps 8. The gathering spot, with the kitchen and game room.", MW_URL, MW_PHOTOS["game"][0], "#d9a21b"),
        ("All of Little Switzerland", "Five cabins and suites that sleep 14, 3.5 miles north.", LS_URL, LS_GROUNDS[0], "#d52b1e"),
    ], "Together that's 22 beds. Call or text Matt at (870) 416-2383 to hold everything at once."),
]

HUB_REVIEWS = [
    {**MW_REVIEWS[0], "place": "Morwood House", "color": "#8a5a12"},
    {**LS_REVIEWS[1], "place": "Little Switzerland", "color": "#d52b1e"},
    {**MW_REVIEWS[1], "place": "Morwood House", "color": "#8a5a12"},
]

HUB_FAQ = [
    ("Where are your cabins?", "Both properties are on Scenic Byway 7 (Highway 7) in Jasper, Arkansas. Little Switzerland is 2.5 miles north of town and Morwood House is 1 mile south, about 3.5 miles apart."),
    ("Which is best for a couple?", "Cabin 2 at Little Switzerland, renovated in December 2025 with a king bed and private balcony, from $110 a night. Rooms 3 and 4 are queen suites from $85. For a splurge, Morwood House gives you a whole house and a hot tub."),
    ("Which is best for a family or a group?", "Morwood House sleeps 8 with three bedrooms, two baths, a full kitchen, hot tub and game room. At Little Switzerland, Cabin 1 and Room 5 each sleep 4."),
    ("What's the largest group you can host?", "22 overnight guests if you book Morwood House (8) and all five Little Switzerland units (14) together."),
    ("Are you pet friendly?", "Dogs are welcome at Little Switzerland for $25 per pet per stay. For Morwood House, ask before you book."),
    ("How close are you to the Buffalo National River?", "A few minutes. Both properties are on Highway 7, which crosses the Buffalo at Pruitt just north of Little Switzerland."),
    ("Do the cabins have kitchens?", "Morwood House has a full kitchen. The Little Switzerland units have a mini fridge, microwave and coffee maker, plus shared grills under a covered pavilion."),
    ("Why book direct?", "Same places and the same calendar as Airbnb and VRBO, without the app's service fee, and you deal with the owner."),
]

LLMS_COMMON = f"""Owner: Matt Mowen. Phone: {PHONE}. Email: {EMAIL}. Book direct on the sites below.

## Properties
- Little Switzerland Cabins ({LS_URL}): 5 rentals on Scenic Byway 7, 2.5 miles north of Jasper, Arkansas 72641. Homestead dating to 1891. Cabin 1 (sleeps 4, 2 queens, from $100), Cabin 2 (sleeps 2, king, renovated Dec 2025, from $110), Room 3 (sleeps 2, queen, from $85), Room 4 (sleeps 2, queen, from $90), Room 5 (sleeps 4, queen + 2 twins, balcony, from $95). No full kitchens (mini fridge, microwave, coffee maker). Dogs welcome, $25 per pet. Shared pavilion, grills, fire pit. Airbnb ratings 4.69 to 4.77.
- Morwood House ({MW_URL}): 2,400 sq ft home on 15 private acres, 1 mile south of Jasper off Highway 7. 3 bedrooms (3 queens) plus sleeper sofa, 2 baths, sleeps 8. Hot tub facing the sunset, game room with pool and ping pong tables built from about 27 local wood species, full kitchen, fireplace, washer/dryer, EV charger. From $205 a night. 9.6/10 on VRBO from 222 reviews.
- Combined: up to 22 guests. Check in 4 PM, check out 11 AM.

## Nearby
Buffalo National River, Arkansas Grand Canyon overlook, Lost Valley Trail, Boxley Valley elk, Hawksbill Crag, Mystic Caverns, downtown Jasper. Branson and Eureka Springs about an hour away.
"""
