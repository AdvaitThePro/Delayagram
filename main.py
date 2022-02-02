from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def main():
    return render_template("index.html")

@app.route("/profile")
def profile():
    return "<h1>Profile Page</h1>"

@app.route("/search")
def search():
    return "<h1>Seach Page</h1>"

@app.route("/new")
def new():
    return "<h1>New Post Page</h1>"

@app.route("/follow")
def follow():
    return "<h1>Follow Page</h1>"

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port="5000")