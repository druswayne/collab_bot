from flask import Flask, render_template, request
import json
import sqlite3
con = sqlite3.connect('Задание 1.db', check_same_thread=False)
cursor = con.cursor()
app = Flask(__name__)
cursor.execute('SELECT * from medicines')
data = cursor.fetchall()

@app.route("/regestration/")
def registr():
    global YourName
    YourName = request.args.get("name")
    age = request.args.get("age")
    choice_tv = request.args.get("med1")
    choice_chid = request.args.get("med2")
    choice_ma = request.args.get("med3")
    choice_kap = request.args.get("med4")
    return render_template("registration.html")
@app.route("/")
def page_medecines():
    return render_template("list.html", data= data, name= YourName)

@app.route("/find/")
def search_page():
    return render_template("BaseList.html")

@app.route("/result_find/")
def find_page():
    NMed = request.args.get("name")
    return render_template("result.html", NMed= NMed)

app.run(debug=True)