from flask import Blueprint,render_template,url_for
import json
main_views = Blueprint("main",__name__)

teams = []
with open('teams.json') as f:
    teams = json.load(f)

@main_views.route("/",methods=["GET"])
def index():
    return render_template("main/index.html",teams=teams)
