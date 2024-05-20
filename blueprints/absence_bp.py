from controller.absence_controller import match,index
from flask import Blueprint


absence_route = Blueprint("absence",__name__)

# api
absence_route.route("/login",methods=["POST"])(match)
absence_route.route("/",methods=["GET"])(index)