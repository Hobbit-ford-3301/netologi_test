import unittest
import os
from t import logger

class TestMain(unittest.TestCase):

    def test_div(self):
        @logger
        def div(a, b):
            return a / b

        result = div(6, 2)
        self.assertEqual(result, 3, "6 / 2 = 3")

    def test_file_exists(self):
        self.assertTrue(os.path.exists('main.log'), "файл main.log должен существовать")

if __name__ == '__main__':
    unittest.main()