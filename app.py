from flask import Flask,render_template
app=Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", path="home")

@app.route("/about")
def about():
    return render_template("about.html", path="about")

if __name__ == "__main__":
    app.run(port=4000,host="localhost")