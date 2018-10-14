import os
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
from jinja2 import Template

app = Flask(__name__)
# app.config['SQLALCHEMY_DB_URL'] = '/'
# db = SQLAlchemy(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods = ['POST'])
def upload():
    file = request.files['inputFile']
    return file.filename
    # newFile = FileContents(name = file.filename, data = file.read())
    # db.session.add(newFile)
    # db.session.commit()
    # return ("Saved " + file.filename + ' to the database!')
    
@app.route('/form')
def form():
    return render_template('forms.html')

# class FileContents(db.Model):
#     id = db.Column(db.Integer, primary_key = True)
#     name = db.Column(db.String(300))
#     data = db.Column(db.LargeBinary)



# @app.route('/new', methods=['GET'])
# def new_user():
#     print(request.args['lastname'])
#     file = request.files['inputFile']
#     return 'new user added', file.filename 

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
