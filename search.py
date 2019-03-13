from flask import Flask, redirect, url_for, request, render_template
from urllib.request import urlopen
import json
app = Flask(__name__)

if __name__ == '__main__':
   app.run(debug=True)