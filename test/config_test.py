import unittest
from config.config import Config

class ConfigTestCase(unittest.TestCase):
    def test_database_config(self):
        test_cases = [
            {
                "name": "Should return database API key",
                "expected": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im14cnpxcWJzbmp5dGd4end4bHliIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MTM3NTI1NDgsImV4cCI6MjAyOTMyODU0OH0.xv3Ciws_StrFit7-_QwSfbjK6R5pnPrOfYeV5586lxQ",
                "actual": Config.DATABASE["api_key"]
            },
            {
                "name": "Should return database URL",
                "expected": "https://mxrzqqbsnjytgxzwxlyb.supabase.co",
                "actual": Config.DATABASE["url"]
            }
        ]
        for case in test_cases:
            with self.subTest(name=case["name"]):
                self.assertEqual(case["actual"], case["expected"])



if __name__ == '__main__':
    unittest.main()
