import unittest

from function import validation

class ValidationTestCase(unittest.TestCase):

    def test_valid(self):
        # Массив точек
        points = [[[1, 2], [5, 6]], [[10, 8], [-3, -4]], [[4, 5], [-2, -4]]]

        valid = validation((150, 50), (300, 150), points, 56, 50)
        self.assertEqual(valid, 'Данные валидны')

    def test_not_valid(self):
        points = [[[1, 2], [5, 6]], [[10, 8], [-3, -4]], [[50, 80], [90, 100]]]

        valid = validation((1024, 768), (600, 400), points, 58, 80)
        self.assertEqual(valid, 'Валидация не пройдена')

unittest.main()