
import unittest
from t import logger

class TestLogger(unittest.TestCase):

    def test_hello_world(self):
        @logger
        def hello_world():
            return 'hello world'

        result = hello_world()
        self.assertEqual(result, 'hello world', "функция возвращает 'hello world'")

    def test_summator(self):
        @logger
        def summator(a, b=0):
            return a + b

        result = summator(2, 2)
        self.assertIsInstance(result, int, "должно вернуться целое число")
        self.assertEqual(result, 4, "2 + 2 = 4")

if __name__ == '__main__':
    unittest.main()
