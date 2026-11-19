"""
GoodVillager Trade Table Generator & Pack Builder - Version 0.2
- Reorganizes trades into logical 5-tier progression
- Implements "One-Trade Leveling":
    total_exp_required: [0, 10, 20, 30, 40]
    trader_exp: 10 on all trades (1 trade = instant level up to next tier)
- Categorizes Librarian enchantments into 5 clean equipment categories
- Guaranteed 100% catalog availability per tier (num_to_select: 1 per group)
- max_uses: 999999, price_multiplier: 0.0, reward_exp: true
- 40-50% resource rebalance
- Wandering Trader retains single-tier full catalog
"""

import os
import json
import re
import urllib.request
import zipfile
from PIL import Image, ImageDraw, ImageFont

BASE_URL = "https://raw.githubusercontent.com/Mojang/bedrock-samples/main/behavior_pack/trading/economy_trades/"
OUTPUT_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "trading", "economy_trades")

FILES = [
    "armorer_trades.json",
    "butcher_trades.json",
    "cartographer_trades.json",
    "cleric_trades.json",
    "farmer_trades.json",
    "fisherman_trades.json",
    "fletcher_trades.json",
    "leather_worker_trades.json",
    "librarian_trades.json",
    "shepherd_trades.json",
    "stone_mason_trades.json",
    "tool_smith_trades.json",
    "wandering_trader_trades.json",
    "weapon_smith_trades.json"
]

TIER_EXP_THRESHOLDS = [0, 10, 20, 30, 40]

# Librarian Categorization for 5 Tiers
LIBRARIAN_TIERS = {
    0: {  # Tier 1 (Novice): Tools & General Utility
        "items_sell": [
            ("minecraft:paper", 12),
            ("minecraft:book", 2),
            ("minecraft:ink_sac", 3)
        ],
        "items_buy": [
            ("minecraft:bookshelf", 4, 1),
            ("minecraft:lantern", 1, 1),
            ("minecraft:glass", 1, 4)
        ],
        "enchants": [
            ("efficiency", 5, 10),
            ("silk_touch", 1, 8),
            ("unbreaking", 3, 10),
            ("fortune", 3, 10)
        ]
    },
    1: {  # Tier 2 (Apprentice): Armor Defense
        "items_sell": [],
        "items_buy": [
            ("minecraft:compass", 2, 1)
        ],
        "enchants": [
            ("protection", 4, 10),
            ("fire_protection", 4, 8),
            ("feather_falling", 4, 10),
            ("blast_protection", 4, 8),
            ("projectile_protection", 4, 8),
            ("respiration", 3, 8),
            ("aqua_affinity", 1, 7)
        ]
    },
    2: {  # Tier 3 (Journeyman): Melee Weapons & Swords
        "items_sell": [],
        "items_buy": [
            ("minecraft:clock", 3, 1)
        ],
        "enchants": [
            ("sharpness", 5, 10),
            ("smite", 5, 8),
            ("bane_of_arthropods", 5, 6),
            ("knockback", 2, 6),
            ("fire_aspect", 2, 8),
            ("looting", 3, 10)
        ]
    },
    3: {  # Tier 4 (Expert): Ranged Weapons & Trident
        "items_sell": [],
        "items_buy": [],
        "enchants": [
            ("power", 5, 10),
            ("punch", 2, 6),
            ("flame", 1, 8),
            ("infinity", 1, 10),
            ("multishot", 1, 7),
            ("quick_charge", 3, 8),
            ("piercing", 4, 8),
            ("luck_of_the_sea", 3, 8),
            ("lure", 3, 8),
            ("loyalty", 3, 8),
            ("impaling", 5, 8),
            ("riptide", 3, 8),
            ("channeling", 1, 8)
        ]
    },
    4: {  # Tier 5 (Master): Endgame, Mobility & Curses
        "items_sell": [],
        "items_buy": [
            ("minecraft:name_tag", 10, 1)
        ],
        "enchants": [
            ("mending", 1, 10),
            ("depth_strider", 3, 8),
            ("frost_walker", 2, 8),
            ("thorns", 3, 10),
            ("binding", 1, 5),
            ("vanishing", 1, 5)
        ]
    }
}

def strip_json_comments(text):
    text = re.sub(r'//.*', '', text)
    text = re.sub(r'/\*[\s\S]*?\*/', '', text)
    text = re.sub(r',\s*([\]}])', r'\1', text)
    return text

def discount_quantity(qty):
    if isinstance(qty, dict):
        q_min = qty.get("min", 1)
        q_max = qty.get("max", 1)
        new_min = max(1, int(round(q_min * 0.55)))
        new_max = max(new_min, int(round(q_max * 0.55)))
        if new_min == new_max:
            return new_min
        return {"min": new_min, "max": new_max}
    elif isinstance(qty, (int, float)):
        val = int(qty)
        if val <= 1:
            return 1
        return max(1, int(round(val * 0.55)))
    return qty

def process_trade(trade):
    new_trade = {}
    
    # Process wants
    wants = []
    for want in trade.get("wants", []):
        w = dict(want)
        w["price_multiplier"] = 0.0
        if "quantity" in w:
            w["quantity"] = discount_quantity(w["quantity"])
        wants.append(w)
    new_trade["wants"] = wants

    # Process gives
    gives = []
    for give in trade.get("gives", []):
        if "choice" in give:
            for choice in give["choice"]:
                c = dict(choice)
                if "filters" in c:
                    del c["filters"]
                gives.append(c)
        else:
            g = dict(give)
            if "filters" in g:
                del g["filters"]
            gives.append(g)
    new_trade["gives"] = gives

    new_trade["max_uses"] = 999999
    new_trade["trader_exp"] = 10  # One-Trade Leveling: 10 XP advances to next tier
    new_trade["reward_exp"] = True

    return new_trade

def generate_librarian_trades():
    tiers = []

    for tier_idx in range(5):
        cfg = LIBRARIAN_TIERS[tier_idx]
        trades = []

        # Items sold to villager
        for item, qty in cfg["items_sell"]:
            trades.append({
                "wants": [{"item": item, "quantity": qty, "price_multiplier": 0.0}],
                "gives": [{"item": "minecraft:emerald", "quantity": 1}],
                "max_uses": 999999, "trader_exp": 10, "reward_exp": True
            })

        # Items bought from villager
        for item, cost, give_qty in cfg["items_buy"]:
            trades.append({
                "wants": [{"item": "minecraft:emerald", "quantity": cost, "price_multiplier": 0.0}],
                "gives": [{"item": item, "quantity": give_qty}],
                "max_uses": 999999, "trader_exp": 10, "reward_exp": True
            })

        # Enchanted books for this category
        for enc_id, lvl, cost in cfg["enchants"]:
            trades.append({
                "wants": [
                    {"item": "minecraft:emerald", "quantity": cost, "price_multiplier": 0.0},
                    {"item": "minecraft:book", "quantity": 1, "price_multiplier": 0.0}
                ],
                "gives": [
                    {
                        "item": "minecraft:enchanted_book",
                        "quantity": 1,
                        "functions": [
                            {
                                "function": "specific_enchants",
                                "enchants": [
                                    {
                                        "id": enc_id,
                                        "level": [lvl, lvl]
                                    }
                                ]
                            }
                        ]
                    }
                ],
                "max_uses": 999999,
                "trader_exp": 10,
                "reward_exp": True
            })

        groups = [{"num_to_select": 1, "trades": [t]} for t in trades]
        tiers.append({
            "total_exp_required": TIER_EXP_THRESHOLDS[tier_idx],
            "groups": groups
        })

    return {"tiers": tiers}

def generate_cartographer_trades(vanilla_data):
    tiers = []
    
    # Tier 1 (Novice): Paper, Empty Map
    t1_trades = [
        {
            "wants": [{"item": "minecraft:paper", "quantity": 12, "price_multiplier": 0.0}],
            "gives": [{"item": "minecraft:emerald", "quantity": 1}],
            "max_uses": 999999, "trader_exp": 10, "reward_exp": True
        },
        {
            "wants": [{"item": "minecraft:emerald", "quantity": 4, "price_multiplier": 0.0}],
            "gives": [{"item": "minecraft:empty_map", "quantity": 1}],
            "max_uses": 999999, "trader_exp": 10, "reward_exp": True
        }
    ]
    tiers.append({"total_exp_required": 0, "groups": [{"num_to_select": 1, "trades": [t]} for t in t1_trades]})

    # Tier 2 (Apprentice): Glass Pane, Ocean Monument Explorer Map
    t2_trades = [
        {
            "wants": [{"item": "minecraft:glass_pane", "quantity": 6, "price_multiplier": 0.0}],
            "gives": [{"item": "minecraft:emerald", "quantity": 1}],
            "max_uses": 999999, "trader_exp": 10, "reward_exp": True
        },
        {
            "wants": [
                {"item": "minecraft:emerald", "quantity": 7, "price_multiplier": 0.0},
                {"item": "minecraft:compass", "quantity": 1, "price_multiplier": 0.0}
            ],
            "gives": [{
                "item": "minecraft:map", "quantity": 1,
                "functions": [{"function": "exploration_map", "destination": "monument"}]
            }],
            "max_uses": 999999, "trader_exp": 10, "reward_exp": True
        }
    ]
    tiers.append({"total_exp_required": 10, "groups": [{"num_to_select": 1, "trades": [t]} for t in t2_trades]})

    # Tier 3 (Journeyman): Compass, Woodland Mansion & Trial Chambers Explorer Maps
    t3_trades = [
        {
            "wants": [{"item": "minecraft:compass", "quantity": 1, "price_multiplier": 0.0}],
            "gives": [{"item": "minecraft:emerald", "quantity": 1}],
            "max_uses": 999999, "trader_exp": 10, "reward_exp": True
        },
        {
            "wants": [
                {"item": "minecraft:emerald", "quantity": 8, "price_multiplier": 0.0},
                {"item": "minecraft:compass", "quantity": 1, "price_multiplier": 0.0}
            ],
            "gives": [{
                "item": "minecraft:map", "quantity": 1,
                "functions": [{"function": "exploration_map", "destination": "mansion"}]
            }],
            "max_uses": 999999, "trader_exp": 10, "reward_exp": True
        },
        {
            "wants": [
                {"item": "minecraft:emerald", "quantity": 7, "price_multiplier": 0.0},
                {"item": "minecraft:compass", "quantity": 1, "price_multiplier": 0.0}
            ],
            "gives": [{
                "item": "minecraft:map", "quantity": 1,
                "functions": [{"function": "exploration_map", "destination": "trial_chambers"}]
            }],
            "max_uses": 999999, "trader_exp": 10, "reward_exp": True
        }
    ]
    tiers.append({"total_exp_required": 20, "groups": [{"num_to_select": 1, "trades": [t]} for t in t3_trades]})

    # Tier 4 (Expert): Item Frame, Village/Structure Maps
    t4_trades = [
        {
            "wants": [{"item": "minecraft:emerald", "quantity": 3, "price_multiplier": 0.0}],
            "gives": [{"item": "minecraft:frame", "quantity": 1}],
            "max_uses": 999999, "trader_exp": 10, "reward_exp": True
        },
        {
            "wants": [
                {"item": "minecraft:emerald", "quantity": 6, "price_multiplier": 0.0},
                {"item": "minecraft:compass", "quantity": 1, "price_multiplier": 0.0}
            ],
            "gives": [{
                "item": "minecraft:map", "quantity": 1,
                "functions": [{"function": "exploration_map", "destination": "jungle_temple"}]
            }],
            "max_uses": 999999, "trader_exp": 10, "reward_exp": True
        },
        {
            "wants": [
                {"item": "minecraft:emerald", "quantity": 6, "price_multiplier": 0.0},
                {"item": "minecraft:compass", "quantity": 1, "price_multiplier": 0.0}
            ],
            "gives": [{
                "item": "minecraft:map", "quantity": 1,
                "functions": [{"function": "exploration_map", "destination": "swamp_hut"}]
            }],
            "max_uses": 999999, "trader_exp": 10, "reward_exp": True
        }
    ]
    tiers.append({"total_exp_required": 30, "groups": [{"num_to_select": 1, "trades": [t]} for t in t4_trades]})

    # Tier 5 (Master): Globe Banner Pattern
    t5_trades = [
        {
            "wants": [{"item": "minecraft:emerald", "quantity": 4, "price_multiplier": 0.0}],
            "gives": [{"item": "minecraft:globe_banner_pattern", "quantity": 1}],
            "max_uses": 999999, "trader_exp": 10, "reward_exp": True
        }
    ]
    tiers.append({"total_exp_required": 40, "groups": [{"num_to_select": 1, "trades": [t]} for t in t5_trades]})

    return {"tiers": tiers}

def transform_file(filename):
    print(f"Processing {filename}...")
    if filename == "librarian_trades.json":
        return generate_librarian_trades()

    url = BASE_URL + filename
    raw = urllib.request.urlopen(url).read().decode('utf-8')
    clean = strip_json_comments(raw)
    vanilla_data = json.loads(clean)

    if filename == "cartographer_trades.json":
        return generate_cartographer_trades(vanilla_data)

    if filename == "wandering_trader_trades.json":
        # Wandering trader has 1 tier, no leveling
        all_trades = []
        seen_sigs = set()
        for tier in vanilla_data.get("tiers", []):
            for group in tier.get("groups", []):
                for trade in group.get("trades", []):
                    pt = process_trade(trade)
                    pt["trader_exp"] = 0  # No leveling for wandering trader
                    if len(pt["gives"]) > 1:
                        for g_item in pt["gives"]:
                            single_trade = dict(pt)
                            single_trade["gives"] = [g_item]
                            sig = json.dumps([single_trade["wants"], single_trade["gives"]], sort_keys=True)
                            if sig not in seen_sigs:
                                seen_sigs.add(sig)
                                all_trades.append(single_trade)
                    else:
                        sig = json.dumps([pt["wants"], pt["gives"]], sort_keys=True)
                        if sig not in seen_sigs:
                            seen_sigs.add(sig)
                            all_trades.append(pt)
        groups = [{"num_to_select": 1, "trades": [t]} for t in all_trades]
        return {"tiers": [{"total_exp_required": 0, "groups": groups}]}

    # Standard 5-tier villager professions
    out_tiers = []
    vanilla_tiers = vanilla_data.get("tiers", [])

    for tier_idx in range(len(vanilla_tiers)):
        v_tier = vanilla_tiers[tier_idx]
        exp_req = TIER_EXP_THRESHOLDS[tier_idx] if tier_idx < len(TIER_EXP_THRESHOLDS) else tier_idx * 10
        tier_trades = []
        seen_sigs = set()

        for group in v_tier.get("groups", []):
            for trade in group.get("trades", []):
                pt = process_trade(trade)
                if len(pt["gives"]) > 1:
                    for g_item in pt["gives"]:
                        single_trade = dict(pt)
                        single_trade["gives"] = [g_item]
                        sig = json.dumps([single_trade["wants"], single_trade["gives"]], sort_keys=True)
                        if sig not in seen_sigs:
                            seen_sigs.add(sig)
                            tier_trades.append(single_trade)
                else:
                    sig = json.dumps([pt["wants"], pt["gives"]], sort_keys=True)
                    if sig not in seen_sigs:
                        seen_sigs.add(sig)
                        tier_trades.append(pt)

        tier_groups = [{"num_to_select": 1, "trades": [t]} for t in tier_trades]
        out_tiers.append({
            "total_exp_required": exp_req,
            "groups": tier_groups
        })

    return {"tiers": out_tiers}

def generate_pack_icon(output_path):
    img = Image.new("RGBA", (256, 256), color=(34, 139, 34))
    draw = ImageDraw.Draw(img)

    # Outer border
    draw.rectangle([0, 0, 255, 255], outline=(20, 90, 20), width=6)
    draw.rectangle([8, 8, 247, 247], fill=(46, 125, 50))
    draw.rectangle([16, 16, 239, 239], fill=(27, 94, 32))

    # Emerald icon representation (Center Diamond shape)
    emerald_pts = [(128, 45), (195, 128), (128, 210), (61, 128)]
    draw.polygon(emerald_pts, fill=(0, 230, 118), outline=(0, 200, 83))
    
    # Inner emerald facets
    inner_pts = [(128, 65), (175, 128), (128, 190), (81, 128)]
    draw.polygon(inner_pts, fill=(105, 240, 174), outline=(0, 230, 118))
    
    # Center highlight
    center_pts = [(128, 85), (155, 128), (128, 170), (101, 128)]
    draw.polygon(center_pts, fill=(185, 246, 202))

    # Text banner at bottom: v0.2
    draw.rectangle([20, 190, 236, 235], fill=(0, 0, 0, 190))
    try:
        font = ImageFont.load_default()
        draw.text((35, 202), "GOOD VILLAGER v0.2", fill=(255, 255, 255), font=font)
    except Exception:
        pass

    img.save(output_path, "PNG")
    print(f"Generated {output_path}")

def package_mcpack(workspace_dir, output_mcpack):
    with zipfile.ZipFile(output_mcpack, 'w', zipfile.ZIP_DEFLATED) as zf:
        manifest_path = os.path.join(workspace_dir, "manifest.json")
        zf.write(manifest_path, "manifest.json")

        icon_path = os.path.join(workspace_dir, "pack_icon.png")
        if os.path.exists(icon_path):
            zf.write(icon_path, "pack_icon.png")

        trading_dir = os.path.join(workspace_dir, "trading")
        for root, _, files in os.walk(trading_dir):
            for file in files:
                abs_path = os.path.join(root, file)
                rel_path = os.path.relpath(abs_path, workspace_dir)
                zf.write(abs_path, rel_path)

    print(f"Created {output_mcpack} successfully!")

def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    workspace_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # Process all files
    for filename in FILES:
        result = transform_file(filename)
        out_path = os.path.join(OUTPUT_DIR, filename)
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(result, f, indent=2, ensure_ascii=False)
        tiers_summary = ", ".join(f"T{i+1}:{len(t['groups'])}" for i, t in enumerate(result['tiers']))
        print(f"Saved {out_path} ({tiers_summary})")

    # Also save mason_trades.json alias for stone_mason_trades.json
    stone_mason_path = os.path.join(OUTPUT_DIR, "stone_mason_trades.json")
    mason_path = os.path.join(OUTPUT_DIR, "mason_trades.json")
    with open(stone_mason_path, "r", encoding="utf-8") as src, open(mason_path, "w", encoding="utf-8") as dst:
        dst.write(src.read())
    print("Saved mason_trades.json (alias for stone_mason_trades.json)")

    # Update manifest.json version to 0.2.0
    manifest_path = os.path.join(workspace_dir, "manifest.json")
    with open(manifest_path, "r", encoding="utf-8") as f:
        manifest = json.load(f)
    manifest["header"]["version"] = [0, 2, 0]
    manifest["header"]["description"] = "GoodVillager v0.2: Categorized 5-tier progression with One-Trade Leveling, 100% catalog availability, and flat 40-50% discounts."
    manifest["modules"][0]["version"] = [0, 2, 0]
    with open(manifest_path, "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2, ensure_ascii=False)
    print("Updated manifest.json to version 0.2.0")

    # Generate pack_icon.png
    icon_path = os.path.join(workspace_dir, "pack_icon.png")
    generate_pack_icon(icon_path)

    # Package into GoodVillager.mcpack
    mcpack_path = os.path.join(workspace_dir, "GoodVillager.mcpack")
    package_mcpack(workspace_dir, mcpack_path)

    print("\nAll files for Version 0.2 built and packaged successfully!")

if __name__ == "__main__":
    main()
