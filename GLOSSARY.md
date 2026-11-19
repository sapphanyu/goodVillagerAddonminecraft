# GoodVillager Trading Domain

Domain vocabulary for the GoodVillager Minecraft Bedrock behavior pack add-on, focusing on overhauled villager trading economics and mechanics.

## Language

**GoodVillager**:
A Minecraft Bedrock Edition behavior pack add-on that modernizes villager and wandering trader economics.
_Avoid_: Mod, resource pack, server plugin

**Tier 1 Consolidation**:
The architectural pattern of flattening all villager trades across progression tiers into the initial Novice tier (Tier 1).
_Avoid_: Multi-tier trades, level progression, trade unlocking

**Economy Trade Table**:
A Minecraft Bedrock behavior pack JSON file (`trading/economy_trades/*.json`) defining villager transaction offers and costs.
_Avoid_: Loot table, trade recipe, exchange file

**Unlimited Trading**:
Trade offers configured with saturated maximum usages (`max_uses: 999999`) preventing stockouts and eliminating restocking requirements.
_Avoid_: Infinite restock, cooldown bypass

**Flat Pricing**:
Fixed trade exchange rates enforced by zeroing demand multipliers (`price_multiplier: 0.0`), preventing in-game price inflation.
_Avoid_: Static rate, locked cost

**Resource Rebalance**:
The standardized 30%–50% resource reduction applied symmetrically to purchasing costs and player selling demands.
_Avoid_: Discount curve, cheap trades

**Trade Group**:
A selection container within an economy trade tier configured with single-item selection to guarantee 100% trade availability.
_Avoid_: Trade roll, random pool

**Player Reward Experience**:
Player experience orbs awarded upon executing a trade transaction, preserved independently of villager leveling.
_Avoid_: Trader XP, villager exp
