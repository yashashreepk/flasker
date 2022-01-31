from flask import Flask, render_template

# create a Flask instance
app = Flask(__name__)


# create a route decorator
''' 
Filters!!!!
safe
capitalize
lower
upper
title
trim
striptags
'''
@app.route('/')
def index():
    first_name="Yashashree"
    stuff = "This is <strong>Bold</strong> Text"
    stuff1 = "This is the example of title"
    fav_pizza=['perripone','cheese_brust','veg_single',41]
    return render_template("index.html",first_name=first_name,stuff=stuff,stuff1=stuff1,fav_pizza=fav_pizza)
# localhost:5000/user/john
@app.route('/user/<name>')
def user(name):
    return render_template("user.html",user_name=name)
# return "<h1> hello {} <h1>".format(name)


# create custom error page


# invalid URL
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"),404

# internal server error
@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"),500


