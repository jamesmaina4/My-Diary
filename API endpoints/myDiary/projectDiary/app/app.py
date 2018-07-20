from flask import Flask, render_template, request, jsonify
from data import Entries

app = Flask(__name__)
api = Api(app)

Entries = Entries()


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/profile", methods=["GET"])
def profile():
    return render_template("profile.html")


@app.route("/contents", methods=["GET"])
def returnEntries():
    return render_template("contents.html", entries=Entries)


@app.route("/contents/<string:id>", methods=["GET"])
def returnEntry(id):
    ents = [entry for entry in entries if entry["id"] == id]
    return render_template("viewEntry.html", id=id)


@app.route("/addEntry", methods=["POST"])
def addOne():
    entry = {"id": request.json["id"]}

    entries.append(entry)
    """return jsonify({"entries" : entries})"""
    return render_template("addEntry.html")


@app.route("/contents/<string:id>", methods=["PUT"])
def editOne(id):
    ents = [entry for entry in entries if entry["id"] == id]
    """return jsonify({"entries" : entries})"""
    return render_template("viewEntry.html", id=id)


@app.route("/contents/<string:id>", methods=["DELETE"])
def removeOne(id):
    ents = [entry for entry in entries if entry["id"] == id]
    return jsonify({"entries": entries})
    """return render_template("viewEntry.html", id=id)"""


if __name__ == "__main__":
    app.run(debug=True)
