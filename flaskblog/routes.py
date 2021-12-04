from flask import render_template, url_for, flash, redirect, request
from flask_login import login_user, logout_user, current_user, login_required

from flaskblog import app, db, bcrypt
from flaskblog.forms import RegistrationForm, LoginForm
from flaskblog.models import User, Post


posts = [
    {
    'author' : 'Nick R',
    'title': 'post 1',
    'content': 'this is the first post',
    'date_posted': 'June 9, 1969'
    },
    {
    'author' : 'John Smith',
    'title': 'post 2',
    'content': 'this is the second',
    'date_posted': 'March 9, 1999'
    }
]

@app.route("/")
@app.route("/home")
def home_page():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about_page():
    return render_template('about.html', title='About')

@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home_page'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Your Account has been created, you are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home_page'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home_page'))
        else:
            flash('Login Failed, please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home_page'))

@app.route("/account")
@login_required
def account():
    return render_template('account.html', title='Account')