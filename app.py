from flask import Flask, render_template, request
import pandas as pd
import pickle
import sklearn


app = Flask(__name__)

@app.route("/")
def welcome():
    return render_template("index.html")

@app.route("/predictor", methods = ["GET", "POST"])
def predictor():
    return render_template("predictor.html")

@app.route("/aboutUs")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug = True)