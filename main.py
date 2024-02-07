from flask import Flask, render_template, redirect, request, session
from main_config import app, db
from Backend.entities.User import User
from Backend.controllers.UserController import user
from Backend.controllers.FileController import fileDownload

app.secret_key = 'Shorohova'
app.register_blueprint(user)
app.register_blueprint(fileDownload)


with app.app_context():
    db.create_all()

def authChecker():
    user = None
    if 'user_id' in session:
        user = session['user_id']
    return user


@app.route('/')
def index():
    user = authChecker()
    if user == None:
        return redirect('/login', code=302)
    return render_template("index.html")


@app.route('/registration')
def registration():
    user = authChecker()
    if user != None:
        return redirect('/', code=302)
    return render_template("registration.html")


@app.route('/login')
def authorization():
    user = authChecker()
    if user != None:
        return redirect('/', code=302)
    return render_template("authorization.html")


@app.after_request
def add_header(r):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r


if __name__ == '__main__':
    app.run(debug=True, port=5001)
