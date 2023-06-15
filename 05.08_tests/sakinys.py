class Sakinys:
    def __init__(self, tekstas="Laba Diena"):
        self.tekstas = tekstas

    def atbulai(self):
        return self.tekstas[::-1]

    def didziosiomis(self):
        return self.tekstas.upper()

    def mazosiomis(self):
        return self.tekstas.lower()

    def ieskoti(self, ieskomas):
        return self.tekstas.count(ieskomas)

    def pakeisti(self, senas, naujas):
        return self.tekstas.replace(senas, naujas)

    def atspausdintiZodi(self, skaicius):
        suskirstytas = self.tekstas.split()
        return suskirstytas[skaicius]

    def info(self):
        zodziu_kiekis = len(self.tekstas.split())
        skaiciai = sum(i.isnumeric() for i in self.tekstas)
        didziosios = sum(i.isupper() for i in self.tekstas)
        mazosios = sum(i.islower() for i in self.tekstas)
        return {
            "Žodžių kiekis": zodziu_kiekis,
            "Skaičiai": skaiciai,
            "Didžiosios": didziosios,
            "Mažosios": mazosios
        }

    def __str__(self):
        return ("Tekstas: " + self.tekstas)
