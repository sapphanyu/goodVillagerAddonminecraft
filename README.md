# 🌾 GoodVillager Minecraft Bedrock Add-on (Version 0.2)

[![Minecraft Bedrock](https://img.shields.io/badge/Minecraft-Bedrock%201.21%2B%20--%2026.xx%2B-brightgreen.svg)](https://minecraft.net/)
[![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20iOS%20%7C%20Android%20%7C%20Console-blue.svg)]()
[![Type](https://img.shields.io/badge/Type-Behavior%20Pack-orange.svg)]()
[![Version](https://img.shields.io/badge/Release-v0.2-blue.svg)]()

**GoodVillager** คือ Add-on สำหรับ **Minecraft Bedrock Edition** ที่ออกแบบมาเพื่อยกระดับความสะดวกสบายในการแลกเปลี่ยน (Trading) กับชาวบ้าน ให้ผู้เล่นไม่ต้องเสียเวลาสุ่มหาของ ไม่ต้องกักตุนของเพื่อฟาร์มเลเวลชาวบ้านนานๆ และไม่ต้องหงุดหงิดกับปัญหาสินค้าหมดสต็อกอีกต่อไป!

---

## ✨ คุณสมบัติเด่นในเวอร์ชัน 0.2 (Version 0.2 Highlights)

### 1. ⚡ One-Trade Leveling (เทรด 1 ครั้งเลเวลอัปทันที)
- หมดปัญหาการเทรดซ้ำซากเพื่อฟาร์มเลเวล! ทุกการแลกเปลี่ยนให้ `trader_exp: 10` ซึ่งสอดคล้องกับเกณฑ์เลเวล `[0, 10, 20, 30, 40]`
- ผู้เล่นเทรดเพียง **1 ครั้ง** ที่เลเวลใดก็ตาม ชาวบ้านจะเลื่อนขั้นไปยังเลเวลถัดไปทันที (Novice -> Apprentice -> Journeyman -> Expert -> Master)

### 2. 📖 จัดระเบียบเอนแชนต์บรรณารักษ์ 5 หมวดหมู่ (Categorized Librarian Enchants)
แบ่งหนังสือเอนแชนต์ระดับสูงสุด (Max Level) ทั้ง 36 ชนิดลงใน 5 เลเวลอย่างเป็นระเบียบ ค้นหาง่าย สบายตา และการันตีออกครบ 100%:
- **Tier 1 (Novice) - เครื่องมือ & ประโยชน์ทั่วไป:** *Efficiency V, Silk Touch, Unbreaking III, Fortune III* (พร้อมขาย Paper, Book, Ink Sac, Bookshelf, Lantern, Glass)
- **Tier 2 (Apprentice) - ป้องกันชุดเกราะ:** *Protection IV, Fire Protection IV, Blast Protection IV, Projectile Protection IV, Feather Falling IV, Respiration III, Aqua Affinity* (พร้อม Compass)
- **Tier 3 (Journeyman) - อาวุธประชิด & ดาบ:** *Sharpness V, Smite V, Bane of Arthropods V, Knockback II, Fire Aspect II, Looting III* (พร้อม Clock)
- **Tier 4 (Expert) - อาวุธยิง & ตรีศูล:** *Power V, Punch II, Flame, Infinity, Quick Charge III, Multishot, Piercing IV, Loyalty III, Riptide III, Channeling, Impaling V, Luck of the Sea III, Lure III*
- **Tier 5 (Master) - Endgame, เคลื่อนที่ & คำสาป:** *Mending, Depth Strider III, Frost Walker II, Thorns III, Curse of Binding, Curse of Vanishing* (พร้อม Name Tag)

### 3. 🎯 การันตีออกครบ 100% ทุกเทียร์ (100% Guaranteed Catalog)
- แต่ละเทียร์ของการเทรดจะแสดงรายการแลกเปลี่ยนครบทุกชิ้น ไม่มีการสุ่มตัดบางรายการออก
- ผู้เล่นไม่ต้องทุบโต๊ะทำงานเพื่อสุ่มหาของที่ต้องการอีกต่อไป

### 4. ♾️ เทรดได้ไม่จำกัด & ราคาคงที่ (Unlimited Trades & Flat Pricing)
- กำหนด `max_uses: 999999` ในทุกข้อเสนอ สามารถเทรดต่อเนื่องได้ไม่จำกัด ไม่มีสินค้าหมดสต็อก
- ปิดระบบ Demand / เงินเฟ้อ (`price_multiplier: 0.0`) ทำให้ราคาคงที่ถาวร ไม่มีการปรับราคาขึ้น

### 5. 💎 ปรับลดทรัพยากร 40–50% (Resource Discount)
- **ฝั่งซื้อของ (Buying):** จ่ายมรกต (Emeralds) หรือทรัพยากรน้อยลง 40–50% จากราคาปกติ
- **ฝั่งขายผลผลิต (Selling):** ใช้ผลผลิตน้อยลง 40–50% ในการแลกรับ 1 มรกต ช่วยให้ตั้งตัวได้รวดเร็ว

---

## 🎮 เวอร์ชันที่รองรับ (Compatibility)

- **Minecraft Bedrock Edition:** รองรับเวอร์ชัน **1.21.xx จนถึง 26.xx+ ขึ้นไป**
- ใช้งานได้บนทุกแพลตฟอร์มที่รองรับ Bedrock Add-on (Windows, Android, iOS, Xbox, PlayStation, Nintendo Switch)

---

## 📦 วิธีการติดตั้งและใช้งาน (Installation)

คุณสามารถเลือกดาวน์โหลดไฟล์ติดตั้งได้ 2 รูปแบบตามความสะดวก:
1. **`GoodVillager.mcaddon` (แนะนำ):** เป็นไฟล์ Bundle มาตรฐานสากลสำหรับ Bedrock Add-on ดับเบิลคลิกเพื่อติดตั้งแพ็กเกจทั้งหมดเข้าตัวเกมทันที
2. **`GoodVillager.mcpack`:** สำหรับติดตั้ง Behavior Pack เดี่ยว

**ขั้นตอนการเปิดใช้งานในเกม:**
1. ดับเบิลคลิกที่ไฟล์ `.mcaddon` หรือ `.mcpack` เพื่อให้ Minecraft นำเข้าอัตโนมัติ
2. เปิดการตั้งค่าโลกของคุณ (World Settings) ➔ ไปที่แท็บ **Behavior Packs**
3. เลือกเปิดใช้งาน (Activate) **GoodVillager**
4. เข้าเล่นเกมและเริ่มเทรดได้ทันที!

---

## 📂 โครงสร้างโปรเจกต์ (Project Structure)

```text
GoodVillager/
├── README.md               # รายละเอียดและคู่มือการใช้งาน Add-on
├── DESIGN_ALIGNMENT.md     # เอกสารสรุปการตัดสินใจและสถาปัตยกรรมระบบ
├── GLOSSARY.md             # นิยามคำศัพท์และขอบเขตโดเมนของโปรเจกต์
├── docs/adr/               # Architecture Decision Records (ADRs)
├── manifest.json           # การกำหนดค่า Behavior Pack และ Engine Version
├── pack_icon.png           # รูปไอคอนของ Add-on
├── GoodVillager.mcaddon     # ไฟล์ติดตั้งสำเร็จรูป One-Click Add-on Bundle
├── GoodVillager.mcpack     # ไฟล์ติดตั้งสำเร็จรูป One-Click Pack
├── tools/
│   └── build_addon.py      # สคริปต์อัตโนมัติสร้างและคอมไพล์ตารางเทรดพร้อมแพ็กเกจ
└── trading/                # ตารางข้อมูลการแลกเปลี่ยน (Economy Trades) ของทุกอาชีพ
    └── economy_trades/
```

---

## 📄 ใบอนุญาตและการมีส่วนร่วม (License)
โปรเจกต์นี้พัฒนาและเผยแพร่ภายใต้ลิขสิทธิ์ Open Source สามารถนำไปปรับแต่งและใช้งานร่วมกับม็อดอื่นๆ ได้อย่างอิสระ
