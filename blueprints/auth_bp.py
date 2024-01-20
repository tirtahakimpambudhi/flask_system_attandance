import face_recognition
import io
import os
import numpy as np
from config.config import Config
from PIL import Image
from flask import Blueprint,render_template,request,jsonify
from validations.forms import RegisterForm
from helper.helper import save_file_blob

auth_views = Blueprint("auth", __name__)

@auth_views.route("/register",methods=["GET","POST"])
def register():
    form = RegisterForm()
    print(form.errors)
    if form.validate_on_submit():
        nis = form.nis.data
        name = form.name.data
        number_absence = form.number_absence.data
        major = form.major.data
        year_graduated = form.year_graduated.data
        photo_data = form.photo.data
        save_file_blob(photo_data,f'{nis}_{name}.png')
        print({"nis":nis,"name":name,"number_absence":number_absence,"major":major,"year_graduated":year_graduated,})
    return render_template("auth/register.html",form=form)

@auth_views.route("/login",methods=["GET"])
def login():
    return render_template("auth/login.html",call={ "timeout" : Config.CALL_API_TIMEOUT, "interval" : Config.CALL_API_TIME_INTERVAL })

@auth_views.route("/match", methods=["POST"])
def match():
    if 'photo' not in request.files:
        return jsonify({"match": False, "messages": "No photo data provided"}), 400

    # Load the uploaded image
    image = Image.open(io.BytesIO(request.files['photo'].read())).convert('RGB')
    image_array = np.array(image)

    # Get face encodings from the uploaded image
    face_encodings = face_recognition.face_encodings(image_array)
    
    if not face_encodings:
        return jsonify({"match": False, "messages": "Face not detected"}), 400
    
    uploaded_face_encoding = face_encodings[0]

    # List all files in the upload directory
    file_image_list = os.listdir(Config.UPLOAD_PATH)
    file_image_list = [f for f in file_image_list if os.path.isfile(os.path.join(Config.UPLOAD_PATH, f))]

    for file_image in file_image_list:
        file_image_path = os.path.join(Config.UPLOAD_PATH, file_image)
        
        # Load each image file
        file_image_array = face_recognition.load_image_file(file_image_path)
        
        # Get face encodings for each image file
        file_image_encodings = face_recognition.face_encodings(file_image_array)
        
        for file_face_encoding in file_image_encodings:
            # Compare the uploaded face encoding with the current file's face encoding
            match = face_recognition.compare_faces([uploaded_face_encoding], file_face_encoding)
            
            if match[0]:
                return jsonify({"match": True, "message": "Successfully matched", "filename": file_image}), 200

    return jsonify({"match": False, "messages": "Failed to match"}), 400

@auth_views.route("/absensi",methods=["GET"])
def index():
    return  "Absen"