from flask import render_template
from app import app

@app.route("/")
@app.route("/index")
def index():
    user = { 'nickname': 'agent47'}
    posts = [
        {
            'author' : { 'nickname': "Jon"},
            'body' : "Some test foo"
        },
        {
            'author' : { 'nickname': "Alice"},
            'body' : "I am not a kryptographer"
        }
    ]
    return render_template("index.html",
        title = "47's home",
        user = user,
        posts = posts)

