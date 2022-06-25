class Czeresnie():
    def __init__(self, cena, ilosc, jakosc, sloiki):
        self.cena: int = cena
        self.ilosc: int = ilosc
        self.jakosc: str = jakosc
        self.sloiki: int = sloiki

    def oblicz_cene(self):
        wynik_1 = self.cena * self.ilosc
        return f"Łączna cena to: {wynik_1} Składa się z ceny za kilogram: {self.cena} oraz ilosci kilogramów: {self.ilosc}."

    def sloiki_na_sprzedaz(self):
        wynik_2 = self.cena + self.sloiki
        if self.jakosc == "zla":
            return wynik_2 / 2
        elif self.jakosc == "dobra":
            return wynik_2
        elif self.jakosc == "exclusive":
            return wynik_2 * 2
        else:
            return None


cz = Czeresnie(cena=125, ilosc=10, jakosc= "dobra", sloiki=20)
cena = cz.oblicz_cene()
print(cena)

slo = cz.sloiki_na_sprzedaz()
print(slo)
import os

lista = [2, 4, 8]

pusta_lista = []

for element in lista:
    element_przemnozony = element * 2
    pusta_lista.append(element_przemnozony)

print(pusta_lista)


def mnoznik_razy_dwa(lista):
    pusta_lista = []
    for element in lista:
        element_przemnozony = element * 2
        pusta_lista.append(element_przemnozony)
    return pusta_lista

mn = mnoznik_razy_dwa(lista=[3,6,9, 158, 555])
print(mn)

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CHROMEDRIVER_PATH = os.path.join(ROOT_DIR, "chromedriver\chromedriver.exe")