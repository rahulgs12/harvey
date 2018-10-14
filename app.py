import os
from flask import Flask, flash, request, redirect, url_for, render_template, abort, send_file
from werkzeug.utils import secure_filename
from jinja2 import Template
from random import randint

app = Flask(__name__)

db = dict()

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/form')
def form():
    return render_template('forms.html', random = ''.join(["%s" % randint(0, 9) for num in range(0, 6)]))

@app.route('/new', methods=['POST'])
def new():
    p = request.form.to_dict()
    db[p['patientID']] = p
    # return 'new user added', file.filename
    file = request.files['inputFile']
    dest_path = 'uploads/' + request.form['patientID'] + '/'
    if not os.path.isdir(dest_path):
        os.makedirs(dest_path)
    file.save(dest_path + secure_filename(file.filename))
    return redirect("/")

# @app.route('/user/<username>')
# def show_user(username):
#     user = User.query.filter_by(username=username).first_or_404()
#     return render_template('show_user.html', user=user)

# @app.route('/', defaults={'req_path': ''})
@app.route('/<user>')
def dir_listing(user):
    BASE_DIR = 'uploads/'
    # # Joining the base and the requested path
    abs_path = os.path.join(BASE_DIR, user)
    print (abs_path)
    # # Return 404 if path doesn't exist
    if not os.path.exists(abs_path):
        return abort(404)
    # # Show directory contents
    files = os.listdir(abs_path)
    files = [abs_path + '/'+ f  for f in files]
    name = "Rahul"
    id = "1"
    return render_template('files.html', files = files, name = name, id = id)

@app.route('/uploads/<user>/<filename>')
def get_file(user, filename):
    BASE_DIR = 'uploads/'
    abs_path = os.path.join(BASE_DIR, user, filename)
    if os.path.isfile(abs_path):
        return send_file(abs_path)
    else:
        return abort(404)
    return abs_path



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
