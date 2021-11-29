from flask import Flask, render_template

app = Flask(__name__)

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

if __name__ == '__main__':
    app.run(debug=True)