from cgitb import html
from flask import Flask, render_template, url_for, request

app = Flask(__name__)

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


