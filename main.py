from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import random
import datetime
import os

app = Flask(__name__)

@app.route('/')
def hello_world():
    #below creates a variable and shows how you can send that to html documents to use
    random_num = random.randint(1, 10)
    current_year = datetime.datetime.now().year
    # By default render_template looks for a templates folder
    # (so make sure you have your files in a foler called "templates")
    # static content like css files or images must be in a folder called static

    #pass a variable name with teh value(**kwargs) in to send to html to use
    return render_template("index.html", num=random_num, year=current_year)

@app.route('/blogs')
def my_blogs():
    return render_template("blog.html")

if __name__ == '__main__':
    app.run(debug=True)