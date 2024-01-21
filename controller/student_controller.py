from models.students import SupabaseStudents
from supabase import Client
from flask import jsonify,request

class StudentsController():
    def __init__(self,pool :Client) -> None:
        self.model = SupabaseStudents(pool=pool)
    
    def index(self):
        try :
            return jsonify({ "students" : self.model.get_all_students() }) , 200
        except Exception as error :
            return jsonify({"error" : error}) , 500
    
    def show(self,id :int) :
        try :
            return jsonify({ "students" : self.model.get_students_by_id(id) }) , 200
        except Exception as error :
            return jsonify({"error" : error}) , 500
    
    