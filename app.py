from flask import Flask
import sqlite3

app = Flask(__name__)

def get_db():     #reusable functio to get database connected
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row  # lets you access columns by name    lets you do result["prize"] instead of result[1]. Way more readable!
    return conn

@app.route("/")
def home():
    return """
        <h1>🎟️ Coupon Redemption System</h1>
        <p>Scan your QR code or visit /redeem/YOUR-CODE to redeem.</p>
    """

@app.route("/redeem/<code>")
def redeem(code):
    code = code.upper().strip()  # cleans user input. If someone types a3f9bc12 or A3F9BC12  (with a space), it still works

    conn = get_db()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT redeemed, prize FROM coupons WHERE code = ?",
        (code,)
    )
    result = cursor.fetchone()

    if result is None:
        conn.close()
        return "❌ Invalid Coupon Code.", 404   
    # these are HTTP status codes. 404 = not found, 400 = bad request, 200 = success. Proper APIs always return these!

    if result["redeemed"] == 1:
        conn.close()
        return "⚠️ This coupon has already been redeemed!", 400

    cursor.execute(
        "UPDATE coupons SET redeemed = 1 WHERE code = ?",
        (code,)
    )
    conn.commit()
    conn.close()   #before every return — always close the connection when you're done, otherwise you get memory leaks

    return f"🎉 Congratulations! You won Rs.{result['prize']}!", 200    


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")  # 0.0.0.0 means "accept from anyone"