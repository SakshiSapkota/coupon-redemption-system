import sqlite3
import qrcode
import os

BASE_URL = "http://192.168.1.2:5000"  # as a variable — if you ever deploy this online, you only change one line instead of hunting through code
OUTPUT_DIR = "qr_codes"

os.makedirs(OUTPUT_DIR, exist_ok=True)

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

cursor.execute("SELECT code, prize FROM coupons WHERE redeemed = 0")
#only generates QR codes for unused coupons. Your original generated QRs for already-redeemed ones too!
coupons = cursor.fetchall()
conn.close()

for row in coupons:
    code, prize = row     #unpacking the row directly into variables, cleaner than row[0], row[1]
    url = f"{BASE_URL}/redeem/{code}"

    img = qrcode.make(url)
    filepath = os.path.join(OUTPUT_DIR, f"{code}.png")
    img.save(filepath)

    print(f"✅ QR saved: {filepath} | Prize: Rs.{prize}")

print(f"\n🎉 Done! {len(coupons)} QR codes generated.")