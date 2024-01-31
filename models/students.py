import logging

from supabase import Client
from config.config import Config

class Students():
    def __init__(self, pool :Client):
        self.db :Client = pool
    def get_all_students(self):
        try:
            return self.db.table(Config.DATABASE["table"]).select("*").execute()
        except Exception as error:
            logging.error(f"error execution query students raise : {type(error).__name__} - { error}")
            return None
    def get_students_by_id(self,id :int):
        try:
            return self.db.table(Config.DATABASE["table"]).select("*").eq("id",id).limit(1).execute()
        except Exception as error:
            logging.error(f"error execution query students raise : {type(error).__name__} - { error}")
            return None
    def insert_students(self,student :dict):
        try:
            return self.db.table(Config.DATABASE["table"]).insert(student).execute()
        except Exception as error:
            logging.error(f"error execution query students raise : {type(error).__name__} - { error}")
            return None
    def update_students_by_id(self,id :int,student :dict):
        try:
            return self.db.table(Config.DATABASE["table"]).update(student).eq("id",id).execute()
        except Exception as error:
            logging.error(f"error execution query students raise : {type(error).__name__} - { error}")
            return None
    def delete_students_by_id(self,id :int):
        try:
            return self.db.table(Config.DATABASE["table"]).delete().eq("id",id).execute()
        except Exception as error:
            logging.error(f"error execution query students raise : {type(error).__name__} - { error}")
            return None