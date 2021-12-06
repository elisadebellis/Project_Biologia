from flask import Flask, render_template, request ,redirect, url_for
import os
import csv
import xlsxwriter
import sys
from werkzeug.utils import secure_filename
import io


app = Flask(__name__)

@app.route("/")
@app.route("/home")

def home():
    return render_template("index.html")

@app.route('/upload.html',methods = ['POST'])
def upload_route_summary():
    if request.method == 'POST':

        # Create variable for uploaded file
        f = request.files['fileupload']
        f.seek(0)
        
        content = f.read()
        content = str(content, 'utf-8')
        return render_template('index.html', text=content)


    
if __name__ == '__main__' :
    app.run(debug = True, port = 5001)