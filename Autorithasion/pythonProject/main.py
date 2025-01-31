from cachelib import FileSystemCache
from flask import Flask, render_template, request, flash, session, redirect, url_for
from flask_session import Session
from datetime import timedelta
import json
import sqlite3

con = sqlite3.connect('login.db', check_same_thread=False)
cursor = con.cursor()

app = Flask(__name__)
app.secret_key = '1998'
app.config['SESSION_TYPE'] = 'cachelib'
app.config['SESSION_CACHELIB'] = FileSystemCache(cache_dir='flask_session', threshold=500)
Session(app)



@app.route("/LogReg/")
def start():
    return render_template("mainPage.html")

@app.route("/register/")
def registr():
    return render_template("registration.html")


@app.route("/login/")
def login():
    return render_template("login.html")


@app.route("/save_register/", methods=['POST'])
def save_register():
    name1 = request.form['name']
    last_name1 = request.form['last_name']
    patronymic1 = request.form['patronymic']
    gender1 = request.form['gender']
    email1 = request.form['email']



    username1 = request.form['username']
    password1 = request.form['password']
    cursor.execute(
        "INSERT INTO login (name, last_name, patronymic, gender, email, username, password) VALUES (?, ?, ?, ?, ?, ?, ?)",
        (name1, last_name1, patronymic1, gender1, email1, username1, password1))
    con.commit()
    return render_template("login.html")


@app.route("/auto/", methods=['POST', 'GET'])
def result():
    if request.method == 'POST':
        username2 = request.form['username']
        password_form = request.form['password']
        cursor.execute('select password from login where username=(?)',(username2,))
        password_db = cursor.fetchall()[0][0]
        if password_db == password_form:
            session['login'] = True
            session['username'] = login
            session.permanent = False
            app.permanent_session_lifetime = timedelta(minutes=1)
            session.modified = True
            flash('Вы авторизованы', 'success')
            return redirect(url_for('main_page'))
        else:
            flash('Неверный логин или пароль', 'danger')
            return render_template("login.html")


@app.route("/add/")
def add_post():
    if 'login' not in session:
        flash('Необходимо авторизоваться', 'danger')
        return redirect(url_for('start'))
    return render_template("add.html")

@app.route("/save_post/", methods=['POST'])
def savepost():
    title = request.form['title']
    image = request.files.get('image')
    description = request.form['description']
    image.save(f'home/GoGn/first sait/Autorithasion/pythonProject/static/uploads/{image.filename}')
    file_name = f'home/GoGn/first sait/Autorithasion/pythonProject/static/uploads/{image.filename}'
    cursor.execute(
        "INSERT INTO PostTable (title, file_name, description) VALUES (?, ?, ?)",
        (title, file_name, description))
    con.commit()
    data = cursor.fetchall()
    return render_template("auto.html", data=data)


@app.route('/')
def main_page():
    cursor.execute('select * from PostTable')
    data = cursor.fetchall()
    return render_template('auto.html', data=data)

@app.route("/logout/")
def logout():
    session.clear()
    flash('Вы вышли из профиля', 'danger')
    return redirect(url_for('main_page'))
