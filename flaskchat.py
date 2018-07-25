from flask import Flask, request, render_template, redirect
import os

app = Flask(__name__)

chat_history=[]
    
tag = []

@app.route("/")
def show_join():
    return render_template("join.html")
    
@app.route("/join")
def do_join():
    username = request.args['username']
    return redirect("/chat/" + username)

def can_view(message, username):
        addressed_to_me = "@" + username in message
        addressed_to_nobody = "@" not in message
        i_wrote_it = message.startswith(username + ":")
        return addressed_to_me or addressed_to_nobody or i_wrote_it


@app.route("/chat/<username>")
def show_chat(username):
    filter_chat_history = []
    for message in chat_history:
        if can_view(message, username):
            filter_chat_history.append(message)
    
    return render_template("chat.html", chat_history=filter_chat_history, username=username, tags=tag)
    
@app.route("/chat/<username>/tags/<hashtag>")
def show_hashtags(username, hashtag):
    tag_messages = []
    for message in chat_history:
        if "#" + hashtag in message:
            tag_messages.append(message)
            
    return render_template("chat.html", chat_history=tag_messages, username=username)


# @app.route("/tags/brexit")
# def show_tags():
#     tag_messages = []
#     for message in chat_history:
#         if "#brexit" in message:
#             tag_messages.append(message)
            
#     return render_template("brexit.html", tag_messages=tag_messages)

def find_tag():
    for chat in chat_history:
        for word in chat.split(" "):
            if word.startswith("#") and word[1:] not in tag:
                tag.append(word[1:])


@app.route("/new", methods=['POST'])
def add_new_message():
    message = request.form['message']
    username= request.form['username']
    chat_history.append(username + ": " + message)
    find_tag()
    
    return redirect("/chat/" + username)


if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8080, debug=True)