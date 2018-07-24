from flask import Flask, request, render_template, redirect
import os

app = Flask(__name__)

@app.route("/")
def show_hi():
    return "Hi"

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8080, debug=True)