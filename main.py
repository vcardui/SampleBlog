# +----------------------------------------------------------------------------+
# | CARDUI WORKS v1.0.0
# +----------------------------------------------------------------------------+
# | Copyright (c) 2024 - 2025, CARDUI.COM (www.cardui.com)
# | Vanessa Reteguín <vanessa@reteguin.com>
# | Released under the MIT license
# | www.cardui.com/carduiframework/license/license.txt
# +----------------------------------------------------------------------------+
# | Author.......: Vanessa Reteguín <vanessa@reteguin.com>
# | First release: January 9th, 2025
# | Last update..: March 27th, 2025
# | WhatIs.......: Cardui Web Development (Upgraded Blog) - Main
# +----------------------------------------------------------------------------+

# ------------ Resources / Documentation involved -------------
# Flask Quickstart: https://flask.palletsprojects.com/en/stable/quickstart/
# Jinja Template Designer Documentation: https://jinja.palletsprojects.com/en/stable/templates/

# ------------------------- Libraries -------------------------
from flask import Flask, render_template, request
import requests

from post import Post
from carduiBot import EmailBot

# ------------------------- Variables -------------------------
app = Flask(__name__)

# --------------------------- Code ----------------------------
@app.route('/')
@app.route('/index.html')
def home():
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    blog_response = requests.get(blog_url)
    all_posts = blog_response.json()
    return render_template("index.html", posts=all_posts)

@app.route('/about.html')
def about():
    return render_template("about.html")

@app.route('/contact.html', methods=["GET","POST"])
def contact():
    if request.method == "POST":
        data = request.form
        print(data)
        carduiBot = EmailBot(data)
        carduiBot.sendMail()
        return render_template("contact.html", title="Successfully sent message")
    else:
        return render_template("contact.html", title="Contact Me")

@app.route('/blog/<id>')
def post(id):
    ChosenPost = Post(id)
    return render_template("post.html", post=ChosenPost)


if __name__ == "__main__":
    app.run(debug=True)
