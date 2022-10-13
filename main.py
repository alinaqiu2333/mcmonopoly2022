from cgitb import html
from flask import Flask, render_template, url_for, request
from mysql.connector import (connection)
import mysql.connector
from mysql.connector import errorcode
app = Flask(__name__)

try:
    cnx = mysql.connector.connect(user='root', password='Alina1116@',
                                host='127.0.0.1',
                                database='mcd_mono',auth_plugin='mysql_native_password')
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)
else:
    print("all is well")
    cnx.close()



def boo():
    d = {}
    for i in range(10):
        d[i] = str(i)*10
    return '这些图片为什么出不来呜呜呜'


@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route("/all")
def show_all():
    return render_template('all.html', data = boo())


