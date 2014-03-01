from flask import render_template, flash, redirect
from app import app
from forms import LoginForm

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

@app.route("/login", methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template("login.html",
        title = "Sign In",
        form = form)
