from flask import Flask, render_template, url_for, flash
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = '56ee563ebf03882044dd258d8cb54cc6'

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
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!')
    return render_template('register.html', title='Register', form=form)

@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)

if __name__ == '__main__':
    app.run(debug=True)