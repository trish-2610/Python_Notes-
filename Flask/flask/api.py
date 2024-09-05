from flask import Flask 
app = Flask(__name__)


## initial data in my to do list 
items = [
    {"id1":1 , "name":"Item1"},
    {"id2":2  , "name":"Item2"}
]

@app.route("/")
def home():
    return "Welcome to my to do list home page"


if __name__ == "__main__":
    app.run(debug = True )