from app import app
from flask import render_template, flash, redirect, url_for 
from app.forms import LoginForm, RegisterForm, AddproductForm

@app.route("/")
@app.route("/home")
def home():
    return render_template('shop.html', title='shop Page')

@app.route("/register" , methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        flash(f'{form.username.data}, You have successfully registered')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register Page', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(f'Welcome {form.username.data}')
        return redirect(url_for('home'))   
    return render_template('login.html', title='Login', form=form)

@app.route("/addproduct", methods=['GET', 'POST'])
def addproduct():
    form = AddproductForm() 
    if form.validate_on_submit():
        flash(f'You have added {form.product_name.data}')
        return redirect(url_for('home'))
    return render_template('addproduct.html', title='addproduct', form=form)