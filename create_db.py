import sqlite3

conn = sqlite3.connect("database.db") #creates the .db file if it donot exists 
cursor = conn.cursor() # as a pen that writes SQL command in the database

cursor.execute("""
    CREATE TABLE IF NOT EXISTS coupons (                 # creates a atable if it dont exists already
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        code TEXT UNIQUE NOT NULL,     # no two coupon can have same code, and it cant be empty
        prize INTEGER NOT NULL,
        redeemed INTEGER DEFAULT 0   # every new coupons starts as non redeemed 
    )
""")

conn.commit()
conn.close()
print("✅ Database ready!")