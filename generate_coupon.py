import sqlite3
import uuid
import random

PRIZES = [50, 100, 200, 500,"try again","one more"]  # different prize amounts

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

for i in range(10):  # generate 10 coupons
    code = uuid.uuid4().hex[:8].upper()  # e.g. "A3F9BC12"
    prize = random.choice(PRIZES)        # picks the random prize from the list so that each coupon vhave differnt prize

    try:
        cursor.execute(
            "INSERT INTO coupons (code, prize) VALUES (?, ?)",
            (code, prize)
        )
        print(f"✅ Created coupon: {code} | Prize: Rs.{prize}")
    except sqlite3.IntegrityError:    # if by some condition two code are identical,it skips it instead of charsh out
        print(f"⚠️ Duplicate code skipped: {code}")

conn.commit()
conn.close()

"""
uuid.uuid4.hex[:8].upper() :- uuid generated a random unique 
.hex :- converts its to plain text + number
[:8] :-takes firat 8 characters
.upper() :- makes look clean like "A3F9BC12"
"""