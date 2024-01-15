import unittest
from supabase import Client
from db.db import new_connection
from config.config import Config

class DBTestCase(unittest.TestCase):
    def test_connection(self):
        test_cases :list = [
            {
                "name" : "Should be Successfully",
                "expected" : Client,
                "actual" : new_connection(Config.DATABASE["url"],Config.DATABASE["api_key"]),
                "is_error" : False,
            },
            {
                "name": "Should be failed",
                "expected": None,
                "actual": new_connection(Config.DATABASE["url"]+".id",Config.DATABASE["api_key"]),
                "is_error" : True,
            }
        ]
        for case in test_cases:
            with self.subTest(name=case["name"]):
                try :
                    self.assertEqual(type(case["actual"]), case["expected"])
                except Exception as e:
                    self.assertTrue(case["is_error"])

if __name__ == '__main__':
    unittest.main()
