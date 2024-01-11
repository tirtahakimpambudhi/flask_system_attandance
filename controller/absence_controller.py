import os
from config.config import Config
from db.db import new_connection
from models.absence import SupabaseAbsensi
from models.students import SupabaseStudents
from validations.forms import EditAbsenceForm
from flask import jsonify, render_template, request
import numpy as np
from PIL import Image
import io
import face_recognition


pool = new_connection(Config.DATABASE["url"],Config.DATABASE["api_key"])
model_absence = SupabaseAbsensi(pool=pool)
model_student = SupabaseStudents(pool=pool)

def index():
    try:
        absence = model_absence.get_all_absence().data
        if len(absence) != 0:
            for a in absence :
                std = model_student.get_students_by_id(a["student_id"]).data
                if std: 
                    std_dict = std[0]  
                    a["student"] = std_dict
                    
        return render_template("absensi/index.html",datas=absence)
    except KeyError as e:
        return render_template("main/error.html",error={ "code" : 500 , "title" : type(e).__name__ , "message" : f"KeyError: {str(e)}"}) , 500
    except IndexError as e:
                return render_template("main/error.html",error={ "code" : 500 , "title" : type(e).__name__ , "message" : f"KeyError: {str(e)}"}) , 500
    except Exception as error:
        return render_template("main/error.html",error={ "code" : 500 , "title" : type(error).__name__ , "message" : error}) , 500



def match():
    try:
        if 'photo' not in request.files:
            return jsonify({"match": False, "message": "No photo data provided"}), 400

        # Load the uploaded image
        image = Image.open(io.BytesIO(request.files['photo'].read())).convert('RGB')
        image_array = np.array(image)

        # Get face encodings from the uploaded image
        face_encodings = face_recognition.face_encodings(image_array)
        
        if not face_encodings:
            return jsonify({"match": False, "message": "Face not detected"}), 400
        
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
                    id = file_image.split(".")[0]
                    model_absence.insert_absence({"student_id" : int(id),"status" : "attend"})
                    return jsonify({"match": True, "message": "Successfully matched", "filename": file_image}), 200

        return jsonify({"match": False, "message": "Failed to match"}), 400

    except Exception as e:
        return jsonify({"match": False, "message": str(e)}), 500
