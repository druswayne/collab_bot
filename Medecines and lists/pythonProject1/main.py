from flask import Flask, render_template, request
import json
import sqlite3
con = sqlite3.connect('Задание 1.db', check_same_thread=False)
cursor = con.cursor()
app = Flask(__name__)


@app.route("/")
def page_medecines():
    cursor.execute('SELECT * from medicines')
    data = cursor.fetchall()
    return render_template("list.html", data= data)

@app.route("/find/")
def search_page():
    return render_template("BaseList.html")

@app.route("/result_find/")
def find_page():
    name = request.args.get("name")
    return f"Вы искали {name}"

app.run(debug=True)