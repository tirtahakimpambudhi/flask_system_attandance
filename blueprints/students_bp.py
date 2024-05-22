from controller.student_controller import login,create,verify_face,index,match_by_id,edit,show
from flask import Blueprint


students_route = Blueprint("students",__name__)
# html
students_route.route("/register",methods=["GET","POST"])(create)
students_route.route("/login",methods=["GET","POST"])(login)
students_route.route("/",methods=["GET"])(index)
# api
students_route.route("/verify-face",methods=["POST"])(verify_face)
students_route.route("/search",methods=["GET"])(show)
students_route.route("/match/<int:id>",methods=["POST"])(match_by_id)
students_route.route("/edit/<int:id>",methods=["POST"])(edit)

