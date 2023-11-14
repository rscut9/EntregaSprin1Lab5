import unittest
from division import dividir

class TestDividir(unittest.TestCase):
    def test_dividir(self):
        self.assertEqual(dividir(6, 3), 2)
        self.assertEqual(dividir(-10, 2), -5)
        self.assertEqual(dividir(0, 5), 0)

        with self.assertRaises(ValueError):
            dividir(8, 0)

if __name__ == '__main__':
    unittest.main()