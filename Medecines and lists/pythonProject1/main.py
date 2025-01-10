from flask import Flask, render_template, request
import json
import sqlite3
app = Flask(__name__)

@app.route("/")
def loginn():
    return render_template("login.html")
@app.route("/regestration/")
def registr():
    YourName = request.args.get("name")
    age = request.args.get("age")
    choice_tv = request.args.get("med1")
    choice_chid = request.args.get("med2")
    choice_ma = request.args.get("med3")
    choice_kap = request.args.get("med4")
    return render_template("registration.html")

@app.route("/main/")
def login():
    return render_template("main_page.html")

#@app.route("/find/")
#def search_page():
#    return render_template("BaseList.html")
#
#@app.route("/result_find/")
#def find_page():
#    NMed = request.args.get("name")
#    return render_template("result.html", NMed= NMed)

app.run(debug=True)