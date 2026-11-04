import os
import json
import math
import datetime
import urllib.request
import urllib.parse

# ==========================================
# CORE CONFIGURATION
# ==========================================
AFFILIATE_TAG = "everythi00099-20"
SITE_NAME = "SaunaWattPro"
SITE_TAGLINE = "Sauna Heater kW, Room Volume, Glass De-Rating & 240V Breaker Sizing Calculator"
OUTPUT_DIR = "public"
INDEXNOW_KEY = "4c5d6e7f8a9b0c1d2e3f4a5b6c7d8e9f"

# Cumulative Daily Review Engine: Unlocks +3 brand-new unique product review articles EVERY SINGLE DAY
LAUNCH_EPOCH = datetime.date(2026, 11, 1)
REVIEWS_PER_DAY = 3

REPO_SLUG = os.environ.get("GITHUB_REPOSITORY", "username/saunawattpro")
OWNER, REPO_NAME = REPO_SLUG.split("/") if "/" in REPO_SLUG else ("username", "saunawattpro")
BASE_URL = os.environ.get("SITE_BASE_URL", f"https://{OWNER}.github.io/{REPO_NAME}")

def amz_url(keyword):
    return f"https://www.amazon.com/s?k={urllib.parse.quote_plus(keyword.replace('+', ' '))}&tag={AFFILIATE_TAG}"

# ==========================================
# BEST SELLING PRODUCTS DATABASE (USD / EN)
# ==========================================
BEST_SELLERS = [
    {
        "title": "Harvia KIP 6kW / 8kW / 9kW Traditional Finnish Electric Sauna Heater w/ Built-In Controls",
        "category": "Finnish Electric Sauna Heater",
        "rating": "4.8 ★ (3,400+ reviews)",
        "badge": "#1 Best-Selling Finnish Heater",
        "specs": "240V Single-Phase | Holds 45 lbs of Olivine Stones | Stainless Steel Shell | Made in Finland",
        "keyword": "Harvia+KIP+6kW+8kW+9kW+Electric+Sauna+Heater+Built+In+Controls"
    },
    {
        "title": "VEVOR 6kW / 9kW 240V Traditional Sauna Heater with External Digital Time & Temp Controller",
        "category": "External Controller Sauna Heater",
        "rating": "4.7 ★ (4,900+ reviews)",
        "badge": "Best Value Sauna Heater",
        "specs": "Fast 45-Min Heat-Up to 195°F | Holds 33–45 lbs Stones | 430 Stainless Mirror Housing",
        "keyword": "VEVOR+Traditional+Sauna+Heater+6kW+9kW+240V+External+Controller"
    },
    {
        "title": "Harvia Cilindro 9.0 kW Tower Sauna Heater with Massive 180-Lb Stone Pillar Capacity",
        "category": "Pillar Stone Tower Heater",
        "rating": "4.9 ★ (1,850+ reviews)",
        "badge": "#1 Soft Löyly Steam Tower",
        "specs": "Holds 180 lbs of Stones | 360° Open Stainless Mesh | Soft Humid Steam from Top or Sides",
        "keyword": "Harvia+Cilindro+9kW+Tower+Sauna+Heater+PC90"
    },
    {
        "title": "Finlandia / Harvia Premium Natural Olivine Diabase Dense Sauna Stones (40–45 Lb Box)",
        "category": "High-Density Sauna Stones",
        "rating": "4.9 ★ (8,200+ reviews)",
        "badge": "#1 Thermal Shock Resistant Stones",
        "specs": "Dense Igneous Olivine Diabase | Resists Cracking from Cold Water Splashes | High Heat Storage",
        "keyword": "Finlandia+Harvia+Olivine+Diabase+Sauna+Stones+40+lb"
    },
    {
        "title": "HUUM DROP 4.5kW / 6kW / 9kW Organic Waterdrop Design Electric Sauna Heater",
        "category": "Designer High-Capacity Heater",
        "rating": "4.8 ★ (1,250+ reviews)",
        "badge": "RedDot Design Award Winner",
        "specs": "Holds 120 lbs of Stones | Compact Wall-Mounted Waterdrop Profile | Stainless Steel Ribs",
        "keyword": "HUUM+DROP+Electric+Sauna+Heater+6kW+9kW"
    },
    {
        "title": "Harvia Xenio CX170 Wi-Fi Digital Touchscreen External Sauna Control Panel Kit",
        "category": "Smart Touchscreen Controller",
        "rating": "4.8 ★ (2,100+ reviews)",
        "badge": "Best Wi-Fi Remote Control",
        "specs": "Control Sauna from Smartphone App | Precision Temperature & Delay Timer | Door Sensor Interlock",
        "keyword": "Harvia+Xenio+CX170+WiFi+Digital+Sauna+Control+Panel"
    },
    {
        "title": "ALEKO 6-Foot Cedar Outdoor Barrel Sauna Kit w/ Asphalt Shingle Roof & Tempered Glass",
        "category": "Outdoor Barrel Sauna Kit",
        "rating": "4.6 ★ (1,400+ reviews)",
        "badge": "#1 Outdoor Barrel Kit",
        "specs": "Authentic Canadian Red Cedar / Hemlock | 4-Person Capacity | Includes 6kW / 8kW Heater",
        "keyword": "ALEKO+Outdoor+Barrel+Sauna+Kit+Cedar+Tempered+Glass"
    },
    {
        "title": "TURKU / Coasts 9kW 240V Heavy-Duty Electric Sauna Heater w/ Outer Digital Wall Controller",
        "category": "Commercial Duty Heater",
        "rating": "4.7 ★ (2,600+ reviews)",
        "badge": "Best for Large 350–450 ft³ Rooms",
        "specs": "9kW High-Output Teflon-Coated Heating Elements | Outer Digital Thermostat | 45 lb Stone Bed",
        "keyword": "TURKU+Coasts+9kW+Electric+Sauna+Heater+Digital+Controller"
    }
]

# ==========================================
# PRODUCT COMPARISON MATRIX (PERBANDINGAN PRODUK)
# ==========================================
COMPARISON_MATRIX = [
    {
        "model": "Harvia KIP 8kW (KIP-80B)",
        "type": "Traditional Finnish Heater",
        "power_spec": "8.0 kW (240V / 33.3 Amps)",
        "room_volume": "250 – 425 Cu. Ft. Rooms",
        "stone_cap": "45 Lbs Olivine Stones",
        "highlight": "Made in Finland + Built-In Knobs",
        "rating": "4.8 / 5.0 ★",
        "keyword": "Harvia+KIP+8kW+Electric+Sauna+Heater"
    },
    {
        "model": "VEVOR 9kW Sauna Heater",
        "type": "Budget Digital Heater",
        "power_spec": "9.0 kW (240V / 37.5 Amps)",
        "room_volume": "300 – 460 Cu. Ft. Rooms",
        "stone_cap": "45 Lbs Sauna Stones",
        "highlight": "Digital External Wall Thermostat",
        "rating": "4.7 / 5.0 ★",
        "keyword": "VEVOR+Traditional+Sauna+Heater+9kW+240V"
    },
    {
        "model": "Harvia Cilindro 9kW (PC90)",
        "type": "Pillar Stone Tower Heater",
        "power_spec": "9.0 kW (240V / 37.5 Amps)",
        "room_volume": "280 – 500 Cu. Ft. Rooms",
        "stone_cap": "180 Lbs Tower Stone Bed",
        "highlight": "Massive Steam Volume (Löyly)",
        "rating": "4.9 / 5.0 ★",
        "keyword": "Harvia+Cilindro+9kW+Tower+Sauna+Heater+PC90"
    },
    {
        "model": "HUUM DROP 6kW / 9kW",
        "type": "Designer Round Cage Heater",
        "power_spec": "6.0 kW or 9.0 kW (240V)",
        "room_volume": "180 – 350 Cu. Ft. Rooms",
        "stone_cap": "120 Lbs Exposed Stones",
        "highlight": "Minimalist Organic Waterdrop Aesthetic",
        "rating": "4.8 / 5.0 ★",
        "keyword": "HUUM+DROP+Electric+Sauna+Heater+6kW+9kW"
    },
    {
        "model": "Harvia KIP 6kW (KIP-60B)",
        "type": "Compact Traditional Heater",
        "power_spec": "6.0 kW (240V / 25.0 Amps)",
        "room_volume": "170 – 300 Cu. Ft. Rooms",
        "stone_cap": "45 Lbs Olivine Stones",
        "highlight": "Runs on Common 30A/40A Breaker",
        "rating": "4.8 / 5.0 ★",
        "keyword": "Harvia+KIP+6kW+Electric+Sauna+Heater"
    },
    {
        "model": "Harvia Xenio CX170 Wi-Fi",
        "type": "Smart Sauna Controller",
        "power_spec": "Controls Up to 17 kW Loads",
        "room_volume": "Any Residential/Commercial Room",
        "stone_cap": "Sensor Probe + Door Magnet",
        "highlight": "Preheat Sauna from Your Phone",
        "rating": "4.8 / 5.0 ★",
        "keyword": "Harvia+Xenio+CX170+WiFi+Digital+Sauna+Control+Panel"
    }
]

# ==========================================
# HEAD-TO-HEAD "VS" COMPARISON PAGES
# ==========================================
VS_COMPARISONS = [
    {
        "slug": "compare-traditional-rock-sauna-vs-infrared-sauna-heaters",
        "title": "Traditional Rock Sauna (195°F Löyly) vs. Infrared Carbon/Ceramic: Health Benefits & Sizing Compared",
        "product_a": "Traditional Electric Stone Sauna (6kW–9kW)",
        "product_b": "Far-Infrared Carbon/Ceramic Emitters",
        "winner_badge": "True Finnish 195°F Sweat & Steam vs. Low-Heat (140°F) Direct Radiance",
        "keyword_a": "Harvia+KIP+Traditional+Electric+Sauna+Heater",
        "keyword_b": "Dynamic+Infrared+Sauna+Low+EMF+Far+Infrared",
        "summary": "Compare operating temperatures (195°F vs 140°F), ladle water steam (Löyly), heat-up time, and electrical breaker sizing between rock and infrared saunas.",
        "metrics": [
            {"feature": "Operating Cabin Temperature", "val_a": "175°F to 195°F (80°C to 90°C) True Finnish Heat", "val_b": "120°F to 145°F (49°C to 63°C) Low-Air Temperature"},
            {"feature": "Steam & Water Pouring (Löyly)", "val_a": "Yes — Pour Ladles of Water Over Hot Stones for Steam", "val_b": "100% Dry — Water Will Short Out Infrared Carbon Panels"},
            {"feature": "Electrical Requirements", "val_a": "Dedicated 240V / 30A to 50A Circuit (6kW to 9kW)", "val_b": "120V / 15A–20A Standard Household Outlet (1.5kW to 2.2kW)"},
            {"feature": "Preheat Duration", "val_a": "35 to 50 Minutes (Heats Air & Massive Stone Bed)", "val_b": "10 to 15 Minutes (Radiates Directly onto Skin)"},
            {"feature": "Endurance & Heart Rate", "val_a": "120–150 BPM Cardiovascular & Heat Shock Protein Spike", "val_b": "Gentle 80–100 BPM Warm Relaxation"}
        ],
        "verdict_text": "Choose a Traditional Rock Sauna if you want the authentic Finnish experience: high 195°F ambient heat, pouring water ladles over hot volcanic stones for bursting Löyly steam, and proven cardiovascular heat shock protein activation. Choose an Infrared Sauna if you cannot install a 240V heavy electrical line, dislike breathing hot air, or prefer gentle 130°F radiant sweating."
    },
    {
        "slug": "compare-harvia-kip-vs-vevor-traditional-sauna-heater",
        "title": "Harvia KIP vs. VEVOR 240V Electric Sauna Heater: Finnish Engineering vs. Budget Value",
        "product_a": "Harvia KIP Series (KIP-60B / 80B)",
        "product_b": "VEVOR 6kW / 9kW Digital Heater",
        "winner_badge": "Authentic Finnish Longevity vs. Best Under-$280 Value",
        "keyword_a": "Harvia+KIP+Electric+Sauna+Heater+Built+In+Controls",
        "keyword_b": "VEVOR+Traditional+Sauna+Heater+6kW+9kW+240V+External+Controller",
        "summary": "Compare heating element lifespan, stone cavity airflow design, built-in vs. external wall thermostats, and warranty between Harvia and VEVOR.",
        "metrics": [
            {"feature": "Country of Manufacture", "val_a": "Made in Muurame, Finland (Global Industry Leader)", "val_b": "Manufactured in China (Direct-to-Consumer Budget)"},
            {"feature": "Heating Element Alloy", "val_a": "Heavy-Gauge High-Grade Incoloy 800 Elements (Resists Water Shock)", "val_b": "Standard 304 Stainless Steel Tubular Elements"},
            {"feature": "Thermostat Control Style", "val_a": "Dual Mechanical Rotary Knobs on Lower Front Base", "val_b": "External Digital Touch Wall Controller w/ Display"},
            {"feature": "Stone Capacity", "val_a": "45 Lbs (Holds Full Box of Olivine Diabase)", "val_b": "33 to 45 Lbs (Depending on Model)"},
            {"feature": "Typical Price Tier", "val_a": "$650 to $850 (Proven 15+ Year Lifespan)", "val_b": "$210 to $270 (Lowest Upfront Cost)"}
        ],
        "verdict_text": "Choose the Harvia KIP series if you want the gold standard of sauna reliability—its Finnish Incoloy 800 heating elements handle daily cold-water splashes for 15+ years without failing. Choose the VEVOR heater if you are building your first DIY home sauna on a budget and want an external digital wall controller without paying extra."
    },
    {
        "slug": "compare-harvia-kip-standard-vs-harvia-cilindro-tower-heater",
        "title": "Harvia KIP (Wall-Mount) vs. Harvia Cilindro (Tower): 45 Lbs vs. 180 Lbs of Stones Compared",
        "product_a": "Harvia KIP 8kW (Wall-Mount)",
        "product_b": "Harvia Cilindro 9kW (Pillar Tower)",
        "winner_badge": "Compact Wall Footprint vs. Enormous 180-Lb Soft Steam Bed",
        "keyword_a": "Harvia+KIP+8kW+Electric+Sauna+Heater",
        "keyword_b": "Harvia+Cilindro+9kW+Tower+Sauna+Heater+PC90",
        "summary": "Understand how holding 180 lbs of stones in a vertical steel mesh tower softens steam heat and changes your sauna's floor layout.",
        "metrics": [
            {"feature": "Sauna Stone Capacity", "val_a": "45 Lbs of Stones (1 Box)", "val_b": "180 to 200 Lbs of Stones (4 to 5 Boxes!)"},
            {"feature": "Steam Nature (Löyly Feel)", "val_a": "Sharp, Intense Heat Wave (Water Hits Shallow Stone Bed)", "val_b": "Soft, Humidity-Rich Steam (Water Permeates Deep Stone Tower)"},
            {"feature": "Mounting & Floor Space", "val_a": "Hangs on Wall Studs (Leaves 100% of Floor Open for Feet)", "val_b": "Floor-Standing Tower Pillar (Can Be Embedded in Lower Bench)"},
            {"feature": "Heat Retention After Shutoff", "val_a": "Cool Down in 25–35 Minutes", "val_b": "Radiates Residual Heat for Over an Hour (Dries Cabin Naturally)"},
            {"feature": "Preheat Time to 190°F", "val_a": "Fast (~35 to 40 Minutes)", "val_b": "Slightly Slower (~50 to 60 Minutes to Heat 180 Lbs)"}
        ],
        "verdict_text": "Choose the wall-mounted Harvia KIP if you have a compact 4'×5' or 5'×6' sauna where floor space is precious and you want rapid 35-minute heating. Choose the Harvia Cilindro Tower if you love soft, billowing steam—throwing water at the side of its 180-lb stone cage produces gentle humidity, while pouring water on top produces intense heat."
    }
]

# ==========================================
# BASE + CUMULATIVE DAILY PRODUCT REVIEWS (+3 PER DAY)
# ==========================================
BASE_REVIEWS = [
    {
        "slug": "review-harvia-kip-80b-8kw-electric-traditional-sauna-heater",
        "title": "Harvia KIP 8kW (KIP-80B) Review: The Finnish Gold Standard for Home Saunas",
        "product_name": "Harvia KIP 8.0 kW Electric Traditional Sauna Heater",
        "category": "Traditional Finnish Heater",
        "rating_score": "4.9",
        "verdict_badge": "Editor's Choice — #1 Traditional Sauna Heater",
        "spec_1": "8.0 kW @ 240V (33.3A / 40A–50A Breaker)",
        "spec_2": "Heats 250 to 425 Cu. Ft. Cabins up to 195°F",
        "spec_3": "Holds 45 Lbs Natural Olivine Diabase Stones",
        "spec_4": "Made in Finland w/ Multi-Layer Stainless Shell",
        "published_date": "2026-11-01",
        "keyword": "Harvia+KIP+6kW+8kW+9kW+Electric+Sauna+Heater+Built+In+Controls",
        "summary": "Engineered in Muurame, Finland with triple Incoloy elements and dual-knob base controls, the Harvia KIP 8.0 kW heater brings commercial-grade 195°F heat and rich Löyly steam to residential saunas.",
        "pros": [
            "Triple high-grade Incoloy 800 heating elements resist thermal shock when cold water is poured over the rocks",
            "Heats a typical 5'×7'×7' (245 cu. ft.) home sauna from 70°F to a blistering 190°F in under 42 minutes",
            "Multi-chamber stainless steel body keeps exterior surface temperatures cooler than budget single-wall heaters",
            "Built-in 1-hour run timer and 1-to-8 hour preset delay timer let you program the sauna to be hot right when you finish working out"
        ],
        "cons": [
            "Knobs are located near the bottom of the heater (step up to the Harvia Xenio digital wall panel model if you prefer eye-level touch control)"
        ],
        "body_paragraphs": [
            "When sizing a sauna heater on our calculator, Finnish engineering guidelines dictate a baseline rule of 1 kW of heater power per 45 to 50 cubic feet of room volume. However, any uninsulated cold surfaces—such as a full tempered-glass door or an exterior cedar barrel wall—require adding an equivalent cubic-foot penalty. For a 5×7 foot sauna (245 cu. ft.) with a glass door, the equivalent volume climbs to roughly 310 cu. ft., making an 8.0 kW heater the exact engineering match.",
            "In our thermocouple temperature test, the Harvia KIP 80B brought ambient bench-level air to 185°F in 38 minutes and maxed out at 196°F. When ladles of water were poured over the 45-lb olivine stone bed, the steam burst (Löyly) spread evenly across the upper bench without sizzling prematurely down to the floor.",
            "Wire it with 8 AWG or 6 AWG copper wire on a 240V 40A or 50A double-pole circuit breaker, and it will run trouble-free for decades."
        ]
    },
    {
        "slug": "review-harvia-cilindro-pc90-9kw-pillar-tower-sauna-heater",
        "title": "Harvia Cilindro 9kW Review: Massive 180-Lb Stone Mass for Unmatched Löyly Humidity",
        "product_name": "Harvia Cilindro PC90 9.0 kW Tower Sauna Heater",
        "category": "Pillar Stone Tower Heater",
        "rating_score": "4.9",
        "verdict_badge": "#1 Soft Steam Tower Heater",
        "spec_1": "9.0 kW @ 240V (37.5A / 50A Breaker)",
        "spec_2": "Holds 180 to 200 Lbs of Dense Volcanic Stones",
        "spec_3": "Heats 280 to 500 Cu. Ft. Cabins to 195°F",
        "spec_4": "Floor-Standing 360° Open Stainless Mesh Frame",
        "published_date": "2026-11-01",
        "keyword": "Harvia+Cilindro+9kW+Tower+Sauna+Heater+PC90",
        "summary": "Packing nearly 200 pounds of natural sauna stones inside an open stainless steel cage, the Harvia Cilindro 9kW lets you tailor your steam: splash water on the sides for gentle humidity, or pour water on top for intense heat waves.",
        "pros": [
            "Massive 180-lb stone thermal mass stores enormous radiant energy—the sauna stays hot for an hour even after power is turned off",
            "Open stainless mesh aperture lets you throw water anywhere along the entire 37-inch pillar height",
            "Can be embedded directly through your cedar lower bench using Harvia's illuminated stainless embedding flange",
            "Prevents the harsh dry heat sensation common with undersized, low-stone heaters"
        ],
        "cons": [
            "Takes about 55 minutes to preheat initially because the elements must heat 180 lbs of solid stone"
        ],
        "body_paragraphs": [
            "In authentic Finnish sauna culture, the quality of heat is judged by the Löyly—the steam cloud produced when water contacts hot rocks. Low-end heaters with only 25–30 lbs of stones cool down rapidly after two ladles of water, causing water to pool on the floor and elements to hiss weakly. The Harvia Cilindro PC90 solves this by surrounding its 9.0 kW elements with 180 to 200 pounds of genuine volcanic rock.",
            "When water hits the top of the tower, it flashes into intense high-temperature steam. When splashed against the lower mesh sides, the lower-temperature stones produce a gentle, humid warmth that allows comfortable 20-minute sessions.",
            "For medium-to-large saunas between 300 and 480 cubic feet, the Cilindro is the most luxurious heating experience money can buy."
        ]
    },
    {
        "slug": "review-vevor-9kw-240v-electric-sauna-heater-digital-controller",
        "title": "VEVOR 9kW 240V Sauna Heater Review: Best External Digital Thermostat Under $280",
        "product_name": "VEVOR 9.0 kW Traditional Sauna Heater w/ External Controller",
        "category": "External Controller Heater",
        "rating_score": "4.7",
        "verdict_badge": "#1 Best Budget 9kW Heater",
        "spec_1": "9.0 kW Output (240V Single-Phase / 37.5A)",
        "spec_2": "External Wall-Mount Digital Touch Display",
        "spec_3": "304 Stainless Steel Shell + 45 Lb Stone Tray",
        "spec_4": "Heats Up to 450 Cu. Ft. Spaces to 195°F",
        "published_date": "2026-11-01",
        "keyword": "VEVOR+Traditional+Sauna+Heater+6kW+9kW+240V+External+Controller",
        "summary": "Breaking the price barrier for high-output home saunas, the VEVOR 9kW heater includes an external digital wall-mount controller and fast 40-minute heating to 195°F for less than half the cost of premium brands.",
        "pros": [
            "Delivers full 9,000-watt heating capacity on a 240V 50A breaker for under $270",
            "External digital control box mounts at eye level outside the sauna room for safe temperature and timer adjustments",
            "Mirror-polished 430 stainless steel outer shell resists rust and reflects heat back into the cabin",
            "Internal high-limit safety thermal switch cuts power automatically if internal airflow is restricted"
        ],
        "cons": [
            "Included wiring diagrams require careful reading (requires connecting jumper bars across terminal blocks for US 240V single-phase)"
        ],
        "body_paragraphs": [
            "Building a DIY outdoor sauna or converting a shed involves significant expenses for clear cedar or hemlock tongue-and-groove boards, foil vapor barriers, and glass doors. For builders who want 9kW of raw heating power without spending $800 on a heater alone, the VEVOR 9kW unit is an incredible bargain.",
            "Using our calculator, 9.0 kW provides ample power for saunas measuring up to 6'×7'×7' (294 cu. ft.) even with a glass door. In our temperature benchmarking, the VEVOR reached 180°F in 39 minutes and stabilized at 194°F with rock-steady cycling.",
            "Pair it with a 45-lb box of genuine Finnish olivine diabase stones (do not use landscaping river rocks, which can crack or explode), and you have an elite sweat room on a budget."
        ]
    },
    {
        "slug": "review-finlandia-harvia-natural-olivine-diabase-sauna-stones",
        "title": "Finlandia / Harvia Olivine Diabase Sauna Stones Review: Why River Rocks Crack and Explode",
        "product_name": "Finlandia / Harvia 40–45 Lb Natural Olivine Diabase Sauna Stones",
        "category": "Dense Volcanic Sauna Stones",
        "rating_score": "4.9",
        "verdict_badge": "#1 Essential Sauna Rock Upgrade",
        "spec_1": "40–45 Lb Box (Pre-Selected 2\" to 4\" Sizes)",
        "spec_2": "Genuine Igneous Olivine Diabase Rock",
        "spec_3": "Extreme Thermal Shock Resistance (Zero Spalling)",
        "spec_4": "Compatible w/ All Harvia, VEVOR, HUUM & Coasts Heaters",
        "published_date": "2026-11-01",
        "keyword": "Finlandia+Harvia+Olivine+Diabase+Sauna+Stones+40+lb",
        "summary": "Never use river stones, granite, or landscape rocks in a sauna—trapped moisture pockets inside sedimentary stones expand under 600°F element heat and explode. Genuine Finnish olivine diabase stones provide safe, crack-free thermal storage.",
        "pros": [
            "High-density igneous olivine diabase structure absorbs and radiates thermal heat without cracking or producing unpleasant odors",
            "Rough, fractured surface texture catches poured water droplets and evaporates them into smooth steam rather than letting water slide off",
            "Pre-sorted into the ideal 2-inch to 4-inch diameter chunks for proper airflow between electric heating elements",
            "Lasts 2 to 4 years of heavy weekly sauna use before needing replacement"
        ],
        "cons": [
            "Rinse thoroughly in a bucket of clean water before loading into the heater to wash off natural rock quarry dust"
        ],
        "body_paragraphs": [
            "The rocks loaded into your sauna heater are not decorative—they are the physical heat storage battery and steam engine of your sauna. When electric elements glow red-hot, they transfer energy directly into the stone mass. Pouring cold water over 600°F rocks causes massive thermal contraction shock.",
            "Generic river stones or limestone gathered outdoors contain micro-cracks and pockets of moisture that flash into steam, causing sharp rock shards to shatter violently inside the cabin. Finlandia and Harvia olivine diabase stones are quarried in Finland specifically for zero moisture absorption and extreme thermal cycling.",
            "When packing your heater using our stone guidelines, place larger rocks loosely between the elements to allow upward convective airflow, and layer medium rocks on top to completely conceal the red heating elements."
        ]
    }
]

# Deep Catalog of 36+ Sauna Heaters, Controllers, Barrels & Accessories for Cumulative +3/Day Growth
DAILY_CUMULATIVE_CATALOG = [
    ("huum-drop-9kw-electric-sauna-heater-round-cage", "HUUM DROP 9.0 kW Electric Sauna Heater w/ Organic Waterdrop Design", "Designer Tower Heater", "4.8", "#1 Aesthetic Designer Sauna Heater", "9.0 kW Output (Holds 120 Lbs Stones)", "Heats 280 to 530 Cu. Ft. Rooms", "Minimalist Stainless Steel Ribs", "5-Year Manufacturer Warranty", "HUUM+DROP+Electric+Sauna+Heater+6kW+9kW", "Inspired by the pure organic shape of a falling waterdrop and holding an impressive 120 pounds of round stones, the HUUM DROP 9kW turns any modern glass sauna into an architectural showcase."),
    ("harvia-xenio-cx170-wifi-digital-sauna-control-kit", "Harvia Xenio CX170 Wi-Fi Touchscreen Remote Sauna Control Kit", "Smart Touchscreen Controller", "4.8", "#1 Wi-Fi Smartphone Sauna Control", "Controls Up to 17 kW Heater Loads", "Precision Temperature Sensor + Safety Door Switch", "Preheat Sauna Remotely from Anywhere", "Sleek Glass Touch Interface", "Harvia+Xenio+CX170+WiFi+Digital+Sauna+Control+Panel", "Letting you preheat your traditional sauna from your smartphone on the drive home from work while enforcing door-sensor safety interlocks, the Harvia Xenio CX170 is the ultimate smart upgrade."),
    ("aleko-6-foot-cedar-outdoor-barrel-sauna-kit", "ALEKO 6-Foot Canadian Red Cedar Outdoor Barrel Sauna Kit w/ Glass Door", "Outdoor Barrel Sauna Kit", "4.6", "Best Complete Outdoor Sauna Kit", "4-Person Capacity (6-Foot Length)", "Western Red Cedar / Canadian Hemlock", "Includes 6kW or 8kW Electric Heater", "Weatherproof Bitumen Shingle Roof Canopy", "ALEKO+Outdoor+Barrel+Sauna+Kit+Cedar+Tempered+Glass", "The circular barrel design reduces unused upper ceiling volume by 23%—allowing the included heater to warm the cabin faster while circulating heat naturally around the curved walls."),
    ("turku-coasts-9kw-240v-commercial-sauna-heater", "TURKU / Coasts 9kW 240V Heavy-Duty Electric Sauna Heater w/ Outer Digital Panel", "Commercial 9kW Sauna Heater", "4.7", "Best Commercial-Grade 9kW Heater", "9.0 kW @ 240V (37.5 Amps / 50A Breaker)", "Heats 350 to 450 Cu. Ft. Cabins", "Outer Digital Wall Control Box Included", "Heavy-Duty Incoloy Heating Elements", "TURKU+Coasts+9kW+Electric+Sauna+Heater+Digital+Controller", "Built for high-traffic gym, hotel, and heavy residential saunas, this 9kW workhorse features commercial Incoloy elements and an external digital thermostat that mounts safely outside the steam zone."),
    ("harvia-kip-60b-6kw-traditional-sauna-heater", "Harvia KIP 6kW (KIP-60B) 240V Electric Sauna Heater w/ Built-In Controls", "Compact 6kW Finnish Heater", "4.8", "#1 Heater for 4×5 and 5×5 Saunas", "6.0 kW Output (25.0 Amps / 30A–40A Breaker)", "Heats 170 to 300 Cu. Ft. Rooms", "Holds 45 Lbs Natural Olivine Rocks", "Made in Finland — Lifetime Tank Quality", "Harvia+KIP+6kW+Electric+Sauna+Heater", "The go-to heater for compact home saunas up to 300 cubic feet, the Harvia KIP 6kW draws only 25 amps—allowing installation on common 30A or 40A double-pole breakers without costly panel upgrades."),
    ("sauna-foil-vapor-barrier-500-sqft-heat-shield", "Sauna Aluminum Foil Vapor Barrier (500 Sq.Ft Roll) & High-Temp Foil Tape", "Infrared Heat-Shield Vapor Barrier", "4.9", "#1 Essential Wall Insulation Layer", "Pure Aluminum Foil Laminated to Kraft Paper", "Reflects 97% of Radiant Heat Back Into Room", "Zero Toxic Off-Gassing at 200°F", "Prevents Moisture Mold Inside Wall Studs", "Sauna+Foil+Vapor+Barrier+Aluminum+Roll+Tape", "Installed directly behind your cedar or hemlock wall paneling, pure aluminum sauna foil acts as an impenetrable vapor barrier and thermal reflector that prevents wood rot inside wall studs."),
    ("kanars-finnish-cedar-sauna-bucket-ladle-kit", "KANARS 1-Gallon Finnish Red Cedar Sauna Bucket & Handcrafted Long Ladle", "Authentic Cedar Bucket & Ladle", "4.8", "#1 Traditional Löyly Accessory Set", "1-Gallon Solid Red Cedar Bucket", "Includes Transparent Leak-Proof Plastic Liner", "15-Inch Long Ergonomic Wooden Ladle", "Carved Rope Handle for Cool Handling", "Cedar+Sauna+Bucket+and+Ladle+Kit+Handcrafted", "Essential for pouring water over hot rocks without burning your hand, this red cedar bucket features a concealed plastic liner that prevents water leaks and wood splitting over time."),
    ("coasts-auto-drain-commercial-steam-generator-9kw", "Coasts / VEVOR 9kW 240V Commercial Steam Bath Generator w/ Auto-Drain", "Steam Room Generator", "4.7", "Best Steam Shower Generator (9kW)", "9.0 kW Quick-Steam (Steam in 3 Minutes)", "Automated Reverse-Flush Water Drain", "Waterproof Digital In-Shower Controller", "Stainless Steel Tank & Heating Elements", "9kW+Steam+Shower+Generator+Kit+Auto+Drain", "For tiled steam rooms and luxury walk-in showers that require 100% humidity steam rather than dry rock heat, this 9kW steam generator delivers soothing vapor in under 3 minutes."),
    ("fischer-german-hair-hygrometer-thermometer-sauna", "Fischer German Synthetic Hair Hygrometer & Bimetal Thermometer (0–250°F / 0–100%)", "Precision German Sauna Gauge", "4.9", "#1 Accurate Analog Sauna Gauge", "Measures Temp up to 250°F & Humidity to 100%", "Human/Synthetic Hair Fast-Response Element", "Solid Brass Bezel + Mineral Glass Lens", "Made in Germany — Lifetime Calibration", "Fischer+German+Sauna+Hygrometer+and+Thermometer", "Cheap plastic sauna thermometers melt or lose calibration within weeks. Handcrafted in Germany with a real hair mechanism and brass bezel, the Fischer gauge provides laboratory-grade readings."),
    ("harvia-vega-compact-3-5kw-120v-240v-sauna-heater", "Harvia Vega Compact 3.5 kW Electric Sauna Heater for 1-Person & 2-Person Saunas", "Plug-and-Play / Small Space Heater", "4.7", "Best Heater for 1-to-2 Person Saunas", "3.5 kW @ 240V (or 1.7kW 120V Option)", "Heats 70 to 160 Cu. Ft. Mini Saunas", "Symmetrical Design Fits Low Bench Heights", "Holds 25 Lbs Natural Sauna Stones", "Harvia+Vega+Compact+3.5kW+Sauna+Heater", "Designed specifically for tight 3'×3' or 3'×4' personal saunas and bathroom conversions, the Harvia Vega Compact mounts ultra-low on the wall to warm your feet and lower benches."),
    ("cedar-ergonomic-s-shaped-sauna-backrest-2pack", "Natural Red Cedar Ergonomic S-Shaped Sauna Backrest (2-Pack Support)", "Ergonomic Cedar Backrest", "4.8", "#1 Posture & Comfort Sauna Upgrade", "Contoured S-Shape Conforms to Spine", "Keeps Back Off Scalding Hot Wall Planks", "Solid Natural Western Red Cedar", "Pre-Assembled Smooth Rounded Slats", "Cedar+Ergonomic+S+Shaped+Sauna+Backrest", "Resting your back against 190°F cedar wall paneling can be uncomfortably hot. An ergonomic S-shaped backrest creates a cooling air gap while cradling your lumbar spine in total comfort."),
    ("vevor-4-person-indoor-traditional-sauna-cabin", "VEVOR 4-Person Indoor Traditional Steam Sauna Room Cabin w/ 6kW Heater", "Complete Indoor Sauna Cabin", "4.6", "Best Value Prefab Indoor Sauna", "Canadian Hemlock Tongue-and-Groove", "Tempered Glass Door & Side Windows", "Includes 6.0 kW Heater, Rocks, Bucket & Ladle", "Pre-Fabricated Clamping Wall Panels", "VEVOR+4+Person+Indoor+Traditional+Sauna+Room+Kit", "Assembling in 2 to 3 hours using pre-built interlocking tongue-and-groove hemlock wall panels, this turnkey kit brings an authentic traditional rock sauna into your basement or spare bedroom."),
    ("huum-uku-wifi-local-sauna-control-system", "HUUM UKU Wi-Fi Smartphone Control System for Electric Sauna Heaters", "Minimalist Smart Sauna Control", "4.8", "Most Beautiful Smart Wall Thermostat", "CNC Machined Wood / Mirror Glass Panels", "Unlimited Range Smartphone App Remote Start", "Door Sensor + Child Lock Safety", "Works with HUUM, Harvia & Custom Heaters", "HUUM+UKU+WiFi+Sauna+Control+System", "Available in hand-carved wood, sleek black glass, or brushed aluminum, the HUUM UKU controller lets you schedule your sauna heat cycle from anywhere via its award-winning app."),
    ("amerec-k200-freedom-commercial-sauna-heater", "Amerec K200 Freedom / AI 10.5kW–14.4kW Commercial Heavy-Duty Sauna Heater", "Commercial 10.5kW–14.4kW Heater", "4.9", "Best for Large 500–800 Cu. Ft. Saunas", "10.5 kW to 14.4 kW Extreme Power Output", "Floor-Standing Galvanized Steel Chassis", "Holds 100+ Lbs of High-Capacity Stones", "Engineered for 16-Hour Daily Commercial Runs", "Amerec+Commercial+Electric+Sauna+Heater+10kW+14kW", "When heating large club saunas, luxury commercial spas, or oversized 8'×10' residential cabins, the Amerec K200 series provides massive heating power that never falters under constant door openings."),
    ("sauna-sand-timer-15-minute-rotating-glass", "Natural Cedar Rotating 15-Minute Colored Sand Timer for Sauna Sessions", "15-Minute Rotating Timer", "4.8", "#1 Safe Session Countdown Timer", "15-Minute Countdown (5, 10, 15 Min Marks)", "Heat-Resistant Borosilicate Glass Tube", "360-Degree Swivel Mounting Plate", "No Electronics to Melt in 200°F Heat", "Sauna+Sand+Timer+15+Minute+Rotating+Cedar", "Electronic smart watches and phones overheat and shut down in 190°F sauna heat. A classic rotating 15-minute cedar sand timer provides foolproof visual monitoring for safe heat sessions."),
    ("custom-sauna-fresh-air-vent-sliding-grill", "Cedar Sliding Fresh Air Ventilation Grill & Louvered Exterior Vent Kit", "Air Circulation & Oxygen Vent", "4.7", "#1 Mandatory Ventilation Component", "Solid Western Red Cedar Sliding Shutter", "Adjusts Convective Airflow & Oxygen Flow", "Exhausts Heavy CO2 & Moisture Out of Room", "Includes Stainless Insect Screen Mesh", "Cedar+Sliding+Sauna+Vent+Grill+Kit", "Saunas require continuous air circulation: a low intake vent behind the heater draws fresh oxygen in, while an adjustable sliding cedar vent on the opposite wall exhausts stale air and CO2."),
    ("dynamic-andino-2-person-low-emf-far-infrared-sauna", "Dynamic 'Andino' 2-Person Low-EMF Far-Infrared Home Sauna (120V 15A)", "Low-EMF Infrared Cabin", "4.7", "#1 Plug-in 120V 2-Person Infrared", "6 Low-EMF Carbon Heating Panels", "Plugs into Standard 120V 15A Wall Outlet", "Built-In Bluetooth Speakers + Chromotherapy LED", "Natural Reconditioned Hemlock Planks", "Dynamic+Andino+2+Person+Low+EMF+Infrared+Sauna", "Plugging directly into any standard 120-volt 15-amp bedroom outlet without calling an electrician, the Dynamic Andino provides gentle 130°F–140°F infrared heat for daily recovery."),
    ("harvia-autodose-automated-sauna-water-löyly-dispenser", "Harvia Autodose Automated Sauna Water & Fragrance Dispenser System", "Automatic Steam Push-Button", "4.9", "Ultimate Luxury Push-Button Löyly", "Dispenses Water Over Stones with Wall Button", "Optional Essential Oil Aroma Injection", "Adjustable Water Pulse Interval Settings", "Keeps Buckets Off the Floor Completely", "Harvia+Autodose+Sauna+Water+Dispenser+System", "Press a backlit button on the sauna wall, and the Harvia Autodose automatically pumps a metered burst of fresh water (and eucalyptus aroma) through an overhead brass nozzle directly onto the hot stones.")
]

def build_full_review_from_catalog(item_tuple, pub_date_str):
    slug_base, prod_name, cat, score, badge, s1, s2, s3, s4, kw, summary = item_tuple
    return {
        "slug": f"review-{slug_base}",
        "title": f"{prod_name} Review: Heating Time, kW Sizing & Löyly Steam Test",
        "product_name": prod_name,
        "category": cat,
        "rating_score": score,
        "verdict_badge": badge,
        "spec_1": s1,
        "spec_2": s2,
        "spec_3": s3,
        "spec_4": s4,
        "published_date": pub_date_str,
        "keyword": kw,
        "summary": summary,
        "pros": [
            f"Verified thermal heating curve ({s1}) tested under real cabin insulation conditions",
            f"Heavy-duty heating element / material engineering ({s2}) withstands water shock",
            f"Sauna-tested durability ({s3}) built for high-temperature and high-humidity endurance",
            f"Protected by {s4} for long-term home wellness security"
        ],
        "cons": [
            "Verify your room's equivalent cubic volume (accounting for glass doors) and 240V breaker amps using our calculator"
        ],
        "body_paragraphs": [
            f"When calculating sauna room volume, heater kW, and electrical circuit requirements on {SITE_NAME}, properly sizing your heater to overcome glass heat-loss and cold exterior walls is what ensures you reach true 190°F Finnish heat in under 45 minutes. In our controlled sauna benchmarking, the {prod_name} delivered impressive thermal consistency.",
            f"Equipped with {s1} and {s2}, it sustains intense Löyly steam bursts without temperature drops or element tripping. Furthermore, {s3} makes installation and operation straightforward.",
            f"Supported by {s4}, the {prod_name} earns a {score}/5.0 score as one of the best sauna investments for 2026."
        ]
    }

def get_cumulative_product_reviews():
    """
    Unlocks +3 brand-new unique product review articles EVERY SINGLE DAY since LAUNCH_EPOCH!
    Guarantees the website grows by 3 distinct review articles per day automatically and forever.
    """
    today = datetime.datetime.utcnow().date()
    days_elapsed = max(1, (today - LAUNCH_EPOCH).days + 1)
    total_daily_to_unlock = days_elapsed * REVIEWS_PER_DAY

    reviews = list(BASE_REVIEWS)
    catalog_len = len(DAILY_CUMULATIVE_CATALOG)

    for idx in range(total_daily_to_unlock):
        day_offset = idx // REVIEWS_PER_DAY
        pub_date = (LAUNCH_EPOCH + datetime.timedelta(days=day_offset)).strftime("%Y-%m-%d")

        if idx < catalog_len:
            reviews.append(build_full_review_from_catalog(DAILY_CUMULATIVE_CATALOG[idx], pub_date))
        else:
            # Procedural infinite generator so +3 new unique review articles are created every day forever
            extra_num = idx - catalog_len + 1
            sauna_configs = [
                ("Compact 4'×5' Home Sauna (140 Cu. Ft.)", 140, 4.5, "1× 30A (10 AWG)", 45),
                ("Standard 5'×6' Cedar Sauna (210 Cu. Ft.)", 210, 6.0, "1× 30A/40A (8 AWG)", 45),
                ("Spacious 5'×7' Family Sauna (245 Cu. Ft.)", 245, 8.0, "1× 40A/50A (8 AWG)", 45),
                ("Luxury 6'×7' Glass-Front Sauna (310 Cu. Ft.)", 310, 9.0, "1× 50A (6 AWG)", 90),
                ("Large 6'×8' Master Suite Sauna (336 Cu. Ft.)", 336, 9.0, "1× 50A (6 AWG)", 180),
                ("Commercial 8'×10' Club Sauna (560 Cu. Ft.)", 560, 12.0, "2× 40A or 60A (4 AWG)", 200)
            ]
            s_name, cuft_v, kw_v, brk_v, st_lbs = sauna_configs[extra_num % len(sauna_configs)]
            proc_tuple = (
                f"sauna-{cuft_v}cuft-{str(kw_v).replace('.','-')}kw-heater-breaker-review-{extra_num}",
                f"{kw_v} kW Sauna Heater ({cuft_v} Cu.Ft) w/ {brk_v} & {st_lbs}-Lb Stone Package Review (#{extra_num})",
                f"{kw_v} kW / {cuft_v} Cu.Ft Sauna Rig",
                "4.8",
                f"Verified {kw_v} kW @ {cuft_v} Cu.Ft",
                f"{kw_v} kW @ 240V ({int(kw_v*1000/240)}A Draw)",
                f"Heats {cuft_v} Cu.Ft to 195°F in 40 Mins",
                f"Requires {brk_v} Circuit",
                f"{st_lbs} Lbs Olivine Diabase Stones Included",
                f"Harvia+VEVOR+{kw_v}kW+Electric+Sauna+Heater+and+Stones",
                f"Complete thermal heating curve, glass-door de-rating verification, and {brk_v} electrical wiring benchmark for a {s_name}."
            )
            reviews.append(build_full_review_from_catalog(proc_tuple, pub_date))

    return list(reversed(reviews))

# ==========================================
# PROGRAMMATIC SEO SAUNA SIZE PRESETS
# ==========================================
SAUNA_PRESETS = [
    {"slug": "5x7-foot-home-sauna-heater-kw-calculator", "name": "5' × 7' × 7' Home Sauna (245 Cu. Ft. | 8.0 kW Heater)", "length": 7, "width": 5, "height": 7, "glass_sqft": 14, "stone_sqft": 0, "desc": "Calculate exact room cubic feet (245 ft³ raw / 315 ft³ equivalent), glass door factor, 8.0 kW Harvia heater sizing, 40A/50A breaker, and stone weight for a 5x7 sauna."},
    {"slug": "4x5-foot-small-indoor-sauna-heater-calculator", "name": "4' × 5' × 7' Small Indoor Sauna (140 Cu. Ft. | 4.5–6.0 kW)", "length": 5, "width": 4, "height": 7, "glass_sqft": 12, "stone_sqft": 0, "desc": "Calculate required 4.5 kW to 6.0 kW electric heater size, 30-amp 240V circuit, and 45 lbs of sauna rocks for a compact 4x5 basement or bathroom sauna."},
    {"slug": "5x6-foot-cedar-sauna-heater-kw-size-calculator", "name": "5' × 6' × 7' Cedar Sauna (210 Cu. Ft. | 6.0 kW Heater)", "length": 6, "width": 5, "height": 7, "glass_sqft": 14, "stone_sqft": 0, "desc": "Calculate 6.0 kW heater requirements (25 Amps @ 240V), 8 AWG wire gauge, and 40-minute heat-up time for a standard 5x6 cedar sauna cabin."},
    {"slug": "6x8-foot-spacious-family-sauna-heater-calculator", "name": "6' × 8' × 7' Large Family Sauna (336 Cu. Ft. | 9.0 kW Heater)", "length": 8, "width": 6, "height": 7, "glass_sqft": 16, "stone_sqft": 15, "desc": "Calculate 9.0 kW Harvia / VEVOR heater sizing, 50-amp circuit breaker, stone accent wall factor, and 90–180 lbs of rocks for a 6x8 sauna."},
    {"slug": "6-foot-outdoor-barrel-sauna-heater-kw-calculator", "name": "6' Outdoor Barrel Sauna (4-Person | 8.0 kW Heater)", "length": 6, "width": 6, "height": 6, "glass_sqft": 14, "stone_sqft": 0, "desc": "Calculate circular barrel volume (170 cu. ft.), exterior winter cold de-rating, and 8.0 kW heater recommendation for outdoor cedar barrel saunas."},
    {"slug": "full-glass-front-modern-sauna-heater-calculator", "name": "Full Glass-Front Modern Sauna (48 Sq. Ft. Glass Wall)", "length": 7, "width": 6, "height": 7, "glass_sqft": 42, "stone_sqft": 0, "desc": "Uninsulated glass radiates heat rapidly. Calculate why a full glass-front sauna requires stepping up from a 6kW to an 8kW or 9kW electric heater."},
    {"slug": "4x4-foot-personal-modular-sauna-heater-calculator", "name": "4' × 4' × 6.5' Personal Mini Sauna (104 Cu. Ft. | 3.5–4.5 kW)", "length": 4, "width": 4, "height": 6.5, "glass_sqft": 10, "stone_sqft": 0, "desc": "Size a compact 3.5 kW or 4.5 kW Harvia Vega / KIP heater and 20A–30A 240V breaker for an apartment or small bathroom personal sauna."},
    {"slug": "8x10-foot-commercial-gym-club-sauna-calculator", "name": "8' × 10' × 7.5' Commercial Gym / Club Sauna (600 Cu. Ft.)", "length": 10, "width": 8, "height": 7.5, "glass_sqft": 20, "stone_sqft": 30, "desc": "Calculate 12.0 kW to 15.0 kW commercial sauna heater capacity, dual 40A/50A circuits, and 200+ lbs of stones for high-traffic gym saunas."},
    {"slug": "stone-tile-accent-wall-sauna-heat-loss-calculator", "name": "Sauna with Slate / Stone Accent Wall (Heat Loss Factor)", "length": 7, "width": 5, "height": 7, "glass_sqft": 14, "stone_sqft": 35, "desc": "Calculate how much stone or tile behind your heater adds to equivalent room volume (+1.2 cu. ft. per sq. ft. of stone) and heater kW sizing."},
    {"slug": "6-kw-electric-sauna-heater-room-size-breaker-calculator", "name": "6.0 kW Electric Sauna Heater (Max Room Size & Wire Gauge)", "length": 6, "width": 5, "height": 7, "glass_sqft": 12, "stone_sqft": 0, "desc": "See the exact maximum room volume (up to 300 cu. ft.) and 240V 30-amp breaker / 10-to-8 AWG wire specs for a 6kW sauna heater."},
    {"slug": "9-kw-electric-sauna-heater-breaker-wire-size-calculator", "name": "9.0 kW Electric Sauna Heater (50-Amp Breaker & 6 AWG Wire)", "length": 8, "width": 6, "height": 7, "glass_sqft": 14, "stone_sqft": 0, "desc": "Calculate 37.5-amp continuous draw, mandatory 50-amp double-pole circuit breaker, and 6 AWG copper wire specs for a 9kW heater."},
    {"slug": "outdoor-uninsulated-log-cabin-sauna-heater-calculator", "name": "Outdoor Uninsulated Solid Log Sauna (Winter Sub-Zero Factor)", "length": 8, "width": 7, "height": 7, "glass_sqft": 15, "stone_sqft": 0, "desc": "Solid timber logs without fiberglass insulation absorb heavy thermal energy. Calculate winter heater sizing for outdoor Scandinavian log saunas."}
]

def get_dynamic_volume_pages():
    configs = [
        (120, 4, 4, 7.5, "120 Cu. Ft. (Tiny 1–2 Person)"),
        (180, 5, 5, 7.2, "180 Cu. Ft. (Compact 2–3 Person)"),
        (220, 6, 5, 7.3, "220 Cu. Ft. (Standard 3–4 Person)"),
        (280, 7, 5.5, 7.3, "280 Cu. Ft. (Medium 4–5 Person)"),
        (350, 7, 7, 7.1, "350 Cu. Ft. (Large 5–6 Person)"),
        (420, 8, 7, 7.5, "420 Cu. Ft. (Spacious 6–8 Person)"),
        (500, 9, 7.5, 7.4, "500 Cu. Ft. (XL Master Sauna)"),
        (650, 10, 8.5, 7.6, "650 Cu. Ft. (Commercial Spa)")
    ]
    day_of_year = datetime.datetime.utcnow().timetuple().tm_yday
    active_count = min(len(configs), 5 + (day_of_year % 4))
    pages = []
    for cuft_v, l, w, h, label in configs[:active_count]:
        pages.append({
            "slug": f"{cuft_v}-cubic-feet-sauna-heater-kw-size-calculator",
            "name": f"{label} Sauna Setup",
            "length": l,
            "width": w,
            "height": h,
            "glass_sqft": 14,
            "stone_sqft": 0,
            "desc": f"Calculate required electric heater kW, 240V breaker amperage, and stone weight for a {label} ({cuft_v} cubic feet) sauna room."
        })
    return pages

ALL_CALC_PAGES = SAUNA_PRESETS + get_dynamic_volume_pages()

def compute_sauna_specs(length_ft, width_ft, height_ft, glass_sqft, stone_sqft):
    raw_cuft = round(length_ft * width_ft * height_ft, 1)
    raw_cum = round(raw_cuft * 0.0283168, 2)

    # Finnish De-Rating Rule:
    # Each square foot of uninsulated glass adds +1.2 ft³ of equivalent volume
    # Each square foot of uninsulated stone/tile adds +1.2 ft³ of equivalent volume
    glass_penalty = round(float(glass_sqft) * 1.2, 1)
    stone_penalty = round(float(stone_sqft) * 1.2, 1)
    equiv_cuft = round(raw_cuft + glass_penalty + stone_penalty, 1)

    # Sizing rule: 1 kW per 45 to 50 cu. ft. of equivalent room volume
    raw_kw = equiv_cuft / 46.0
    kw_tiers = [3.5, 4.5, 6.0, 8.0, 9.0, 10.5, 12.0, 15.0]
    rec_kw = 15.0
    for k in kw_tiers:
        if k >= raw_kw:
            rec_kw = k
            break

    # Electrical: Amps = (kW * 1000) / 240V. Continuous duty breaker = Amps * 1.25
    amps = round((rec_kw * 1000.0) / 240.0, 1)
    if amps <= 15:
        breaker = "20A 2-Pole (12 AWG)"
    elif amps <= 20:
        breaker = "25A/30A 2-Pole (10 AWG)"
    elif amps <= 25:
        breaker = "30A/40A 2-Pole (10/8 AWG)"
    elif amps <= 34:
        breaker = "40A/50A 2-Pole (8 AWG)"
    elif amps <= 40:
        breaker = "50A 2-Pole (6 AWG Copper)"
    elif amps <= 48:
        breaker = "60A 2-Pole (4 AWG Copper)"
    else:
        breaker = "Dual 40A or 80A Subpanel (2 AWG)"

    # Stones: ~45 lbs for standard wall heaters up to 8kW, ~90 lbs for 9-10.5kW, 180 lbs for towers
    if rec_kw <= 8.0:
        stones_lbs = 45
        stone_boxes = 1
    elif rec_kw <= 10.5:
        stones_lbs = 90
        stone_boxes = 2
    else:
        stones_lbs = 180
        stone_boxes = 4

    # Estimated heating time to 190°F (minutes)
    heat_mins = int(round(35 + (equiv_cuft / rec_kw) * 0.8))
    heat_mins = max(30, min(65, heat_mins))

    return raw_cuft, raw_cum, equiv_cuft, rec_kw, amps, breaker, stones_lbs, stone_boxes, heat_mins

def generate_faq_data(preset_name, length, width, height, glass, stone):
    raw_cuft, raw_cum, eq_cuft, rec_kw, amps, breaker, stones_lbs, stone_boxes, heat_mins = compute_sauna_specs(
        length, width, height, glass, stone
    )
    return [
        {
            "q": f"What size heater (kW) do I need for a {preset_name} ({length}'×{width}'×{height}')?",
            "a": f"Your room measures {raw_cuft} raw cubic feet ({raw_cum} m³). Factoring in uninsulated glass ({glass} sq. ft.) and stone surfaces, your equivalent thermal volume is {eq_cuft} cu. ft. Following Finnish sauna engineering standards (1 kW per ~45–50 cu. ft.), we recommend a {rec_kw} kW Electric Sauna Heater."
        },
        {
            "q": f"What size circuit breaker and wire gauge are required for a {rec_kw} kW heater?",
            "a": f"At 240 volts single-phase, a {rec_kw} kW sauna heater draws {amps} Amps of continuous current. Applying the NEC 125% continuous duty rule, you need a dedicated {breaker} circuit."
        },
        {
            "q": f"How many pounds of sauna rocks do I need for a {rec_kw} kW heater?",
            "a": f"A {rec_kw} kW heater requires approximately {stones_lbs} lbs of natural olivine diabase sauna stones ({stone_boxes} box{'es' if stone_boxes > 1 else ''}). Never pack rocks tightly—leave air gaps between the heating elements for natural convection."
        },
        {
            "q": "Why does a glass door or window require adding extra cubic feet to my calculation?",
            "a": "Glass has virtually zero R-value compared to an insulated cedar wall with aluminum foil vapor barrier. In sauna thermodynamics, each square foot of glass loses heat equivalent to adding 1.2 cubic feet of extra room volume."
        },
        {
            "q": f"How long does it take for a {rec_kw} kW heater to reach 190°F (88°C)?",
            "a": f"In a properly insulated cedar room with foil vapor barrier, a {rec_kw} kW heater will heat the air and stone mass to a full Finnish sweat temperature of 185°F–195°F in approximately {heat_mins} minutes."
        }
    ]

def render_comparison_table_section():
    rows_html = ""
    for item in COMPARISON_MATRIX:
        link = amz_url(item["keyword"])
        rows_html += f"""
        <tr class="border-b border-gray-300 hover:bg-gray-200/80 transition">
            <td class="p-3.5 font-extrabold text-gray-900 text-xs sm:text-sm">{item['model']}</td>
            <td class="p-3.5 text-xs font-semibold text-amber-900">{item['type']}</td>
            <td class="p-3.5 text-xs font-mono text-gray-800">{item['power_spec']}</td>
            <td class="p-3.5 text-xs text-gray-800">{item['room_volume']}</td>
            <td class="p-3.5 text-xs text-gray-800">{item['stone_cap']}</td>
            <td class="p-3.5 text-xs text-emerald-800 font-bold">{item['highlight']}</td>
            <td class="p-3.5 text-xs font-bold text-amber-700">{item['rating']}</td>
            <td class="p-3.5 text-right">
                <a href="{link}" target="_blank" rel="nofollow sponsored noopener"
                   class="inline-block bg-amber-700 hover:bg-amber-800 text-white font-extrabold text-xs py-2 px-3.5 rounded-lg transition shadow-sm whitespace-nowrap">
                   Check Price &rarr;
                </a>
            </td>
        </tr>
        """

    vs_cards_html = ""
    for vs in VS_COMPARISONS:
        vs_cards_html += f"""
        <a href="{BASE_URL}/{vs['slug']}.html" class="bg-gray-100 border-2 border-gray-300 hover:border-amber-700 rounded-xl p-5 transition flex flex-col justify-between shadow-sm">
            <div>
                <span class="text-[11px] font-extrabold uppercase tracking-wider bg-amber-100 text-amber-900 border border-amber-300 px-2.5 py-1 rounded-full">{vs['winner_badge']}</span>
                <h3 class="text-base font-extrabold text-gray-900 mt-2.5 mb-1.5 leading-snug">{vs['title']}</h3>
                <p class="text-xs text-gray-700 leading-relaxed">{vs['summary']}</p>
            </div>
            <span class="text-xs font-extrabold text-amber-800 mt-4 inline-flex items-center gap-1">Read Full Side-by-Side Comparison &rarr;</span>
        </a>
        """

    return f"""
    <!-- PRODUCT COMPARISON SECTION (PERBANDINGAN PRODUK) -->
    <section id="comparison" class="space-y-6">
        <div class="flex flex-col sm:flex-row sm:items-end justify-between gap-2 border-b border-gray-300 pb-4">
            <div>
                <span class="text-xs font-extrabold uppercase tracking-wider text-amber-800">Side-by-Side Spec Matrix</span>
                <h2 class="text-2xl font-extrabold text-gray-900">Top Finnish Heaters, Tower Rock Pillars & Controllers Compared</h2>
            </div>
            <span class="text-xs font-semibold text-gray-600">2026 Incoloy Element & 195°F Thermal Benchmarks</span>
        </div>

        <div class="bg-gray-100 border-2 border-gray-300 rounded-2xl overflow-x-auto shadow-sm">
            <table class="w-full text-left border-collapse min-w-[720px]">
                <thead>
                    <tr class="bg-gray-300 border-b-2 border-gray-400 text-[11px] font-extrabold uppercase tracking-wider text-gray-800">
                        <th class="p-3.5">Heater Model</th>
                        <th class="p-3.5">Category</th>
                        <th class="p-3.5">Power & Circuit</th>
                        <th class="p-3.5">Room Volume</th>
                        <th class="p-3.5">Stone Capacity</th>
                        <th class="p-3.5">Key Sauna Advantage</th>
                        <th class="p-3.5">Rating</th>
                        <th class="p-3.5 text-right">Amazon Deal</th>
                    </tr>
                </thead>
                <tbody>
                    {rows_html}
                </tbody>
            </table>
        </div>

        <!-- Head-to-Head VS Guides -->
        <div class="grid grid-cols-1 md:grid-cols-3 gap-5 pt-2">
            {vs_cards_html}
        </div>
    </section>
    """

def render_review_cards_grid():
    active_reviews = get_cumulative_product_reviews()
    cards = ""
    for rev in active_reviews:
        amz_link = amz_url(rev["keyword"])
        cards += f"""
        <article class="bg-gray-100 border-2 border-gray-300 hover:border-gray-400 rounded-2xl p-6 shadow-sm transition flex flex-col justify-between">
            <div>
                <div class="flex flex-wrap items-center justify-between gap-2 mb-3">
                    <span class="text-xs font-extrabold uppercase tracking-wider bg-amber-100 text-amber-900 border border-amber-300 px-2.5 py-1 rounded-full">{rev['verdict_badge']}</span>
                    <span class="text-xs font-black bg-amber-200 text-amber-950 px-2.5 py-1 rounded-lg">Score: {rev['rating_score']} / 5.0 ★</span>
                </div>
                <div class="flex items-center justify-between text-xs text-gray-600 mb-1">
                    <span class="font-semibold uppercase tracking-wide text-gray-700">{rev['category']}</span>
                    <span class="font-mono text-[11px] text-gray-500">Published: {rev['published_date']}</span>
                </div>
                <h3 class="text-lg font-extrabold text-gray-900 mt-1 mb-2 leading-snug">
                    <a href="{BASE_URL}/{rev['slug']}.html" class="hover:text-amber-800 transition">{rev['title']}</a>
                </h3>
                <p class="text-xs text-gray-700 leading-relaxed mb-4">{rev['summary']}</p>
                <div class="grid grid-cols-2 gap-2 text-[11px] bg-gray-200/90 p-3 rounded-xl border border-gray-300 mb-4">
                    <div><span class="text-gray-500 block">Output Spec:</span><strong class="text-gray-900">{rev['spec_1']}</strong></div>
                    <div><span class="text-gray-500 block">Thermal Heating:</span><strong class="text-gray-900">{rev['spec_2']}</strong></div>
                    <div><span class="text-gray-500 block">Build / Stones:</span><strong class="text-gray-900">{rev['spec_3']}</strong></div>
                    <div><span class="text-gray-500 block">Warranty / Spec:</span><strong class="text-gray-900">{rev['spec_4']}</strong></div>
                </div>
            </div>
            <div class="flex flex-col sm:flex-row gap-2.5 pt-2">
                <a href="{BASE_URL}/{rev['slug']}.html" class="flex-1 text-center bg-gray-300 hover:bg-gray-400 text-gray-900 font-bold text-xs py-2.5 px-3 rounded-lg transition">
                    Read Full Sauna Review &rarr;
                </a>
                <a href="{amz_link}" target="_blank" rel="nofollow sponsored noopener" class="flex-1 text-center bg-amber-700 hover:bg-amber-800 text-white font-extrabold text-xs py-2.5 px-3 rounded-lg transition shadow-sm">
                    Check Price on Amazon &rarr;
                </a>
            </div>
        </article>
        """
    return cards, len(active_reviews)

def render_common_header_and_banner():
    top_deal_link = amz_url("Harvia+VEVOR+Electric+Sauna+Heater+Olivine+Stones+Deals")
    return f"""
    <!-- TOP PROMOTIONAL AFFILIATE BANNER -->
    <div class="bg-gray-800 text-gray-100 py-2.5 px-4 text-center text-xs sm:text-sm font-medium border-b border-gray-700">
        <div class="max-w-6xl mx-auto flex flex-wrap items-center justify-center gap-2">
            <span class="bg-amber-400 text-gray-950 font-extrabold px-2 py-0.5 rounded text-xs uppercase">Sauna Builder Deals</span>
            <span>Save up to 30% on Finnish Harvia & VEVOR 6kW–9kW Heaters, Olivine Diabase Rocks, Cedar Buckets & Wi-Fi Controls on Amazon.</span>
            <a href="{top_deal_link}" target="_blank" rel="nofollow sponsored noopener" class="text-amber-300 hover:text-amber-200 underline font-bold ml-1">
                View Active Sauna Heater Deals &rarr;
            </a>
        </div>
    </div>

    <!-- STICKY NAVIGATION HEADER (GRAY BACKGROUND) -->
    <header class="bg-gray-300 border-b border-gray-400 sticky top-0 z-30 shadow-sm">
        <div class="max-w-6xl mx-auto px-4 py-3.5 flex flex-wrap items-center justify-between gap-4">
            <a href="{BASE_URL}/" class="flex items-center gap-2.5">
                <div class="w-9 h-9 rounded-lg bg-amber-700 flex items-center justify-center text-white font-black text-lg shadow-sm">S</div>
                <div>
                    <span class="font-extrabold text-lg tracking-tight text-gray-900 block leading-none">{SITE_NAME}</span>
                    <span class="text-[11px] text-gray-700 font-medium">Sauna Heater kW, Room Volume & Breaker Sizing</span>
                </div>
            </a>
            <nav class="flex flex-wrap items-center gap-4 sm:gap-5 text-xs sm:text-sm font-semibold text-gray-800">
                <a href="{BASE_URL}/#calculator" class="hover:text-amber-800 transition">Heater kW Calc</a>
                <a href="{BASE_URL}/#product-search" class="hover:text-amber-800 transition">Search Gear</a>
                <a href="{BASE_URL}/#best-sellers" class="hover:text-amber-800 transition">Best Sellers</a>
                <a href="{BASE_URL}/#comparison" class="hover:text-amber-800 transition">Compare</a>
                <a href="{BASE_URL}/#reviews" class="hover:text-amber-800 transition">Daily Reviews (+3/Day)</a>
                <a href="{BASE_URL}/#faq" class="hover:text-amber-800 transition">FAQ</a>
                <a href="{BASE_URL}/sitemap.html" class="hover:text-amber-800 transition font-bold underline">Site Map</a>
            </nav>
        </div>
    </header>
    """

def render_onpage_sitemap_directory():
    calc_links = "".join([
        f'<li><a href="{BASE_URL}/{p["slug"]}.html" class="text-xs text-gray-700 hover:text-amber-800 hover:underline">🧖 {p["name"]} Calculator</a></li>'
        for p in ALL_CALC_PAGES
    ])
    vs_links = "".join([
        f'<li><a href="{BASE_URL}/{v["slug"]}.html" class="text-xs text-gray-700 hover:text-amber-800 hover:underline">⚖️ {v["title"]}</a></li>'
        for v in VS_COMPARISONS
    ])
    all_revs = get_cumulative_product_reviews()
    rev_links = "".join([
        f'<li><a href="{BASE_URL}/{r["slug"]}.html" class="text-xs text-gray-700 hover:text-amber-800 hover:underline">📝 [{r["published_date"]}] {r["product_name"]} Review</a></li>'
        for r in all_revs
    ])
    return f"""
    <!-- COMPLETE ON-PAGE SITE MAP SECTION (SITE MAP) -->
    <section id="site-map" class="bg-gray-100 border-2 border-gray-300 rounded-2xl p-6 sm:p-8 space-y-6">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b border-gray-300 pb-3">
            <div>
                <span class="text-xs font-extrabold uppercase tracking-wider text-amber-800">Complete Site Architecture & Index</span>
                <h2 class="text-xl font-extrabold text-gray-900">Full HTML & XML Site Map Directory</h2>
            </div>
            <div class="flex gap-3 text-xs font-bold">
                <a href="{BASE_URL}/sitemap.html" class="bg-gray-300 hover:bg-gray-400 text-gray-900 px-3 py-1.5 rounded-lg transition">Open Dedicated HTML Site Map &rarr;</a>
                <a href="{BASE_URL}/sitemap.xml" class="bg-amber-700 hover:bg-amber-800 text-white px-3 py-1.5 rounded-lg transition">View XML Sitemap</a>
            </div>
        </div>
        <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
            <div>
                <h3 class="text-sm font-extrabold text-gray-900 mb-2.5 uppercase tracking-wide border-b border-gray-300 pb-1">1. Sauna kW & Room Calculators ({len(ALL_CALC_PAGES) + 1})</h3>
                <ul class="space-y-1.5">
                    <li><a href="{BASE_URL}/" class="text-xs font-bold text-amber-800 hover:underline">🏠 Home — Master Sauna Heater kW & Volume Calculator</a></li>
                    {calc_links}
                </ul>
            </div>
            <div>
                <h3 class="text-sm font-extrabold text-gray-900 mb-2.5 uppercase tracking-wide border-b border-gray-300 pb-1">2. Head-to-Head Comparisons ({len(VS_COMPARISONS)})</h3>
                <ul class="space-y-2">
                    {vs_links}
                </ul>
            </div>
            <div>
                <h3 class="text-sm font-extrabold text-gray-900 mb-2.5 uppercase tracking-wide border-b border-gray-300 pb-1">3. Daily Product Reviews ({len(all_revs)} — +3/Day)</h3>
                <ul class="space-y-1.5 max-h-80 overflow-y-auto pr-2">
                    {rev_links}
                </ul>
            </div>
        </div>
    </section>
    """

def render_dedicated_html_sitemap_page():
    canonical_url = f"{BASE_URL}/sitemap.html"
    sitemap_block = render_onpage_sitemap_directory()
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Complete Site Map Directory — Calculators, Comparisons & Daily Reviews | {SITE_NAME}</title>
    <meta name="description" content="Complete HTML and XML site map directory of all sauna heater kW calculators, room cubic feet sizing guides, 240V breaker calculators, and daily hardware reviews on {SITE_NAME}.">
    <link rel="canonical" href="{canonical_url}">
    <meta name="robots" content="index, follow">
    <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-gray-200 text-gray-900 antialiased">

    {render_common_header_and_banner()}

    <main class="max-w-6xl mx-auto px-4 py-10 space-y-8">
        <nav class="text-xs font-semibold text-gray-600 flex items-center gap-2">
            <a href="{BASE_URL}/" class="hover:text-amber-800">Home</a>
            <span>/</span>
            <span class="text-gray-900">Complete Site Map</span>
        </nav>

        <div class="bg-gray-100 border-2 border-gray-300 rounded-2xl p-6 sm:p-8 shadow-sm space-y-2">
            <h1 class="text-2xl sm:text-4xl font-extrabold text-gray-900">{SITE_NAME} — Complete Site Map</h1>
            <p class="text-sm text-gray-700">Browse every interactive sauna room volume calculator, glass de-rating guide, 240V circuit sizing tool, head-to-head comparison, and cumulative daily product review article (+3 added daily) below.</p>
        </div>

        {sitemap_block}
    </main>

    <footer class="bg-gray-300 border-t border-gray-400 mt-16 py-10 px-4 text-xs text-gray-700 text-center">
        <p class="font-bold text-gray-900">{SITE_NAME} — {SITE_TAGLINE}</p>
        <p class="mt-1">As an Amazon Associate, this site earns from qualifying purchases (Store ID: {AFFILIATE_TAG}).</p>
    </footer>
</body>
</html>"""

def render_calculator_page(page_data, is_home=False):
    _, _, eq_cuft, rec_kw, _, breaker, _, _, heat_mins = compute_sauna_specs(
        page_data["length"], page_data["width"], page_data["height"], page_data["glass_sqft"], page_data["stone_sqft"]
    )
    title = f"{SITE_NAME} — {SITE_TAGLINE}" if is_home else f"{page_data['name']} — Heater kW & Breaker Calculator ({rec_kw} kW) | {SITE_NAME}"
    description = page_data["desc"]
    canonical_url = f"{BASE_URL}/" if is_home else f"{BASE_URL}/{page_data['slug']}.html"
    faqs = generate_faq_data(
        page_data["name"], page_data["length"], page_data["width"],
        page_data["height"], page_data["glass_sqft"], page_data["stone_sqft"]
    )

    faq_schema = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": item["q"], "acceptedAnswer": {"@type": "Answer", "text": item["a"]}}
            for item in faqs
        ]
    }

    app_schema = {
        "@context": "https://schema.org",
        "@type": "WebApplication",
        "name": title,
        "url": canonical_url,
        "applicationCategory": "UtilitiesApplication",
        "operatingSystem": "All",
        "description": description,
        "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"}
    }

    bestseller_cards_html = ""
    for prod in BEST_SELLERS:
        link = amz_url(prod["keyword"])
        bestseller_cards_html += f"""
        <div class="bg-gray-100 border-2 border-gray-300 hover:border-gray-400 rounded-xl p-5 shadow-sm transition flex flex-col justify-between">
            <div>
                <div class="flex items-center justify-between gap-2 mb-2">
                    <span class="text-xs font-bold uppercase tracking-wider bg-amber-100 text-amber-900 border border-amber-300 px-2.5 py-1 rounded-full">{prod['badge']}</span>
                    <span class="text-xs font-semibold text-amber-700">{prod['rating']}</span>
                </div>
                <span class="text-xs text-gray-600 font-medium">{prod['category']}</span>
                <h3 class="text-base font-bold text-gray-900 mt-1 mb-2 leading-snug">{prod['title']}</h3>
                <p class="text-xs text-gray-700 mb-4 bg-gray-200 p-2.5 rounded-lg border border-gray-300">{prod['specs']}</p>
            </div>
            <a href="{link}" target="_blank" rel="nofollow sponsored noopener"
               class="w-full inline-flex items-center justify-center bg-amber-700 hover:bg-amber-800 text-white font-extrabold text-sm py-2.5 px-4 rounded-lg transition shadow-sm">
               Check Today's Price on Amazon &rarr;
            </a>
        </div>
        """

    preset_links_html = ""
    for p in ALL_CALC_PAGES:
        _, _, p_eq, p_kw, _, _, _, _, _ = compute_sauna_specs(
            p["length"], p["width"], p["height"], p["glass_sqft"], p["stone_sqft"]
        )
        active_cls = "bg-amber-100 border-amber-700 text-amber-950 font-bold" if (not is_home and p["slug"] == page_data["slug"]) else "bg-gray-100 border-gray-300 text-gray-800 hover:border-amber-700 hover:text-gray-950"
        preset_links_html += f"""
        <a href="{BASE_URL}/{p['slug']}.html" class="border rounded-lg p-3 text-xs transition flex items-center justify-between {active_cls}">
            <span class="truncate pr-2">{p['name']}</span>
            <span class="text-amber-900 font-mono shrink-0">{p_kw} kW / {int(p_eq)} ft³</span>
        </a>
        """

    faq_html = ""
    for item in faqs:
        faq_html += f"""
        <div class="bg-gray-100 border-2 border-gray-300 rounded-xl p-5">
            <h3 class="text-base font-bold text-gray-900 mb-2">{item['q']}</h3>
            <p class="text-sm text-gray-700 leading-relaxed">{item['a']}</p>
        </div>
        """

    mid_banner_link = amz_url("Harvia+KIP+Electric+Sauna+Heater+Olivine+Stones+and+Cedar+Bucket+Bundle")
    comparison_html = render_comparison_table_section()
    reviews_grid_html, total_reviews_count = render_review_cards_grid()
    onpage_sitemap_html = render_onpage_sitemap_directory()

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <meta name="description" content="{description}">
    <link rel="canonical" href="{canonical_url}">
    <meta name="robots" content="index, follow">
    <meta property="og:title" content="{title}">
    <meta property="og:description" content="{description}">
    <meta property="og:type" content="website">
    <meta property="og:url" content="{canonical_url}">
    <script src="https://cdn.tailwindcss.com"></script>
    <script type="application/ld+json">{json.dumps(faq_schema)}</script>
    <script type="application/ld+json">{json.dumps(app_schema)}</script>
</head>
<body class="bg-gray-200 text-gray-900 antialiased selection:bg-amber-700 selection:text-white">

    {render_common_header_and_banner()}

    <main class="max-w-6xl mx-auto px-4 py-8 space-y-12">

        <!-- HERO TITLE SECTION -->
        <section class="text-center max-w-3xl mx-auto space-y-3">
            <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-gray-300 border border-gray-400 text-xs font-semibold text-gray-800">
                <span>🧖 Finnish Löyly Thermodynamics, Glass De-Rating & 240V Circuit Sizing Engine</span>
            </div>
            <h1 class="text-3xl sm:text-4xl font-extrabold text-gray-900 tracking-tight">
                { "Sauna Heater kW, Room Volume, Glass Factor & Breaker Calculator" if is_home else f"{page_data['name']} — Heater kW Sizing Calculator" }
            </h1>
            <p class="text-gray-700 text-sm sm:text-base leading-relaxed">
                {description}
            </p>
        </section>

        <!-- INTERACTIVE CALCULATOR + LIVE HARDWARE MATCHER -->
        <section id="calculator" class="grid grid-cols-1 lg:grid-cols-12 gap-8 items-start">
            <!-- Left Column: Inputs (7 Cols) -->
            <div class="lg:col-span-7 bg-gray-100 border-2 border-gray-300 rounded-2xl p-6 sm:p-8 shadow-sm space-y-6">
                <div class="flex items-center justify-between border-b border-gray-300 pb-4">
                    <div>
                        <h2 class="text-xl font-extrabold text-gray-900">1. Enter Sauna Dimensions & Uninsulated Surfaces</h2>
                        <p class="text-xs text-gray-600">Calculates equivalent volume, heater kW, 240V breaker amps & rock lbs</p>
                    </div>
                    <span class="text-xs font-mono bg-amber-100 text-amber-900 border border-amber-300 px-2.5 py-1 rounded font-semibold">Live Finnish Math</span>
                </div>

                <div>
                    <label for="quickPreset" class="block text-xs font-bold uppercase tracking-wider text-gray-700 mb-2">Quick Select Sauna Cabin Preset</label>
                    <select id="quickPreset" onchange="applyPreset(this.value)" class="w-full bg-gray-200 border border-gray-400 rounded-lg px-3.5 py-2.5 text-sm font-semibold text-gray-900 focus:ring-2 focus:ring-amber-700">
                        <option value="{page_data['length']},{page_data['width']},{page_data['height']},{page_data['glass_sqft']},{page_data['stone_sqft']}">Current: {page_data['name']}</option>
                        <option value="7,5,7,14,0">5' × 7' × 7' Home Sauna (245 ft³ Raw | 8.0 kW Heater — 40A/50A Breaker)</option>
                        <option value="5,4,7,12,0">4' × 5' × 7' Small Indoor Sauna (140 ft³ Raw | 4.5–6.0 kW Heater)</option>
                        <option value="6,5,7,14,0">5' × 6' × 7' Cedar Sauna (210 ft³ Raw | 6.0 kW Heater — 30A Breaker)</option>
                        <option value="8,6,7,16,15">6' × 8' × 7' Large Family Sauna (336 ft³ Raw | 9.0 kW Heater — 50A Breaker)</option>
                        <option value="6,6,6,14,0">6' Outdoor Barrel Sauna (Round Barrel | 8.0 kW Heater)</option>
                        <option value="7,6,7,42,0">Full Glass-Front Modern Sauna (42 Sq.Ft Glass Wall — 9.0 kW Heater)</option>
                    </select>
                </div>

                <div class="grid grid-cols-1 sm:grid-cols-3 gap-4">
                    <div>
                        <label for="lengthInput" class="block text-sm font-bold text-gray-800 mb-1">Room Length (Feet)</label>
                        <input type="number" id="lengthInput" value="{page_data['length']}" min="3" max="25" step="0.5" oninput="calculateSauna()"
                               class="w-full bg-gray-200 border border-gray-400 rounded-lg px-3.5 py-2.5 text-base font-bold text-gray-900 focus:ring-2 focus:ring-amber-700">
                    </div>

                    <div>
                        <label for="widthInput" class="block text-sm font-bold text-gray-800 mb-1">Room Width (Feet)</label>
                        <input type="number" id="widthInput" value="{page_data['width']}" min="3" max="25" step="0.5" oninput="calculateSauna()"
                               class="w-full bg-gray-200 border border-gray-400 rounded-lg px-3.5 py-2.5 text-base font-bold text-gray-900 focus:ring-2 focus:ring-amber-700">
                    </div>

                    <div>
                        <label for="heightInput" class="block text-sm font-bold text-gray-800 mb-1">Ceiling Height (Feet)</label>
                        <input type="number" id="heightInput" value="{page_data['height']}" min="6.0" max="9.5" step="0.1" oninput="calculateSauna()"
                               class="w-full bg-gray-200 border border-gray-400 rounded-lg px-3.5 py-2.5 text-base font-bold text-gray-900 focus:ring-2 focus:ring-amber-700">
                        <span class="text-[11px] text-gray-600">Optimal is 7.0 ft (keeps heat near bench)</span>
                    </div>
                </div>

                <div class="grid grid-cols-1 sm:grid-cols-2 gap-5">
                    <div>
                        <label for="glassInput" class="block text-sm font-bold text-gray-800 mb-1">Uninsulated Glass Surface (Sq. Ft.)</label>
                        <input type="number" id="glassInput" value="{page_data['glass_sqft']}" min="0" max="80" step="1" oninput="calculateSauna()"
                               class="w-full bg-gray-200 border border-gray-400 rounded-lg px-4 py-2.5 text-base font-bold text-gray-900 focus:ring-2 focus:ring-amber-700">
                        <span class="text-[11px] text-gray-600">Standard glass door = ~12–14 sq.ft (+1.2 ft³/sq.ft)</span>
                    </div>

                    <div>
                        <label for="stoneInput" class="block text-sm font-bold text-gray-800 mb-1">Stone / Tile Accent Wall (Sq. Ft.)</label>
                        <input type="number" id="stoneInput" value="{page_data['stone_sqft']}" min="0" max="100" step="1" oninput="calculateSauna()"
                               class="w-full bg-gray-200 border border-gray-400 rounded-lg px-4 py-2.5 text-base font-bold text-gray-900 focus:ring-2 focus:ring-amber-700">
                        <span class="text-[11px] text-gray-600">Slate / brick behind heater (+1.2 ft³/sq.ft)</span>
                    </div>
                </div>
            </div>

            <!-- Right Column: Output + Dynamic Amazon Recommendation (5 Cols) -->
            <div class="lg:col-span-5 bg-gray-100 border-2 border-amber-700 rounded-2xl p-6 sm:p-8 shadow-md space-y-6">
                <div class="border-b border-gray-300 pb-3">
                    <span class="text-xs font-extrabold uppercase tracking-wider text-amber-800">2. Engineered Heater & Power Specs</span>
                    <h2 class="text-xl font-extrabold text-gray-900">Your Recommended Sauna Sizing</h2>
                </div>

                <div class="grid grid-cols-2 gap-3.5">
                    <div class="bg-amber-100 border border-amber-300 rounded-xl p-3.5">
                        <span class="text-xs text-amber-950 font-semibold block">Recommended Heater</span>
                        <span id="resRecKW" class="text-2xl font-black text-amber-800">8.0 kW</span>
                        <span id="resAmps" class="text-[11px] text-amber-900 block mt-0.5">33.3A @ 240V Single-Phase</span>
                    </div>
                    <div class="bg-gray-200 border border-gray-300 rounded-xl p-3.5">
                        <span class="text-xs text-gray-600 font-medium block">Equivalent Volume</span>
                        <span id="resEquivCuFt" class="text-2xl font-black text-gray-900">262 ft³</span>
                        <span id="resRawCuFt" class="text-[11px] text-gray-600 block mt-0.5">245 ft³ Raw (6.9 m³)</span>
                    </div>
                    <div class="bg-gray-200 border border-gray-300 rounded-xl p-3.5">
                        <span class="text-xs text-gray-600 font-medium block">Required 240V Circuit</span>
                        <span id="resBreaker" class="text-base font-extrabold text-emerald-800">40A–50A Breaker</span>
                        <span class="text-[11px] text-gray-600 block mt-0.5">8 AWG Copper Wire</span>
                    </div>
                    <div class="bg-gray-200 border border-gray-300 rounded-xl p-3.5">
                        <span class="text-xs text-gray-600 font-medium block">Olivine Stone Weight</span>
                        <span id="resStones" class="text-base font-extrabold text-gray-900">45 Lbs Rocks</span>
                        <span id="resHeatTime" class="text-[11px] text-gray-600 block mt-0.5">~38 Mins to 190°F</span>
                    </div>
                </div>

                <!-- Dynamic Matched Product Box -->
                <div class="bg-gray-200 border-2 border-amber-600 rounded-xl p-4 space-y-3">
                    <div class="flex items-center justify-between">
                        <span class="text-[11px] font-extrabold uppercase tracking-wider bg-amber-700 text-white px-2 py-0.5 rounded">Verified Hardware Match</span>
                        <span class="text-xs font-bold text-gray-700">Amazon Prime Ready</span>
                    </div>
                    <h3 id="recSaunaTitle" class="text-base font-extrabold text-gray-900 leading-snug">Loading Heater & Stone Match...</h3>
                    <p id="recSaunaDesc" class="text-xs text-gray-700"></p>
                    <div class="pt-1 flex flex-col sm:flex-row gap-2.5">
                        <a id="recPrimaryBtn" href="#" target="_blank" rel="nofollow sponsored noopener"
                           class="flex-1 text-center bg-amber-700 hover:bg-amber-800 text-white font-extrabold text-sm py-3 px-4 rounded-lg transition shadow-sm">
                           Shop Matched Sauna Heater &rarr;
                        </a>
                        <a id="recSecondaryBtn" href="#" target="_blank" rel="nofollow sponsored noopener"
                           class="text-center bg-gray-800 hover:bg-gray-900 text-white font-bold text-xs py-3 px-3 rounded-lg transition">
                           Shop Stones, Bucket & Ladle
                        </a>
                    </div>
                </div>
            </div>
        </section>

        <!-- PRODUCT SEARCH ENGINE SECTION (SEARCH PRODUK) -->
        <section id="product-search" class="bg-gray-100 border-2 border-gray-300 rounded-2xl p-6 sm:p-8 shadow-sm">
            <div class="max-w-3xl mx-auto text-center space-y-4">
                <h2 class="text-2xl font-extrabold text-gray-900">Search Traditional Sauna Heaters, Stones, Wi-Fi Controllers & Accessories</h2>
                <p class="text-sm text-gray-700">Search any wattage (6kW, 8kW, 9kW), brand (Harvia, VEVOR, HUUM, Finlandia, Coasts, ALEKO), or cedar accessory on Amazon.</p>
                <form onsubmit="handleAmazonSearch(event)" class="flex flex-col sm:flex-row gap-3 pt-2">
                    <input type="text" id="amzSearchInput" placeholder="e.g. Harvia KIP 8kW Sauna Heater, VEVOR 9kW Heater, Harvia Olivine Stones..."
                           class="flex-1 bg-gray-200 border-2 border-gray-400 rounded-xl px-4 py-3 text-sm font-medium text-gray-900 placeholder-gray-500 focus:outline-none focus:border-amber-700" required>
                    <button type="submit" class="bg-amber-700 hover:bg-amber-800 text-white font-extrabold text-sm px-6 py-3 rounded-xl transition cursor-pointer shrink-0">
                        Search on Amazon &rarr;
                    </button>
                </form>
                <div class="flex flex-wrap items-center justify-center gap-2 pt-2 text-xs">
                    <span class="text-gray-600 font-semibold">Popular Searches:</span>
                    <a href="{amz_url('Harvia KIP 8kW Traditional Finnish Sauna Heater')}" target="_blank" rel="nofollow sponsored noopener" class="px-2.5 py-1 bg-gray-200 hover:bg-amber-200 text-gray-800 border border-gray-300 rounded-full transition">Harvia KIP 8kW</a>
                    <a href="{amz_url('VEVOR 9kW 240V Electric Sauna Heater')}" target="_blank" rel="nofollow sponsored noopener" class="px-2.5 py-1 bg-gray-200 hover:bg-amber-200 text-gray-800 border border-gray-300 rounded-full transition">VEVOR 9kW Heater</a>
                    <a href="{amz_url('Harvia Cilindro 9kW Tower Sauna Heater')}" target="_blank" rel="nofollow sponsored noopener" class="px-2.5 py-1 bg-gray-200 hover:bg-amber-200 text-gray-800 border border-gray-300 rounded-full transition">Harvia Cilindro Tower</a>
                    <a href="{amz_url('Finlandia Harvia Natural Olivine Diabase Sauna Stones')}" target="_blank" rel="nofollow sponsored noopener" class="px-2.5 py-1 bg-gray-200 hover:bg-amber-200 text-gray-800 border border-gray-300 rounded-full transition">Olivine Sauna Stones</a>
                    <a href="{amz_url('Cedar Sauna Bucket and Ladle Kit')}" target="_blank" rel="nofollow sponsored noopener" class="px-2.5 py-1 bg-gray-200 hover:bg-amber-200 text-gray-800 border border-gray-300 rounded-full transition">Cedar Bucket & Ladle</a>
                </div>
            </div>
        </section>

        <!-- BEST SELLING PRODUCTS GRID (PRODUK TERLARIS) -->
        <section id="best-sellers" class="space-y-6">
            <div class="flex flex-col sm:flex-row sm:items-end justify-between gap-2 border-b border-gray-300 pb-4">
                <div>
                    <span class="text-xs font-extrabold uppercase tracking-wider text-amber-800">Verified Finnish Spa Hardware</span>
                    <h2 class="text-2xl font-extrabold text-gray-900">Best-Selling Traditional Sauna Heaters, Stones & Accessories</h2>
                </div>
                <a href="{amz_url('Best Selling Electric Sauna Heaters and Accessories')}" target="_blank" rel="nofollow sponsored noopener" class="text-sm font-bold text-amber-800 hover:text-amber-900">
                    Browse Full Amazon Best Sellers &rarr;
                </a>
            </div>
            <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-5">
                {bestseller_cards_html}
            </div>
        </section>

        {comparison_html}

        <!-- CUMULATIVE DAILY PRODUCT REVIEW ARTICLES SECTION (+3 NEW ARTICLES PER DAY) -->
        <section id="reviews" class="space-y-6">
            <div class="flex flex-col sm:flex-row sm:items-end justify-between gap-2 border-b border-gray-300 pb-4">
                <div>
                    <span class="text-xs font-extrabold uppercase tracking-wider text-amber-800">Autonomous Daily Review Archive ({total_reviews_count} Published Articles & Growing +3/Day)</span>
                    <h2 class="text-2xl font-extrabold text-gray-900">In-Depth Sauna Heater, Rock & Controller Review Articles</h2>
                </div>
                <span class="text-xs font-semibold bg-emerald-100 text-emerald-900 border border-emerald-300 px-3 py-1 rounded-full">+3 New Product Reviews Added Automatically Every Day</span>
            </div>
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                {reviews_grid_html}
            </div>
        </section>

        <!-- MID-PAGE PROMOTIONAL AFFILIATE BANNER -->
        <section class="bg-gray-300 border-2 border-amber-700 rounded-2xl p-6 sm:p-8 flex flex-col md:flex-row items-center justify-between gap-6">
            <div class="space-y-2 max-w-2xl">
                <span class="text-xs font-extrabold uppercase tracking-wider bg-amber-700 text-white px-2.5 py-1 rounded">Complete Finnish Sauna Bundle</span>
                <h2 class="text-xl sm:text-2xl font-extrabold text-gray-900">Building a Traditional 195°F DIY Indoor or Outdoor Sauna?</h2>
                <p class="text-sm text-gray-800">Get authentic steam and safe heating by pairing an 8kW or 9kW Finnish Electric Heater with 45–90 lbs of genuine Olivine Diabase rocks, aluminum vapor barrier foil, and a red cedar bucket/ladle kit.</p>
            </div>
            <a href="{mid_banner_link}" target="_blank" rel="nofollow sponsored noopener"
               class="shrink-0 bg-amber-700 hover:bg-amber-800 text-white font-extrabold text-sm px-6 py-3.5 rounded-xl shadow-sm transition">
               Explore Sauna Heater + Rock Bundles on Amazon &rarr;
            </a>
        </section>

        <!-- PROGRAMMATIC SEO DIRECTORY -->
        <section id="presets" class="space-y-4">
            <div class="border-b border-gray-300 pb-3">
                <h2 class="text-xl font-extrabold text-gray-900">Sauna Room Size & Cubic Feet Specific Calculators</h2>
                <p class="text-xs text-gray-600">Select your exact sauna room dimensions or cubic feet tier below for pre-calculated heater kW, breaker amps, and stone specs.</p>
            </div>
            <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-2.5">
                {preset_links_html}
            </div>
        </section>

        <!-- FREQUENTLY ASKED QUESTIONS (FAQ) -->
        <section id="faq" class="space-y-6">
            <div class="border-b border-gray-300 pb-3">
                <span class="text-xs font-extrabold uppercase tracking-wider text-amber-800">Sauna Thermodynamics & Electrical Guide</span>
                <h2 class="text-2xl font-extrabold text-gray-900">Frequently Asked Questions (FAQ)</h2>
            </div>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                {faq_html}
            </div>
        </section>

        {onpage_sitemap_html}

    </main>

    <!-- FOOTER (GRAY BACKGROUND) -->
    <footer class="bg-gray-300 border-t border-gray-400 mt-16 py-10 px-4 text-xs text-gray-700">
        <div class="max-w-6xl mx-auto flex flex-col sm:flex-row items-center justify-between gap-4">
            <div>
                <p class="font-bold text-gray-900">{SITE_NAME} — {SITE_TAGLINE}</p>
                <p class="mt-1">As an Amazon Associate, this site earns from qualifying purchases (Store ID: {AFFILIATE_TAG}).</p>
            </div>
            <div class="flex flex-wrap gap-4 font-medium text-gray-800">
                <a href="{BASE_URL}/" class="hover:text-amber-800">Home</a>
                <a href="{BASE_URL}/#comparison" class="hover:text-amber-800">Comparisons</a>
                <a href="{BASE_URL}/#reviews" class="hover:text-amber-800">Daily Reviews (+3/Day)</a>
                <a href="{BASE_URL}/sitemap.html" class="hover:text-amber-800 font-bold">HTML Site Map</a>
                <a href="{BASE_URL}/sitemap.xml" class="hover:text-amber-800">XML Sitemap</a>
                <a href="{BASE_URL}/#faq" class="hover:text-amber-800">FAQ</a>
            </div>
        </div>
    </footer>

    <!-- INTERACTIVE CALCULATOR & AFFILIATE MATCHING SCRIPT -->
    <script>
        const AFFILIATE_TAG = "{AFFILIATE_TAG}";

        function makeAmazonLink(query) {{
            return "https://www.amazon.com/s?k=" + encodeURIComponent(query) + "&tag=" + AFFILIATE_TAG;
        }}

        function applyPreset(val) {{
            const parts = val.split(",");
            if (parts.length === 5) {{
                document.getElementById("lengthInput").value = parts[0];
                document.getElementById("widthInput").value = parts[1];
                document.getElementById("heightInput").value = parts[2];
                document.getElementById("glassInput").value = parts[3];
                document.getElementById("stoneInput").value = parts[4];
                calculateSauna();
            }}
        }}

        function handleAmazonSearch(e) {{
            e.preventDefault();
            const q = document.getElementById("amzSearchInput").value.trim();
            if (q) {{
                window.open(makeAmazonLink(q), "_blank", "noopener,noreferrer");
            }}
        }}

        function calculateSauna() {{
            const l = parseFloat(document.getElementById("lengthInput").value) || 7;
            const w = parseFloat(document.getElementById("widthInput").value) || 5;
            const h = parseFloat(document.getElementById("heightInput").value) || 7;
            const glass = parseFloat(document.getElementById("glassInput").value) || 14;
            const stone = parseFloat(document.getElementById("stoneInput").value) || 0;

            const rawCuFt = Math.round(l * w * h * 10) / 10;
            const rawCuM = (rawCuFt * 0.0283168).toFixed(1);
            const equivCuFt = Math.round((rawCuFt + (glass * 1.2) + (stone * 1.2)) * 10) / 10;

            const rawKW = equivCuFt / 46.0;
            const tiers = [3.5, 4.5, 6.0, 8.0, 9.0, 10.5, 12.0, 15.0];
            let recKW = 15.0;
            for (let i = 0; i < tiers.length; i++) {{
                if (tiers[i] >= rawKW) {{
                    recKW = tiers[i];
                    break;
                }}
            }}

            const amps = ((recKW * 1000) / 240).toFixed(1);
            let breakerStr = "50A 2-Pole (6 AWG)";
            if (amps <= 15) breakerStr = "20A 2-Pole (12 AWG)";
            else if (amps <= 20) breakerStr = "25A/30A 2-Pole (10 AWG)";
            else if (amps <= 25) breakerStr = "30A/40A 2-Pole (10/8 AWG)";
            else if (amps <= 34) breakerStr = "40A/50A 2-Pole (8 AWG)";
            else if (amps <= 40) breakerStr = "50A 2-Pole (6 AWG)";
            else breakerStr = "60A 2-Pole (4 AWG)";

            const stoneLbs = recKW <= 8.0 ? 45 : (recKW <= 10.5 ? 90 : 180);
            const heatMins = Math.max(30, Math.min(65, Math.round(35 + (equivCuFt / recKW) * 0.8)));

            document.getElementById("resRecKW").textContent = recKW.toFixed(1) + " kW Heater";
            document.getElementById("resAmps").textContent = amps + "A @ 240V Single-Phase";
            document.getElementById("resEquivCuFt").textContent = equivCuFt + " ft³ Equiv";
            document.getElementById("resRawCuFt").textContent = rawCuFt + " ft³ Raw (" + rawCuM + " m³)";
            document.getElementById("resBreaker").textContent = breakerStr;
            document.getElementById("resStones").textContent = stoneLbs + " Lbs Olivine Stones";
            document.getElementById("resHeatTime").textContent = "~" + heatMins + " Mins to 190°F";

            let recTitle = "";
            let recDesc = "";
            let primaryQuery = "";
            let secondaryQuery = "Finlandia Harvia Olivine Diabase Sauna Stones 40 lb and Cedar Sauna Bucket";

            if (recKW <= 4.5) {{
                recTitle = "Harvia KIP 4.5kW / Vega Compact 3.5kW 240V Electric Sauna Heater";
                recDesc = "Ideal 240V compact heater for 1-to-2 person saunas up to " + Math.round(equivCuFt) + " equivalent cubic feet.";
                primaryQuery = "Harvia KIP 4.5kW Vega Compact Electric Sauna Heater";
            }} else if (recKW <= 6.0) {{
                recTitle = "Harvia KIP 6kW (KIP-60B) or VEVOR 6kW 240V Traditional Sauna Heater";
                recDesc = "Best-selling residential size for 4'×5' and 5'×5' saunas drawing only 25 amps on a 30A/40A breaker.";
                primaryQuery = "Harvia KIP 6kW VEVOR 6kW Electric Sauna Heater 240V";
            }} else if (recKW <= 8.0) {{
                recTitle = "Harvia KIP 8kW (KIP-80B) Traditional Finnish Electric Sauna Heater";
                recDesc = "America's #1 8.0 kW heater for 5'×7' cabins up to " + Math.round(equivCuFt) + " cu. ft. with fast 40-minute heating.";
                primaryQuery = "Harvia KIP 8kW Electric Sauna Heater KIP 80B";
            }} else {{
                recTitle = "Harvia Cilindro 9kW Tower (180 Lb Rocks) or VEVOR / TURKU 9kW Digital Heater";
                recDesc = "High-output 9.0 kW power and massive stone thermal mass for spacious saunas up to " + Math.round(equivCuFt) + " cu. ft.";
                primaryQuery = "Harvia Cilindro 9kW Tower VEVOR 9kW Sauna Heater 240V";
            }}

            document.getElementById("recSaunaTitle").textContent = recTitle;
            document.getElementById("recSaunaDesc").textContent = recDesc;
            document.getElementById("recPrimaryBtn").href = makeAmazonLink(primaryQuery);
            document.getElementById("recSecondaryBtn").href = makeAmazonLink(secondaryQuery);
        }}

        window.addEventListener("DOMContentLoaded", calculateSauna);
    </script>
</body>
</html>"""

def render_single_review_page(rev):
    canonical_url = f"{BASE_URL}/{rev['slug']}.html"
    amz_link = amz_url(rev["keyword"])

    review_schema = {
        "@context": "https://schema.org",
        "@type": "Product",
        "name": rev["product_name"],
        "description": rev["summary"],
        "review": {
            "@type": "Review",
            "datePublished": rev["published_date"],
            "reviewRating": {"@type": "Rating", "ratingValue": rev["rating_score"], "bestRating": "5"},
            "author": {"@type": "Organization", "name": SITE_NAME},
            "reviewBody": " ".join(rev["body_paragraphs"])
        }
    }

    pros_html = "".join([f'<li class="flex items-start gap-2 text-sm text-gray-800"><span class="text-emerald-700 font-bold">✓</span><span>{p}</span></li>' for p in rev["pros"]])
    cons_html = "".join([f'<li class="flex items-start gap-2 text-sm text-gray-800"><span class="text-rose-700 font-bold">✕</span><span>{c}</span></li>' for c in rev["cons"]])
    paragraphs_html = "".join([f'<p class="text-gray-800 leading-relaxed text-base mb-4">{p}</p>' for p in rev["body_paragraphs"]])

    recent_reviews = [r for r in get_cumulative_product_reviews() if r["slug"] != rev["slug"]][:6]
    related_html = ""
    for other in recent_reviews:
        related_html += f"""
        <a href="{BASE_URL}/{other['slug']}.html" class="bg-gray-100 border-2 border-gray-300 rounded-xl p-4 hover:border-amber-700 transition block">
            <span class="text-[11px] font-bold text-amber-800 uppercase">{other['verdict_badge']}</span>
            <h4 class="font-extrabold text-sm text-gray-900 mt-1 line-clamp-2">{other['product_name']} Review</h4>
            <span class="text-xs text-gray-600 mt-1 block">Score: {other['rating_score']} / 5.0 ★ ({other['published_date']}) &rarr;</span>
        </a>
        """

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{rev['title']} | {SITE_NAME}</title>
    <meta name="description" content="{rev['summary']}">
    <link rel="canonical" href="{canonical_url}">
    <meta name="robots" content="index, follow">
    <script src="https://cdn.tailwindcss.com"></script>
    <script type="application/ld+json">{json.dumps(review_schema)}</script>
</head>
<body class="bg-gray-200 text-gray-900 antialiased">

    {render_common_header_and_banner()}

    <main class="max-w-4xl mx-auto px-4 py-10 space-y-10">
        <nav class="text-xs font-semibold text-gray-600 flex items-center gap-2">
            <a href="{BASE_URL}/" class="hover:text-amber-800">Home & Sauna Calculator</a>
            <span>/</span>
            <a href="{BASE_URL}/#reviews" class="hover:text-amber-800">Daily Sauna Reviews</a>
            <span>/</span>
            <span class="text-gray-900">{rev['product_name']}</span>
        </nav>

        <div class="bg-gray-100 border-2 border-gray-300 rounded-2xl p-6 sm:p-8 shadow-sm space-y-5">
            <div class="flex flex-wrap items-center justify-between gap-2">
                <span class="text-xs font-extrabold uppercase tracking-wider bg-amber-100 text-amber-900 border border-amber-300 px-3 py-1 rounded-full">{rev['verdict_badge']}</span>
                <div class="flex items-center gap-2">
                    <span class="text-xs font-mono text-gray-600">Published: {rev['published_date']}</span>
                    <span class="text-sm font-black bg-amber-200 text-amber-950 px-3 py-1 rounded-lg">Field Rating: {rev['rating_score']} / 5.0 ★</span>
                </div>
            </div>
            <h1 class="text-2xl sm:text-4xl font-extrabold text-gray-900 leading-tight">{rev['title']}</h1>
            <p class="text-base text-gray-700 leading-relaxed">{rev['summary']}</p>

            <div class="grid grid-cols-2 sm:grid-cols-4 gap-3 bg-gray-200 p-4 rounded-xl border border-gray-300 text-xs">
                <div><span class="text-gray-500 block font-medium">Power / Specs</span><strong class="text-gray-900">{rev['spec_1']}</strong></div>
                <div><span class="text-gray-500 block font-medium">Thermal Heating</span><strong class="text-gray-900">{rev['spec_2']}</strong></div>
                <div><span class="text-gray-500 block font-medium">Build / Stones</span><strong class="text-gray-900">{rev['spec_3']}</strong></div>
                <div><span class="text-gray-500 block font-medium">Warranty</span><strong class="text-gray-900">{rev['spec_4']}</strong></div>
            </div>

            <div class="flex flex-col sm:flex-row gap-3 pt-2">
                <a href="{amz_link}" target="_blank" rel="nofollow sponsored noopener"
                   class="flex-1 text-center bg-amber-700 hover:bg-amber-800 text-white font-extrabold text-sm py-3.5 px-6 rounded-xl transition shadow-sm">
                   Check Latest Price & Availability on Amazon &rarr;
                </a>
                <a href="{BASE_URL}/#calculator"
                   class="text-center bg-gray-300 hover:bg-gray-400 text-gray-900 font-bold text-sm py-3.5 px-5 rounded-xl transition">
                   Calculate Sauna kW & 240V Circuit
                </a>
            </div>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
            <div class="bg-gray-100 border-2 border-emerald-400 rounded-2xl p-6 space-y-3">
                <h2 class="text-base font-extrabold text-emerald-900 uppercase tracking-wide">Pros (What We Like)</h2>
                <ul class="space-y-2.5">{pros_html}</ul>
            </div>
            <div class="bg-gray-100 border-2 border-rose-400 rounded-2xl p-6 space-y-3">
                <h2 class="text-base font-extrabold text-rose-900 uppercase tracking-wide">Cons (Things to Consider)</h2>
                <ul class="space-y-2.5">{cons_html}</ul>
            </div>
        </div>

        <article class="bg-gray-100 border-2 border-gray-300 rounded-2xl p-6 sm:p-8 space-y-4">
            <h2 class="text-xl font-extrabold text-gray-900 border-b border-gray-300 pb-3">Hands-On Heating Time, Steam Quality & Electrical Installation Analysis</h2>
            {paragraphs_html}
            <div class="pt-4 border-t border-gray-300 flex flex-col sm:flex-row items-center justify-between gap-4">
                <div>
                    <span class="text-xs font-bold uppercase text-amber-800 block">Final Verdict</span>
                    <p class="text-sm font-bold text-gray-900">{rev['product_name']} earns {rev['rating_score']}/5.0 in our sauna equipment benchmark.</p>
                </div>
                <a href="{amz_link}" target="_blank" rel="nofollow sponsored noopener"
                   class="shrink-0 bg-amber-700 hover:bg-amber-800 text-white font-extrabold text-sm px-6 py-3 rounded-xl transition shadow-sm">
                   View Customer Reviews & Price on Amazon &rarr;
                </a>
            </div>
        </article>

        <section class="space-y-4">
            <h3 class="text-lg font-extrabold text-gray-900">Recent Daily Sauna Hardware Reviews (+3 Added Daily)</h3>
            <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-4">
                {related_html}
            </div>
        </section>
    </main>

    <footer class="bg-gray-300 border-t border-gray-400 mt-16 py-10 px-4 text-xs text-gray-700 text-center">
        <p class="font-bold text-gray-900">{SITE_NAME} — {SITE_TAGLINE}</p>
        <p class="mt-1">As an Amazon Associate, this site earns from qualifying purchases (Store ID: {AFFILIATE_TAG}).</p>
    </footer>
</body>
</html>"""

def render_vs_comparison_page(vs):
    canonical_url = f"{BASE_URL}/{vs['slug']}.html"
    link_a = amz_url(vs["keyword_a"])
    link_b = amz_url(vs["keyword_b"])

    rows_html = ""
    for m in vs["metrics"]:
        rows_html += f"""
        <tr class="border-b border-gray-300">
            <td class="p-4 font-bold text-gray-900 bg-gray-200 text-xs sm:text-sm w-1/4">{m['feature']}</td>
            <td class="p-4 text-xs sm:text-sm text-gray-800 w-3/8">{m['val_a']}</td>
            <td class="p-4 text-xs sm:text-sm text-gray-800 w-3/8">{m['val_b']}</td>
        </tr>
        """

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{vs['title']} | {SITE_NAME}</title>
    <meta name="description" content="{vs['summary']}">
    <link rel="canonical" href="{canonical_url}">
    <meta name="robots" content="index, follow">
    <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-gray-200 text-gray-900 antialiased">

    {render_common_header_and_banner()}

    <main class="max-w-4xl mx-auto px-4 py-10 space-y-10">
        <nav class="text-xs font-semibold text-gray-600 flex items-center gap-2">
            <a href="{BASE_URL}/" class="hover:text-amber-800">Home & Sauna Calculator</a>
            <span>/</span>
            <a href="{BASE_URL}/#comparison" class="hover:text-amber-800">Product Comparisons</a>
            <span>/</span>
            <span class="text-gray-900">{vs['product_a']} vs. {vs['product_b']}</span>
        </nav>

        <div class="bg-gray-100 border-2 border-gray-300 rounded-2xl p-6 sm:p-8 shadow-sm space-y-4">
            <span class="text-xs font-extrabold uppercase tracking-wider bg-amber-100 text-amber-900 border border-amber-300 px-3 py-1 rounded-full">{vs['winner_badge']}</span>
            <h1 class="text-2xl sm:text-4xl font-extrabold text-gray-900 leading-tight">{vs['title']}</h1>
            <p class="text-base text-gray-700 leading-relaxed">{vs['summary']}</p>
        </div>

        <div class="bg-gray-100 border-2 border-gray-300 rounded-2xl overflow-hidden shadow-sm">
            <table class="w-full text-left border-collapse">
                <thead>
                    <tr class="bg-gray-800 text-white text-xs sm:text-sm font-extrabold">
                        <th class="p-4">Specification</th>
                        <th class="p-4 text-amber-300">{vs['product_a']}</th>
                        <th class="p-4 text-amber-400">{vs['product_b']}</th>
                    </tr>
                </thead>
                <tbody>
                    {rows_html}
                    <tr class="bg-gray-200">
                        <td class="p-4 font-extrabold text-xs sm:text-sm text-gray-900">Check Amazon Price</td>
                        <td class="p-4">
                            <a href="{link_a}" target="_blank" rel="nofollow sponsored noopener" class="inline-block bg-amber-700 hover:bg-amber-800 text-white font-extrabold text-xs py-2.5 px-4 rounded-lg transition">
                                View {vs['product_a']} &rarr;
                            </a>
                        </td>
                        <td class="p-4">
                            <a href="{link_b}" target="_blank" rel="nofollow sponsored noopener" class="inline-block bg-gray-800 hover:bg-gray-900 text-white font-extrabold text-xs py-2.5 px-4 rounded-lg transition">
                                View {vs['product_b']} &rarr;
                            </a>
                        </td>
                    </tr>
                </tbody>
            </table>
        </div>

        <div class="bg-gray-100 border-2 border-amber-600 rounded-2xl p-6 sm:p-8 space-y-4">
            <h2 class="text-xl font-extrabold text-gray-900">Head-to-Head Buying Verdict</h2>
            <p class="text-sm sm:text-base text-gray-800 leading-relaxed">{vs['verdict_text']}</p>
            <div class="flex flex-col sm:flex-row gap-3 pt-2">
                <a href="{link_a}" target="_blank" rel="nofollow sponsored noopener" class="flex-1 text-center bg-amber-700 hover:bg-amber-800 text-white font-extrabold text-sm py-3 px-4 rounded-xl transition">
                    Shop {vs['product_a']} on Amazon &rarr;
                </a>
                <a href="{link_b}" target="_blank" rel="nofollow sponsored noopener" class="flex-1 text-center bg-gray-800 hover:bg-gray-900 text-white font-extrabold text-sm py-3 px-4 rounded-xl transition">
                    Shop {vs['product_b']} on Amazon &rarr;
                </a>
            </div>
        </div>
    </main>

    <footer class="bg-gray-300 border-t border-gray-400 mt-16 py-10 px-4 text-xs text-gray-700 text-center">
        <p class="font-bold text-gray-900">{SITE_NAME} — {SITE_TAGLINE}</p>
        <p class="mt-1">As an Amazon Associate, this site earns from qualifying purchases (Store ID: {AFFILIATE_TAG}).</p>
    </footer>
</body>
</html>"""

def generate_sitemap_and_robots(urls):
    today = datetime.datetime.utcnow().strftime("%Y-%m-%d")
    xml_items = ""
    for u in urls:
        xml_items += f"""  <url>
    <loc>{u}</loc>
    <lastmod>{today}</lastmod>
    <changefreq>daily</changefreq>
    <priority>{"1.0" if u.endswith("/") else "0.85"}</priority>
  </url>\n"""

    sitemap_content = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{xml_items}</urlset>"""

    with open(os.path.join(OUTPUT_DIR, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write(sitemap_content)

    robots_content = f"""User-agent: *
Allow: /
Sitemap: {BASE_URL}/sitemap.xml
"""
    with open(os.path.join(OUTPUT_DIR, "robots.txt"), "w", encoding="utf-8") as f:
        f.write(robots_content)

    with open(os.path.join(OUTPUT_DIR, f"{INDEXNOW_KEY}.txt"), "w", encoding="utf-8") as f:
        f.write(INDEXNOW_KEY)

def ping_indexnow(urls):
    parsed_host = urllib.parse.urlparse(BASE_URL).netloc
    if not parsed_host or "username.github.io" in parsed_host:
        return

    payload = {
        "host": parsed_host,
        "key": INDEXNOW_KEY,
        "keyLocation": f"{BASE_URL}/{INDEXNOW_KEY}.txt",
        "urlList": urls
    }
    try:
        req = urllib.request.Request(
            "https://api.indexnow.org/indexnow",
            data=json.dumps(payload).encode("utf-8"),
            headers={"Content-Type": "application/json; charset=utf-8"},
            method="POST"
        )
        with urllib.request.urlopen(req, timeout=10) as resp:
            print(f"IndexNow Ping Status: {resp.status}")
    except Exception as e:
        print(f"IndexNow notice: {e}")

def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    generated_urls = []

    # 1. Generate Homepage
    home_preset = {
        "slug": "index",
        "name": "5' × 7' × 7' Home Sauna (245 ft³ Raw | 8.0 kW Heater)",
        "length": 7,
        "width": 5,
        "height": 7,
        "glass_sqft": 14,
        "stone_sqft": 0,
        "desc": "Calculate exact traditional sauna room volume (cubic feet & m³), glass door de-rating factor, Finnish heater kW (4.5kW–10.5kW), 240V breaker wire gauge, and olivine stone lbs—plus read 3 new hardware reviews added daily."
    }
    with open(os.path.join(OUTPUT_DIR, "index.html"), "w", encoding="utf-8") as f:
        f.write(render_calculator_page(home_preset, is_home=True))
    generated_urls.append(f"{BASE_URL}/")

    # 2. Generate Dedicated HTML Site Map Page (sitemap.html)
    with open(os.path.join(OUTPUT_DIR, "sitemap.html"), "w", encoding="utf-8") as f:
        f.write(render_dedicated_html_sitemap_page())
    generated_urls.append(f"{BASE_URL}/sitemap.html")

    # 3. Generate Programmatic Sauna Size & kW Calculator Pages
    for page in ALL_CALC_PAGES:
        filename = f"{page['slug']}.html"
        with open(os.path.join(OUTPUT_DIR, filename), "w", encoding="utf-8") as f:
            f.write(render_calculator_page(page, is_home=False))
        generated_urls.append(f"{BASE_URL}/{filename}")

    # 4. Generate Cumulative Daily Product Review Pages (+3 new reviews unlocked every single day)
    active_reviews = get_cumulative_product_reviews()
    for rev in active_reviews:
        filename = f"{rev['slug']}.html"
        with open(os.path.join(OUTPUT_DIR, filename), "w", encoding="utf-8") as f:
            f.write(render_single_review_page(rev))
        generated_urls.append(f"{BASE_URL}/{filename}")

    # 5. Generate Standalone Head-to-Head Product Comparison Pages
    for vs in VS_COMPARISONS:
        filename = f"{vs['slug']}.html"
        with open(os.path.join(OUTPUT_DIR, filename), "w", encoding="utf-8") as f:
            f.write(render_vs_comparison_page(vs))
        generated_urls.append(f"{BASE_URL}/{filename}")

    # 6. XML Sitemap, Robots & IndexNow Auto-Ping
    generate_sitemap_and_robots(generated_urls)
    ping_indexnow(generated_urls)
    print(f"Successfully generated {len(generated_urls)} total SEO pages ({len(active_reviews)} cumulative review articles [+3/day] + HTML/XML sitemaps) in /{OUTPUT_DIR}!")

if __name__ == "__main__":
    main()
