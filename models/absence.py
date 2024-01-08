
import logging

from supabase import Client
from config.config import Config

class SupabaseAbsensi():
    def __init__(self, pool :Client):
        self.db :Client = pool
    def get_all_absence(self):
        try:
            return self.db.table(Config.DATABASE["tables"][1]).select("*").execute()
        except Exception as error:
            logging.error(f"error execution query absensi raise : {type(error).__name__} - { error}")
            raise error
    def get_absence_by_id(self,id :int):
        try:
            return self.db.table(Config.DATABASE["tables"][1]).select("*").eq("id",id).limit(1).execute()
        except Exception as error:
            logging.error(f"error execution query absensi raise : {type(error).__name__} - { error}")
            raise error
    def insert_absence(self,student :dict):
        try:
            return self.db.table(Config.DATABASE["tables"][1]).insert(student).execute()
        except Exception as error:
            logging.error(f"error execution query absensi raise : {type(error).__name__} - { error}")
            raise error
    def update_absence_by_id(self,id :int,student :dict):
        try:
            return self.db.table(Config.DATABASE["tables"][1]).update(student).eq("id",id).execute()
        except Exception as error:
            logging.error(f"error execution query absensi raise : {type(error).__name__} - { error}")
            raise error
    def delete_absence_by_id(self,id :int):
        try:
            return self.db.table(Config.DATABASE["tables"][1]).delete().eq("id",id).execute()
        except Exception as error:
            logging.error(f"error execution query absensi raise : {type(error).__name__} - { error}")
            raise error

