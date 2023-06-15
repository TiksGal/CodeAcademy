import unittest
import calendar
import datetime


def skaiciu_suma(sk1, sk2, sk3):
    return sk1 + sk2 + sk3


def saraso_suma(sarasas):
    suma = 0
    for skaicius in sarasas:
        suma += skaicius
    return suma


def didziausias_skaicius(*args):
    return max(args)


def stringas_atbulai(stringas):
    return stringas[::-1]


def info_apie_sakini(stringas):
    zodziu_skaicius = len(stringas.split())
    didziosios = 0
    mazosios = 0
    skaiciai = 0
    for simbolis in stringas:
        if simbolis.isupper():
            didziosios += 1
        if simbolis.islower():
            mazosios += 1
        if simbolis.isnumeric():
            skaiciai += 1
    return zodziu_skaicius, didziosios, mazosios, skaiciai


def unikalus_sarasas(sarasas):
    naujas_sarasas = []
    for skaicius in sarasas:
        if skaicius not in naujas_sarasas:
            naujas_sarasas.append(skaicius)
    return naujas_sarasas


def ar_pirminis(skaicius):
    if skaicius > 1:
        for num in range(2, skaicius):
            if skaicius % num == 0:
                return False
        return True
    return False


def isrikiuoti_nuo_galo(sakinys):
    zodziai = sakinys.split()[::-1]
    return " ".join(zodziai)


def ar_keliamieji(metai):
    return calendar.isleap(metai)


def patikrinti_data(sukaktis):
    ivesta_data = datetime.datetime.strptime(sukaktis, "%Y-%m-%d %X")
    now = datetime.datetime.now()
    skirtumas = now - ivesta_data

    return {
        "metai": skirtumas.days // 365,
        "menesiai": skirtumas.days / 365 * 12,
        "savaites": skirtumas.days // 7,
        "dienos": skirtumas.days,
        "valandos": skirtumas.total_seconds() / 3600,
        "minutes": skirtumas.total_seconds() / 60,
        "sekundes": skirtumas.total_seconds()
    }


class TestFunkcijos(unittest.TestCase):
    def test_skaiciu_suma(self):
        self.assertEqual(skaiciu_suma(1, 2, 3), 6)
        self.assertEqual(skaiciu_suma(0, -1, 1), 0)
        self.assertEqual(skaiciu_suma(5, 5, 5), 15)

    def test_saraso_suma(self):
        self.assertEqual(saraso_suma([1, 2, 3, 4]), 10)
        self.assertEqual(saraso_suma([0, -1, 1]), 0)
        self.assertEqual(saraso_suma([-5, -5, 5]), -5)
        self.assertEqual(saraso_suma([-5, -5, 5, 5]), 0)

    def test_didziausias_skaicius(self):
        self.assertEqual(didziausias_skaicius(1, 2, 3), 3)
        self.assertEqual(didziausias_skaicius(0, -1, 1), 1)
        self.assertEqual(didziausias_skaicius(-5, -5, 5, 5), 5)

    def test_stringas_atbulai(self):
        self.assertEqual(stringas_atbulai("Labas"), "sabaL")
        self.assertEqual(stringas_atbulai("abc"), "cba")
        self.assertEqual(stringas_atbulai(" "), " ")

    def test_info_apie_sakini(self):
        self.assertEqual(info_apie_sakini("Labas"), (1, 1, 4, 0))
        self.assertEqual(info_apie_sakini("123"), (1, 0, 0, 3))
        self.assertEqual(info_apie_sakini("abc"), (1, 0, 3, 0))

    def test_unikalus_sarasas(self):
        self.assertEqual(unikalus_sarasas([1, 1, 2, 2, 3, 3]), [1, 2, 3])
        self.assertEqual(unikalus_sarasas([4, 4, 5, 5, 6, 6]), [4, 5, 6])
        self.assertEqual(unikalus_sarasas([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_ar_pirminis(self):
        self.assertTrue(ar_pirminis(2))
        self.assertTrue(ar_pirminis(3))
        self.assertFalse(ar_pirminis(4))

    def test_isrikiuoti_nuo_galo(self):
        self.assertEqual(isrikiuoti_nuo_galo("Vienas du trys keturi"), "keturi trys du Vienas")
        self.assertEqual(isrikiuoti_nuo_galo("a b c d e"), "e d c b a")
        self.assertEqual(isrikiuoti_nuo_galo("1 2 3"), "3 2 1")

    def test_ar_keliamieji(self):
        self.assertTrue(ar_keliamieji(2020))
        self.assertFalse(ar_keliamieji(2100))
        self.assertTrue(ar_keliamieji(2000))

    def test_patikrinti_data(self):
        now = datetime.datetime.now()
        entered_date = datetime.datetime(2000, 1, 1)
        delta = now - entered_date
        years = delta.days // 365
        months = (years * 12) + (delta.days % 365) // 30
        weeks = delta.days // 7
        days = delta.days

        result = patikrinti_data("2000-01-01 00:00:00")
        self.assertEqual(result["metai"], years)
        self.assertAlmostEqual(result["menesiai"], months, delta=1)
        self.assertEqual(result["savaites"], weeks)
        self.assertEqual(result["dienos"], days)


if __name__ == '__main__':
    unittest.main()
