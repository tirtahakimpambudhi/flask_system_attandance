import unittest
import uuid

from db.db import new_connection
from config.config import Config
from models.students import SupabaseStudents

class ModelsTestCase(unittest.TestCase):
    __config = Config()
    __pool = new_connection(__config.DATABASE["url"], __config.DATABASE["api_key"])
    models_students =  SupabaseStudents(pool=__pool)
    TOTAL_DUMMY_DATA = 10
    dummy_id :int;
    @classmethod
    def setUp(cls):
        for i in range(cls.TOTAL_DUMMY_DATA):
            cls.dummy_id = uuid.uuid1().int
            nis_dummy = 34672+i
            cls.__pool.table(cls.__config.DATABASE["tables"][0]).insert(
                {"id": cls.dummy_id,"nis":nis_dummy, "name": f"dummy name to - {i}", "major": f"dummy major {i}", "number_absence" :i,"major": "SIJA","year_graduated" : 2026}).execute()

    @classmethod
    def tearDown(cls):
        cls.__pool.table(cls.__config.DATABASE["tables"][0]).delete().neq("id",1).execute()

    def test_get_all_students(self):
        test_cases = [
            {
            "name" : "Should be Successfully get all",
            "expected" : self.TOTAL_DUMMY_DATA,
            "actual" : len(self.models_students.get_all_students().data),
            "is_error" : False
            }
        ]
        for case in test_cases:
            with self.subTest(name=case["name"]):
                try:
                    self.assertEqual(case["actual"], case["expected"])
                except Exception as e:
                    self.assertTrue(case["is_error"])
    def test_get_students_by_id(self):
        test_cases = [
            {
                "name" : "Should be Successfuly",
                "id" : self.dummy_id,
                "expected_field" : 8,
                "is_error" : False
            }, {
                "name" : "Should be Successfully but empyt data",
                "id" : uuid.uuid1().int,
                "expected_field" : 0,
                "is_error" : True
            }
        ]
        for case in test_cases:
            with self.subTest(name=case["name"]):
                try:
                    data :dict = self.models_students.get_students_by_id(case["id"]).data
                    self.assertEqual(len(data[0]),case["expected_field"])
                except Exception as e:
                    self.assertTrue(case["is_error"])



if __name__ == '__main__':
    unittest.main()
