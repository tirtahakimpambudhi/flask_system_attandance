from models.students import SupabaseStudents
from flask import jsonify,request,render_template
from config.config import Config
from PIL import Image
from flask import render_template,request,jsonify
from config.config import Config
from werkzeug.utils import secure_filename
from validations.forms import RegisterForm,LoginForm
from helper.helper import save_file_blob
import base64
from io import BytesIO
from db.db import new_connection
import numpy as np
import uuid
import face_recognition
import os

pool = new_connection(Config.DATABASE["url"],Config.DATABASE["api_key"])
model = SupabaseStudents(pool=pool)

def index():
        try :
            students = model.get_all_students().data
            return render_template("auth/index.html" , students=students) , 200
        except KeyError as e:
            return render_template("main/error.html",error={ "code" : 500 , "title" : type(e).__name__ , "message" : f"KeyError: {str(e)}"}) , 500
        except IndexError as e:
            return render_template("main/error.html",error={ "code" : 500 , "title" : type(e).__name__ , "message" : f"KeyError: {str(e)}"}) , 500
        except Exception as error :
            return render_template("main/error.html",error={ "code" : 500 , "title" : type(error).__name__ , "message" : error}) , 500


def show():
    try:
        key = request.args.get('s')
        data = model.get_students_by_key(key=key).data
        for student in data:
            student['id'] = str(student['id'])
        return jsonify({"students": data, "message" : "successfully search"}), 200
    except KeyError as e:
        return jsonify({"data" : [] , "error": f"KeyError: {str(e)}"}), 500
    except IndexError as e:
        return jsonify({"data" : [] ,"error": f"IndexError: {str(e)}"}), 500
    except Exception as e:
        return jsonify({"data" : [] ,"error": str(e)}), 500
        
def create() :
        try :
            form = RegisterForm()
            if form.validate_on_submit():
                id = uuid.uuid1().int
                nis = form.nis.data
                name = form.name.data
                number_absence = form.number_absence.data
                major = form.major.data
                year_graduated = form.year_graduated.data
                photo_data = form.photo.data
                save_file_blob(photo_data=photo_data,filename=f"{id}.png")
                model.insert_students({"id" : id,"nis":nis,"name":name,"number_absence":number_absence,"major":major,"year_graduated":year_graduated})
            return render_template("auth/register.html",form=form) , 200
        except KeyError as e:
            return render_template("main/error.html",error={ "code" : 500 , "title" : type(e).__name__ , "message" : f"KeyError: {str(e)}"}) , 500
        except IndexError as e:
            return render_template("main/error.html",error={ "code" : 500 , "title" : type(e).__name__ , "message" : f"KeyError: {str(e)}"}) , 500
        except Exception as error :
            return render_template("main/error.html",error={ "code" : 500 , "title" : type(error).__name__ , "message" : error}) , 500


def login():
    try:
        form = LoginForm()
        if form.validate_on_submit():
            nis = form.nis.data
            status = form.status.data
            id = pool.table(Config.DATABASE["tables"][0]).select("id").eq("nis",nis).execute().data
            pool.table(Config.DATABASE["tables"][1]).insert({"student_id" :id[0]["id"],"status" : status}).execute()
            
        return render_template("auth/login.html",call={ "timeout" : Config.CALL_API_TIMEOUT, "interval" : Config.CALL_API_TIME_INTERVAL },form=form) , 200
    except KeyError as e:
        return render_template("main/error.html",error={ "code" : 500 , "title" : type(e).__name__ , "message" : f"KeyError: {str(e)}"}) , 500
    except IndexError as e:
                return render_template("main/error.html",error={ "code" : 500 , "title" : type(e).__name__ , "message" : f"KeyError: {str(e)}"}) , 500
    except Exception as error:
        return render_template("main/error.html",error={ "code" : 500 , "title" : type(error).__name__ , "message" : error}) , 500

def verify_face():
    try:
        data = request.get_json()
        image_data = data['image']
        image_data = image_data.split(',')[1]
        image_bytes = base64.b64decode(image_data)
        image = Image.open(BytesIO(image_bytes))

        # Ensure the image is in RGB format
        image = image.convert('RGB')

        image_array = np.array(image)

        face_locations = face_recognition.face_locations(image_array)
        if face_locations:
            return jsonify({"verify": True, "message": "Face detected"}) , 200
        else:
            return jsonify({"verify": False, "message": "No face detected"}) , 400
    except KeyError as e:
        return jsonify({"verify" : False ,"message": f"KeyError: {str(e)}"}), 500
    except IndexError as e:
        return jsonify({"verify" : False ,"message": f"IndexError: {str(e)}"}), 500
    except Exception as e:
        return jsonify({"verify" : False ,"message": str(e)}), 500
    
def edit(id : int):
    try:
        data = request.get_json()
        if "image" in data and data["image"]:
            filename = secure_filename(f"{id}.png")
            file_path = os.path.join(Config.UPLOAD_PATH,filename)
            if os.path.exists(file_path):
                os.remove(file_path)

            image_data = data["image"].split(',')[1]
            image_bytes = base64.b64decode(image_data)
            image = Image.open(BytesIO(image_bytes))
            image.save(file_path)
            del data["image"]
        model.update_students_by_id(id=id,student=data)
        return jsonify({"status": "success", "message": "successfully update"}),200
    except KeyError as e:
        return jsonify({"status" : "failure" ,"message": f"KeyError: {str(e)}"}), 500
    except IndexError as e:
        return jsonify({"status" : "failure" ,"message": f"IndexError: {str(e)}"}), 500
    except Exception as e:
        return jsonify({"status" : "failure" ,"message": str(e)}), 500
         


def match_by_id(id: int):
    try:
        data = request.get_json()
        image_data = data['image']
        image_data = image_data.split(',')[1]
        image_bytes = base64.b64decode(image_data)
        image = Image.open(BytesIO(image_bytes))

        # Ensure the image is in RGB format
        image = image.convert('RGB')

        image_array = np.array(image)

        # Get face encodings from the uploaded image
        face_encodings = face_recognition.face_encodings(image_array)
        
        if not face_encodings:
            return jsonify({"match": False, "message": "Face not detected"}), 400
        
        uploaded_face_encoding = face_encodings[0]
        
        file_image_path = os.path.join(Config.UPLOAD_PATH, f"{id}.png")
        
        if not os.path.exists(file_image_path):
            return jsonify({"match": False, "message": "Reference image not found"}), 404
        
        # Load each image file
        file_image_array = face_recognition.load_image_file(file_image_path)
        
        # Get face encodings for each image file
        file_image_encodings = face_recognition.face_encodings(file_image_array)
        
        if not file_image_encodings:
            return jsonify({"match": False, "message": "No face detected in reference image"}), 400
        
        for file_face_encoding in file_image_encodings:
            # Compare the uploaded face encoding with the current file's face encoding
            match = face_recognition.compare_faces([uploaded_face_encoding], file_face_encoding)
            
            if match[0]:
                return jsonify({"match": True, "message": "Successfully matched"}), 200

        return jsonify({"match": False, "message": "Failed to match"}), 400
    
    except KeyError:
        return jsonify({"match": False, "message": "Invalid data format"}), 400
    
    except Exception as e:
        return jsonify({"match": False, "message": str(e)}), 500
    