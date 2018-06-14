# Project: Website in Python using flask library
# Author: Sahil Sharma
# Created on: Feb 12, 2018
# Last edited on: March 13, 2018

# From 'flask' library import 'Flask' class/object.
# render_template to use HTML pages for website.
from flask import Flask, render_template

# Note: Create a folder named 'tempalate' where all html pages will be stored.

# Instantiating the object.
# __name__: will store the name of the script.
app = Flask(__name__)

# Creates a homepage. Go to 'localhost:5000'
@app.route('/')
def home():
	return render_template("home.html")

# Creates another page. Go to it using 'localhost:5000/about'
@app.route('/about/')
def about():
	return render_template("about.html")

# When we execute the script, python assigns __name__ = __main__
# If we import this script from another script, then __name__ will be equals to __script1__
# Script is whole code from line1 to last line.
if __name__ == "__main__":
	app.run(host='0.0.0.0')
#	app.run(debug = True)
