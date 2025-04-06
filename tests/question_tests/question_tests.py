#write function tests here, don't add input('') statements here!
import unittest

#follow this example to add questions b, c, and d for testing including their functions
from src.question_a.question_a import test_config, get_fahrenheit
import unittest

class Test_Config(unittest.TestCase):

    def test_question_a_config(self):
        self.assertEqual(True, test_config())

class TestTemperatureConversion(unittest.TestCase):
    def test_get_fahrenheit(self):
        self.assertEqual(get_fahrenheit(0), 32)
        self.assertEqual(get_fahrenheit(5), 41)
        self.assertEqual(get_fahrenheit(10), 50)

#Question B
from src.question_b.question_b import get_assessment_value, get_tax_assessed

class TestPropertyTax(unittest.TestCase):
    def test_get_assessment_value(self):
        self.assertEqual(get_assessment_value(10000), 6000)
        self.assertEqual(get_assessment_value(20000), 12000)

    def test_get_tax_assessed(self):
        self.assertEqual(round(get_tax_assessed(6000), 2), 43.20)
        self.assertEqual(round(get_tax_assessed(10000), 2), 72.00)

#Question C
from src.question_c.question_c import use_local_variable

class TestScopeDemo(unittest.TestCase):
    def test_local_variable_scope(self):
        num = 100
        use_local_variable(num)
        self.assertEqual(num, 100)  # Confirm num is still 100

#Question D
from src.question_d.question_d import get_random_number

class TestGuessGame(unittest.TestCase):
    def test_random_range(self):
        for _ in range(100):
            num = get_random_number()
            self.assertGreaterEqual(num, 1)
            self.assertLessEqual(num, 5)