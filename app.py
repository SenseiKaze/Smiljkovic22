import os
import sqlite3
from flask import Flask, request, jsonify, json, render_template
from flask_cors import CORS

app = Flask(__name__)

@app.route("/")
def index():
    nazivSpiska = "Spisak restorana"
    spisakRestorana = ["Pastica","Pica Tim","HasHub","Sahara"]
    return  render_template("index.html", naziv=nazivSpiska, spisak=spisakRestorana)

@app.route("/restorani")
def  restorani():
    nazivRestorana = "Spisak restorana"
    spisakRestorani = ["Pastica","Pica Tim","HasHub","Sahara"]
    return  render_template("restorani.html", naziv=nazivRestorana, spisak=spisakRestorani)

@app.route("/restorani/1")
def  meni():
    nazivMeni = "Meni restorana"
    spisakMeni = ["Pastica","Pica Tim","HasHub","Sahara"]
    return  render_template("meno.html", naziv=nazivMeni, spisak=spisakMeni)

@app.route("/primer-niz")
def  niz():
    nekiNiz = [1,2,3,4,5]
    return nekiNiz

@app.route("/primer-json")
def  primerJson():
    data = {"message":"This is a JSON response","status":"success"}
    return jsonify(data)

@app.route("/primer-html")
def  primerHTML():
    data = """<!DOCTYPE hmtl>
    <html lang="en">
    <head>
    <meta charset="UTF-8">
    <meta name="viewport" contet="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
    <link rel="stylesheet" href=:static/style.css">
    </head>
    <body>
        <h1>Zdravo budale<h1>
    </body>
    </html>"""
    return data

  
if __name__== "__main__":
    app.run()                                          