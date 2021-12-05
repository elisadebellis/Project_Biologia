from flask import Flask, render_template, request,redirect, url_for
import os
import csv
import xlsxwriter
import sys

app = Flask(__name__)

@app.route("/")
@app.route("/home")

def home():
    return render_template("index.html")

@app.route("/result", methods = ['POST',"GET"])
def result(): 
    id =""
    if request.method == 'POST':

        # Create variable for uploaded file
        f = request.files['fileupload']  

        #store the file contents as a string
        fstring = f.read()
        
        #create list of dictionaries keyed by header row
        csv_dicts = [{k: v for k, v in row.items()} for row in csv.DictReader(fstring.splitlines(), skipinitialspace=True)]
        
        
        
        for i in csv_dicts:
            for key in i:
                print(key)

    
        
        #do something list of dictionaries
    
    return render_template("index.html")


    
if __name__ == '__main__' :
    app.run(debug = True, port = 5001)