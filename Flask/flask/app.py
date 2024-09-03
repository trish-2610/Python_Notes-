# ## Basic Skeleton of flask framework

# from flask import Flask 

# ## WSGI application
# app=Flask(__name__)
# ## It creates an instance of the Flask Class which will be your WSGI application

# if __name__ == "__main__": ## execution process starts from here 
#     app.run()

## -----------------------------------------------------------------------------
from flask import Flask 

## WSGI application
app=Flask(__name__)
## It creates an instance of the Flask Class which will be your WSGI application

@app.route("/") ## welcome page 
def welcome():
    return "Hello ... welcome to flask"

@app.route("/home") ## home page
def home():
    return "This is the home page"

@app.route("/index") ## index page
def index():
    return "This is the index page"

if __name__ == "__main__": ## execution process starts from here 
    app.run(debug=True)
    ## debug = True for making changes directly without restarting
