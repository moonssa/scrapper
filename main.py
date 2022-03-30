import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template, request, redirect
from so_scrapper import get_jobs

app = Flask("SuperScrapper")

@app.route("/")
def home():
    return render_template("potato.html")

@app.route("/<username>")
def potato(username):
    return "<h1> 안녕 반가워 ${username}</h1>"

@app.route("/report")
def report():
    
    word = request.args.get('word')
    if word:
        word=word.lower()
        get_jobs(word)
    else:
        return redirect('/')
    print(word)
    return render_template("report.html", searchingKey=word)

app.run(host="0.0.0.0") 