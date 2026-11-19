# Pure Economy Trade Table Override

We decided to implement GoodVillager exclusively through Bedrock's economy trade table JSON definitions (`trading/economy_trades/*.json`) without modifying or overriding the `entities/villager_v2.json` or `wandering_trader.json` entity files. This provides 100% compatibility with other entity behavior packs, custom textures, animation packs, and model overhauls, while insulating GoodVillager from breaking changes when Mojang updates entity schemas.
