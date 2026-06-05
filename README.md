what is this

a small but complete web system where you can generate coupon codes, turn them into QR codes, and redeem them through a browser. scan the QR, hit a URL, win a prize. each coupon can only be redeemed once.
it's not a toy project — it has a real database, a real web server, real QR codes, and actual logic to prevent double redemption.


how it works (the big picture)

generate coupons → generate QR codes → someone scans → Flask checks the database → prize or rejection

that's the whole flow. five files, each doing one job cleanly.


the files

create_db.py — sets up the database. creates a coupons table with four columns: id, code, prize, and whether it's been redeemed. run this once before anything else.

generate_coupon.py — creates 10 random coupon codes (like A3F9BC12) and assigns each one a random prize from a list. saves them all to the database. every code is unique.

generate_qr.py — looks up all unused coupons from the database and generates a QR code image for each one. each QR code points to a URL like http://yourserver/redeem/A3F9BC12. saves them as .png files in a qr_codes/ folder.
app.py — the web server. has two pages:


/ — home page, basic instructions

/redeem/CODE — where the magic happens. checks if the code exists, checks if it's already been used, marks it as redeemed, and returns the prize. returns proper error messages if something's wrong.

database.db — the SQLite database file. gets created automatically when you run create_db.py.


how to run this

step 1 — install the libraries

bashpip install flask qrcode[pil]

step 2 — set up the database

bashpython create_db.py

step 3 — generate coupons

bashpython generate_coupon.py

step 4 — start the web server

bashpython app.py

step 5 — generate QR codes

open generate_qr.py and change this line to your actual local IP address:

pythonBASE_URL = "your ip_configuration"

not sure what your IP is? run ipconfig on Windows or ifconfig on Mac/Linux and look for your local IP. then run:

bashpython generate_qr.py

your QR codes will appear in a folder called qr_codes/. print them or open them and scan with your phone — make sure your phone is on the same wifi network as your laptop.


what you'll learn from this code


SQLite — how to create a database, insert rows, query them, and update them from Python

Flask — how to build a simple web server with routes that respond to URLs

UUID — how to generate random unique codes that don't repeat

QR codes — how to turn a URL into a scannable image programmatically

HTTP status codes — why 404 means not found and 200 means success and why APIs use these


folder structure

📂 coupon-redemption-system

 ├── app.py               # web server
 
 ├── create_db.py         # database setup
 
 ├── generate_coupon.py   # coupon generator
 
 ├── generate_qr.py       # QR code generator
 
 ├── database.db          # created automatically
 
 └── 📂 qr_codes/         # created automatically
      
      ├── A3F9BC12.png
      
      ├── B7D2EF45.png
      
      └── ...
