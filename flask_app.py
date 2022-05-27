
from flask import Flask, render_template,request
import sqlite3

app = Flask(__name__)

@app.route('/')

def home():
    return render_template('simpleForm.html')

@app.route('/signup',methods=['POST'])
def signup():
    con = sqlite3.connect('login.db')
    cur = con.cursor()
    cur.execute("INSERT INTO USER(username,password)VALUES (?,?)",
                    (request.form['un'],request.form['pw']))
    con.commit()
    return 'insert'




@app.route('/create')
def create():
    con = sqlite3.connect('login.db')
    cur = con.cursor()
    cur.execute("""CREATE TABLE USER(
        username VARCHAR(20) NOT NULL PRIMARY KEY,
        password VARCHAR(20) NOT NULL)
        """)
    return 'created'


@app.route('/select')
def select():
    con = sqlite3.connect('login.db')
    cur = con.cursor()
    cur.execute("SELECT * FROM user")
    rows = cur.fetchall()
    return str(rows)


@app.route('/login')
def login():
    con = sqlite3.connect('login.db')
    cur = con.cursor()
    cur.execute("SELECT * FROM user")
    rows = cur.fetchall()
    return str(rows)

