import unittest
from one_hot_encoder import fit_transform


class TestTF(unittest.TestCase):
    def test_basic(self):
        cities = ['Moscow', 'New York', 'Moscow', 'London']
        exp_transformed_cities = [
            ('Moscow', [0, 0, 1]),
            ('New York', [0, 1, 0]),
            ('Moscow', [0, 0, 1]),
            ('London', [1, 0, 0]),
        ]
        transformed_cities = fit_transform(cities)
        self.assertEqual(transformed_cities, exp_transformed_cities)

    def test_ints(self):
        data = [1, 2, 3, 2, 1]
        expected = [
            (1, [0, 0, 1]),
            (2, [0, 1, 0]),
            (3, [1, 0, 0]),
            (2, [0, 1, 0]),
            (1, [0, 0, 1])
        ]
        transformed = fit_transform(data)
        self.assertEqual(expected, transformed)

    def test_not_in(self):
        data = ['A', 'B', 'C', 'C']
        transformed = fit_transform(data)
        self.assertNotIn('D', transformed)

    def test_exception(self):
        data = 1
        with self.assertRaises(TypeError):
            fit_transform(data)


if __name__ == '__main__':
    unittest.main()
