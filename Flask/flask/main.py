from flask import Flask,render_template

app = Flask(__name__)

## Integrating html with flask framework
@app.route("/")
def html():
    return "<html><h1> This is a header tag </h1></html>"

## Integrating html with flask framework
@app.route("/html")
def head():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/css")
def css():
    return render_template("style.css")

if __name__ == "__main__":
    app.run(debug =True)