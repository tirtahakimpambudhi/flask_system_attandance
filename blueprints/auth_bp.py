from flask import Blueprint,render_template
from validations.forms import RegisterForm
auth_views = Blueprint("auth", __name__)

@auth_views.route("/register",methods=["GET"])
def register():
    form = RegisterForm()
    return render_template("auth/register.html",form=form)

@auth_views.route("/login",methods=["GET"])
def login():
    return "Login"

@auth_views.route("/absensi",methods=["GET"])
def index():
    return  "Absen"