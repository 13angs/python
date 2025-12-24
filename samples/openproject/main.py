import json

# กำหนดชื่อไฟล์เข้าและออก
INPUT_FILE = 'users.json'        # ไฟล์ต้นฉบับที่คุณมี
OUTPUT_FILE = 'exported_users.json' # ไฟล์ปลายทางที่จะสร้างใหม่

def process_and_export_json():
    try:
        # 1. อ่านไฟล์ต้นฉบับ
        with open(INPUT_FILE, 'r', encoding='utf-8') as f_in:
            data = json.load(f_in)

        # 2. ดึงข้อมูล (Extract)
        users_raw = data.get('_embedded', {}).get('elements', [])
        cleaned_users = []

        for user in users_raw:
            cleaned_users.append({
                "id": user.get("id"),
                "name": user.get("name"),
                "email": user.get("email"),
                "login": user.get("login"),
                "status": user.get("status")
            })

        # 3. บันทึกเป็นไฟล์ JSON ใหม่ (Export)
        with open(OUTPUT_FILE, 'w', encoding='utf-8') as f_out:
            # indent=4 : จัดย่อหน้าให้สวยงาม (Pretty Print)
            # ensure_ascii=False : เพื่อให้แสดงภาษาไทยได้ถูกต้อง (ไม่เป็นรหัส \uXXXX)
            json.dump(cleaned_users, f_out, indent=4, ensure_ascii=False)

        print(f"✅ ทำงานสำเร็จ!")
        print(f"📌 บันทึกข้อมูล {len(cleaned_users)} รายการ ลงในไฟล์ '{OUTPUT_FILE}' เรียบร้อยแล้ว")

    except FileNotFoundError:
        print(f"❌ ไม่พบไฟล์ '{INPUT_FILE}' กรุณาตรวจสอบชื่อไฟล์")
    except Exception as e:
        print(f"❌ เกิดข้อผิดพลาด: {e}")

# เรียกใช้งาน
if __name__ == "__main__":
    process_and_export_json()