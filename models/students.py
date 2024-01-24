
import logging

from supabase import Client
from config.config import Config

class SupabaseStudents():
    def __init__(self, pool :Client):
        self.db :Client = pool
    def get_all_students(self):
        try:
            return self.db.table(Config.DATABASE["tables"][0]).select("*").execute()
        except Exception as error:
            logging.error(f"error execution query students raise : {type(error).__name__} - { error}")
            raise error
    def get_students_by_id(self,id :int):
        try:
            return self.db.table(Config.DATABASE["tables"][0]).select("*").eq("id",id).limit(1).execute()
        except Exception as error:
            logging.error(f"error execution query students raise : {type(error).__name__} - { error}")
            raise error
    def get_students_by_key(self,key :str):
        try:
            return self.db.table(Config.DATABASE["tables"][0]).select("*").like("name",f"%{key}%").like("major",f"%{key}%").execute()
        except Exception as error:
            logging.error(f"error execution query students raise : {type(error).__name__} - { error}")
            raise error
    def insert_students(self,student :dict):
        try:
            return self.db.table(Config.DATABASE["tables"][0]).insert(student).execute()
        except Exception as error:
            logging.error(f"error execution query students raise : {type(error).__name__} - { error}")
            raise error
    def update_students_by_id(self,id :int,student :dict):
        try:
            return self.db.table(Config.DATABASE["tables"][0]).update(student).eq("id",id).execute()
        except Exception as error:
            logging.error(f"error execution query students raise : {type(error).__name__} - { error}")
            raise error
    def delete_students_by_id(self,id :int):
        try:
            return self.db.table(Config.DATABASE["tables"][0]).delete().eq("id",id).execute()
        except Exception as error:
            logging.error(f"error execution query students raise : {type(error).__name__} - { error}")
            raise error

