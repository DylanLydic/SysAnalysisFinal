from flask import Flask, request, redirect, url_for, render_template
import sqlite3 as sql
app = Flask (__name__)

@app.route("/")
def start():
    return render_template("home.htm")

@app.route("/home")
def home():
    return render_template("home.htm")

@app.route("/newproduct")
def newproduct():
    return render_template("product.htm")

@app.route("/summary")
def summary():
    return render_template("summary.htm")

@app.route("/inventory")
def listproduct():
    con = sql.connect("database.db")
    con.row_factory= sql.Row

    cur = con.cursor()
    cur.execute("SELECT * FROM Inventory")

    rows = cur.fetchall()
    return render_template("summary.htm", rows = rows)

@app.route("/newProduct/", methods = ["POST", "GET"])
def addProduct():
    if request.method == "POST":
        product = request.form["product"]
        price = request.form["price"]
        quantity = request.form["quantity"]
        checkin = request.form["checkin"]

    with sql.connect("database.db") as con:
        cur = con.cursor()
        cur.execute("INSERT INTO Inventory (product, description, quantity, checkin) VALUES ('{0}','{1}','{2}','{3}')".format(product, price, quantity, checkin))
        con.commit()

    return render_template("home.htm")





if __name__ == "__main__":
    app.run(debug=True)