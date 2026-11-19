# 🌾 GoodVillager Minecraft Bedrock Add-on

[![Minecraft Bedrock](https://img.shields.io/badge/Minecraft-Bedrock%201.21%2B%20--%2026.xx%2B-brightgreen.svg)](https://minecraft.net/)
[![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20iOS%20%7C%20Android%20%7C%20Console-blue.svg)]()
[![Type](https://img.shields.io/badge/Type-Behavior%20Pack-orange.svg)]()

**GoodVillager** คือ Add-on สำหรับ **Minecraft Bedrock Edition** ที่ออกแบบมาเพื่อยกระดับความสะดวกสบายในการแลกเปลี่ยน (Trading) กับชาวบ้าน ให้ผู้เล่นไม่ต้องเสียเวลาสุ่มหาของ ไม่ต้องกักตุนของเพื่อฟาร์มเลเวลชาวบ้าน และไม่ต้องหงุดหงิดกับปัญหาสินค้าหมดสต็อกอีกต่อไป!

---

## ✨ คุณสมบัติเด่น (Key Features)

### 1. 🔓 ปลดล็อคข้อเสนอทั้งหมดทันที (Instant All-Tier Unlock)
- ไม่ต้องทำการเทรดเพื่อเก็บแต้มประสบการณ์ (XP) สะสมเลเวลชาวบ้านอีกต่อไป
- ข้อเสนอแลกเปลี่ยนทั้งหมดของทุกอาชีพถูกรวบรวมไว้ที่ **Tier 1** เปิดหน้าต่างเทรดขึ้นมาจะพบรายการแลกเปลี่ยนครบทั้งหมดทันที 100%

### 2. 📚 ชาวบ้านขายทุกอย่างในอาชีพ (Complete Trade Catalog)
- ครอบคลุมชาวบ้านทั้ง **13 อาชีพปกติ** และ **Wandering Trader (พ่อค้าพเนจร)**
- **บรรณารักษ์ (Librarian):** บรรจุหนังสือเอนแชนต์ระดับสูงสุด (**Max Level**) ครบทุกเอนแชนต์ในตัวเดียว (เช่น *Mending, Unbreaking III, Fortune III, Silk Touch, Protection IV, Sharpness V, Efficiency V, Looting III ฯลฯ รวมถึงคำสาป Curse of Binding และ Curse of Vanishing*)
- **นักทำแผนที่ (Cartographer):** มีแผนที่สำรวจโครงสร้างหายากครบทั้งหมด (*Ocean Monument, Woodland Mansion, Trial Chambers*)
- **ช่างตีเกราะ & อาวุธ (Armorer / Weaponsmith / Toolsmith):** มีชุดเกราะเพชรและเครื่องมือเพชรครบทุกชิ้นให้เลือกซื้อทันที

### 3. ♾️ เทรดได้ไม่จำกัดตลอดวัน (Unlimited Trades & Flat Pricing)
- กำหนด `max_uses: 999999` ในทุกข้อเสนอ สามารถเทรดต่อเนื่องได้ไม่จำกัดจำนวนครั้ง ไม่มีสินค้าหมดสต็อก (ไม่ติดสัญลักษณ์ 'X')
- ปิดระบบ Demand / เงินเฟ้อ (`price_multiplier: 0.0`) ทำให้ราคาคงที่ถาวร ไม่มีการปรับราคาขึ้นแม้จะเทรดของชิ้นเดิมซ้ำๆ หลายพันรอบ

### 4. 💎 ปรับลดทรัพยากรลง 30–50% (Resource Discount)
- **ฝั่งซื้อของ (Buying):** จ่ายมรกต (Emeralds) หรือทรัพยากรน้อยลง 30–50% จากราคาปกติ
- **ฝั่งขายผลผลิต (Selling):** ใช้ทรัพยากร (เช่น ข้าวสาลี, ถ่านหิน, แท่งไม้, ผลผลิตฟาร์ม) น้อยลง 30–50% ในการแลกรับ 1 มรกต ช่วยให้หาเงินได้รวดเร็วและคุ้มค่า

---

## 🎮 เวอร์ชันที่รองรับ (Compatibility)

- **Minecraft Bedrock Edition:** รองรับเวอร์ชัน **1.21.xx จนถึง 26.xx+ ขึ้นไป**
- ใช้งานได้บนทุกแพลตฟอร์มที่รองรับ Bedrock Add-on (Windows, Android, iOS, Xbox, PlayStation, Nintendo Switch)

---

## 📦 วิธีการติดตั้งและใช้งาน (Installation)

1. ดาวน์โหลดไฟล์ `GoodVillager.mcpack` จากหน้า Releases หรือในโปรเจกต์
2. ดับเบิลคลิกที่ไฟล์ `GoodVillager.mcpack` เพื่อให้ตัวเกม Minecraft Bedrock เปิดและนำเข้า Add-on โดยอัตโนมัติ
3. เข้าไปที่การตั้งค่าโลกของคุณ (World Settings) -> ไปที่แท็บ **Behavior Packs**
4. เลือกเปิดใช้งาน (Activate) **GoodVillager**
5. เข้าเล่นเกมและเริ่มแลกเปลี่ยนกับชาวบ้านได้ทันที!

---

## 📂 โครงสร้างโปรเจกต์ (Project Structure)

```text
GoodVillager/
├── README.md               # รายละเอียดและคู่มือการใช้งาน Add-on
├── DESIGN_ALIGNMENT.md     # เอกสารสรุปการตัดสินใจและสถาปัตยกรรมระบบ
├── manifest.json           # การกำหนดค่า Behavior Pack และ Engine Version
├── pack_icon.png           # รูปไอคอนของ Add-on
└── trading/                # ตารางข้อมูลการแลกเปลี่ยน (Economy Trades) ของทุกอาชีพ
```

---

## 📄 ใบอนุญาตและการมีส่วนร่วม (License)
โปรเจกต์นี้พัฒนาและเผยแพร่ภายใต้ลิขสิทธิ์ Open Source สามารถนำไปปรับแต่งและใช้งานร่วมกับม็อดอื่นๆ ได้อย่างอิสระ
