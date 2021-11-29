from flask import Flask

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home_page():
    return "<h1>Hello, Internet!</h1>"


@app.route("/about")
def about_page():
    return "<p>I need to test this framework to see what's going on</p>"

if __name__ == '__main__':
    app.run(debug=True)