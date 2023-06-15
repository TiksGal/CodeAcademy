import unittest
from third import kmi

class TestSkaiciavimas(unittest.TestCase):
    def test_kmi(self):
        self.assertEqual(23.54788069073783, kmi(78, 1.82))
        self.assertEqual(20.5456936226167, kmi(50, 1.56))
        self.assertEqual(27.70083102493075, kmi(100, 1.90))
        with self.assertRaises(ValueError):
            kmi(20, 1.40)
        with self.assertRaises(ValueError):
            kmi(240, 1.40)
        with self.assertRaises(ValueError):
            kmi(80, 0.40)
        with self.assertRaises(ValueError):
            kmi(80, 3.40)

if __name__ == '__main__':
    unittest.main()