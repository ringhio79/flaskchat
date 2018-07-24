from flask import Flask, request, render_template, redirect
import os

app = Flask(__name__)

chat_history=[
    "Bruce: hello how are you?",
    "Tori: good thank you and you?",
    "Bruce: let's go have lunch"
    ]

@app.route("/")
def show_hi():
    return render_template("index.html", chat_history=chat_history)

@app.route("/add", methods=['POST'])
def add_item():
    message = request.form["message"]
    chat_history.append(message)
    return redirect("/")


if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8080, debug=True)