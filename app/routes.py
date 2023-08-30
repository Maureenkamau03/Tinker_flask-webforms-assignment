from app import app
from flask import render_template, flash, redirect, url_for 
from app.forms import LoginForm

@app.route("/")
@app.route("/home")
def home():
    return render_template('index.html', title='shop Page')

@app.route("/register")
def register():
    return render_template('register.html', title='Register Page')

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(f'You are requesting to login in {form.username.data}')
        return redirect(url_for('index'))   
    return render_template('login.html', title='Login', form=form)