from flask import Flask, request, render_template
from stories import story

app = Flask(__name__)


@app.route('/')
def show_form():
    return render_template("base.html")


@app.route('/results')
def show_results():
    place = request.args.get("place")
    noun = request.args.get("noun")
    verb = request.args.get("verb")
    adjective = request.args.get("adjective")
    plural_noun = request.args.get("plural_noun")

    return render_template("results.html", place=place, noun=noun, verb=verb, adjective=adjective, plural_noun=plural_noun)
