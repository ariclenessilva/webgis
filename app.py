from flask import Flask, escape, request, render_template
import os

app = Flask(__name__)


@app.route('/')
def index():

    list_geojson_files = []
    list_geotiff_files = []
    for root, dirs, files in os.walk("./static/geodata"):
        for filename in files:
            if '.geojson' in filename:
                list_geojson_files.append(root.split('geodata')[-1][1:]+'/'+filename)
            if '.geojsonjhbj' in filename:
                list_geotiff_files.append(root.split('geodata')[-1][1:]+'/'+filename)

    return render_template('index.html', list_geojson_files=list_geojson_files)
