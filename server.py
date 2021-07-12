from types import MethodType
from flask import Flask, render_template, request, redirect, session, Markup
import random


app = Flask(__name__)
app.secret_key = "thegameofnumbers"

@app.route("/")
def whatsDanumber():
    random_number = random.randrange(0,101)
    session["guess"] = random_number
    return render_template("index.html")

@app.route("/checkguess", methods=["POST"])
def checknumber():
    selectednum = session["guess"]
    print(selectednum)
    userinput = int(request.form["guessinput"])
    print(userinput);
    text = " "

    if userinput == selectednum:
        text = "Correct!"
        return render_template("index.html", text = text)

    if userinput > selectednum:
        text = "Too high Junior"
        return render_template("index.html", text = text)

    if userinput < selectednum:
        text = "Too low Junior"
        return render_template("index.html", text = text)

if __name__ == "__main__":

    app.run(debug=True)
