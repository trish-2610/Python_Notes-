## Building url directly
## Variable rule
## Jinja 2 template engine

from flask import Flask , render_template , request,redirect,url_for
app = Flask(__name__)

@app.route("/home")
def home():
    return render_template("index.html")

## variable rule 
@app.route("/success/<score>")  ## parameter
def success(score):
    return "Your maths score is " + score ## by default string value 

@app.route("/success1/<int:marks>")
## specifying the data-type (by default string)
def success1(marks):
    return "Your maths score is " + str(marks)
## you need to typecast marks into string as we can't concatenate string with integer


## Building url dynamically 
@app.route("/success2/<int:mark>")
def success2(mark):
    res = ""
    if mark >= 33 :
        res = "PASS"
    else :
        res = "FAIL"
    return render_template("/result.html",results=res)

## jinja2 templates 
## {{  }} expressions are used to print o/p in html file
## {%...%} for conditional expressions and loops
## {#...#} for comments  


## using for loop
@app.route("/for1/<int:m>")
def for1(m):
    res = ""
    if m >= 33:
        res = "PASS"
    else :
        res = "FAIL"
    
    exp = {"score":m ,"result":res} ## dictionary
    return render_template("result1.html",results=exp)

## using if-else in html file
@app.route("/ifelse/<int:score>")
def if_else(score):
    return render_template("result.html",results=score)


## building score calculator 
@app.route("/submit",methods=["GET","POST"])
def submit():
    total_score = 0
    if request.method=="POST":
        science = float(request.form["science"])
        maths = float(request.form["maths"])

        total_score = (science+maths)/2

    return redirect(url_for("if_else",score=total_score))

if __name__=="__main__":
    app.run(debug = True) 