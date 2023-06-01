from flask import Flask, flash, redirect, render_template, url_for, request, session
from flask_bootstrap import Bootstrap5

from entity import Entity
from utils import create_triplet, createTimestamp, writer
import testing

# create the app
app = Flask(__name__)
app.config[
    "SECRET_KEY"
] = 'h+u5-sNA2%Fr&3"y"9nQEn==rfLjfKB{$RGShJ"$2I`d&j[5-J79:RJZoQJ('
app.config["BOOTSTRAP_BOOTSWATCH_THEME"] = "lux"
bootstrap = Bootstrap5(app)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        if request.form.get("start"):
            session["descriptions"] = [create_triplet("", 4)]
            return redirect(url_for("define"))
        
    return render_template("index.html")


@app.route("/define", methods=["GET", "POST"])
def define():
    if request.method == "POST":
        if request.form.get("simulate"):
            session.pop("_flashes", None)
            entities = []
            for index in range(len(session.get("descriptions"))*3):
                check_begin = "e{}".format(str(index+1))
                entities.append([ v for k, v in request.form.items() if k.startswith(check_begin)])
            session["entities"] = entities
            return redirect(url_for("simulation"))
        
        if request.form.get("add"):
            session.pop('_flashes', None)
            session["descriptions"].append(create_triplet("", 4))
        
        if request.form.get("back"):
            return redirect(url_for("index"))
        
    return render_template("define.html", page_descriptions=session.get("descriptions")[1:], first_triplet=session.get("descriptions")[0])


@app.route("/define/simulation", methods=["GET", "POST"])
def simulation():
    #testing.test_handshake()
    #testing.test_dhcp()

    testing.test_dummyTextTranslate()

    logfile = createTimestamp()

    with open(logfile, "r") as file:
        output = file.read()

    flash(output, "success")
    if request.method == "POST":
        if request.form.get("back"):
            return redirect(url_for("index"))
        
    return render_template("simulation.html")


if __name__ == "__main__":
    app.run(debug=True)
