from flask import Flask, render_template, request ,redirect, url_for, send_file
import os
import csv
import xlsxwriter
import sys
import zipfile
from tempfile import TemporaryDirectory
import shutil

from Analisi import *

app = Flask(__name__)

@app.route("/")

@app.route("/home")
def home():
    return render_template("index.html")

@app.route("/main")
def main():
    return render_template("main.html")

@app.route('/upload.html',methods = ['POST'])
def upload_route_summary():
    if request.method == 'POST':

        # Create variable for uploaded file
        f = request.files['fileupload']
        
        zip = zipfile.ZipFile(f)
        zip.extractall("Temporary")

        explore_dir("Temporary/QUINT","Temporary/")
        for i in os.listdir("Temporary"+ "/Results"):
            print(i)

    return render_template('main.html')


@app.route('/file.doc')
def download_file():
    p = "Temporary/Results"
    f = shutil.make_archive("Results", 'zip', p)
    return send_file(f,as_attachment = True)
    
if __name__ == '__main__' :
    app.run(debug = True, port = 5001)