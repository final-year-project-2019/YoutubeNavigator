from flask import Flask, redirect, url_for, request, render_template
from urllib.request import urlopen
import json
import key
app = Flask(__name__)

@app.route('/search',methods = ['POST', 'GET'])
def search():
    if request.method == 'POST':
        q = request.form['keyword']
        url = "https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=10&q=" + q +"&type=video&key=AIzaSyAwNhzfrT58k7wNaOmUB6vS5tJ0e39t7Aw"
        response = urlopen(url)
        data = json.loads(response.read())
        videoId = []
        x= ""
        for i in range(len(data["items"])):
            videoId.append(data["items"][i]["id"]["videoId"]);
        return render_template('search.html',videoIds = videoId,lenV = len(videoId));
    else:
        return render_template('search.html',videoIds = [],lenV=0);

if __name__ == '__main__':
   app.run(debug=True)