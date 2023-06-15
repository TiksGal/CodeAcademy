import unittest
from sakinys import Sakinys

class TestSakinys(unittest.TestCase):
    def setUp(self):
        self.sakinys = Sakinys("Mano tekstas yra toks")

    def test_atbulai(self):
        self.assertEqual(self.sakinys.atbulai(), "skot ary satsket onaM")

    def test_didziosiomis(self):
        self.assertEqual(self.sakinys.didziosiomis(), "MANO TEKSTAS YRA TOKS")

    def test_mazosiomis(self):
        self.assertEqual(self.sakinys.mazosiomis(), "mano tekstas yra toks")

    def test_ieskoti(self):
        self.assertEqual(self.sakinys.ieskoti("a"), 3)

    def test_pakeisti(self):
        self.assertEqual(self.sakinys.pakeisti("Mano", "Savo"), "Savo tekstas yra toks")

    def test_atspausdintiZodi(self):
        self.assertEqual(self.sakinys.atspausdintiZodi(2), "yra")

    def test_info(self):
        self.assertDictEqual(self.sakinys.info(), {
            "Žodžių kiekis": 4,
            "Skaičiai": 0,
            "Didžiosios": 1,
            "Mažosios": 17
        })

if __name__ == '__main__':
    unittest.main()
