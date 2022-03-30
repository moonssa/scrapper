import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template, request, redirect
from so_scrapper import get_jobs

app = Flask("SuperScrapper")

db = {}
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
        fromDB= db.get(word)
        if fromDB:
            jobs = fromDB
        else:
            jobs= get_jobs(word)
            db[word]= jobs    
    else:
        return redirect('/')
    print(word)
    return render_template("report.html", 
    searchingKey=word, 
    resultNumber=len(jobs), 
    jobs=jobs)

app.run(host="0.0.0.0") 