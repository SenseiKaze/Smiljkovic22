import os
import sqlite3
from flask import Flask, request, jsonify, json, render_template
from flask_cors import CORS

app = Flask(__name__)

@app.route("/")
def index():
    return  render_template("index.html")

@app.route("/primer-string")
def  string():
    return "Luka Smiljkovic najjaci"

@app.route("/primer-broj")
def  broj():
    return "265"

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