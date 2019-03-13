from flask import Flask, redirect, url_for, request, render_template
from urllib.request import urlopen
import json
import key
app = Flask(__name__)

@app.route('/search',methods = ['POST', 'GET'])
def search():
    return "This is the search page"

if __name__ == '__main__':
   app.run(debug=True)