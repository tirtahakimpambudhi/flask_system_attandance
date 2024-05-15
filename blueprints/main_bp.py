from flask import Blueprint,render_template

main_views = Blueprint("main",__name__)

@main_views.route("/",methods=["GET"])
def index():
    return render_template("main/index.html")

@main_views.route("/about",methods=["GET"])
def about():
    return render_template("main/about.html")