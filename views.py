from flask import render_template
from app import app

@app.route("/")
@app.route("/index")
def index():
    user = { 'nickname': 'agent47'}
    return render_template("index.html",
        title = "47's home",
        user = user)

