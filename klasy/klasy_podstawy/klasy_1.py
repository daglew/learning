# tworzenie klasy
class KlasaPierwsza():
    pass


# tworzenie instancji klasy
klasa_pierwsza = KlasaPierwsza()
print()


# tworzenie klasy z zainicjowanymi parametrami na sztywno
class KlasaDruga():
    def __init__(self):
        self.lista = []
        self.nazwa_klasy = "klasa druga"
        self.numer_klasy = 2


klasa_druga = KlasaDruga()
lista_klasy_drugiej = klasa_druga.lista
nazwa_klasy_drugiej = klasa_druga.nazwa_klasy
numer_klasy_drugiej = klasa_druga.numer_klasy
print()


# tworzenie klasy z parametrami z zewnatrz
class KlasaTrzecia():
    def __init__(self, lista, nazwa_klasy, numer_klasy):
        self.lista = lista
        self.nazwa_klasy = nazwa_klasy
        self.numer_klasy = numer_klasy


klasa_trzecia = KlasaTrzecia(lista=[1, 2, 3], nazwa_klasy="klasa trzecia", numer_klasy=3)
lista_klasy_trzeciej = klasa_trzecia.lista
nazwa_klasy_trzeciej = klasa_trzecia.nazwa_klasy
numer_klasy_trzeciej = klasa_trzecia.numer_klasy
print()


# stworz klase i w niej funkcje. Klasa ma przyjmowac parametry z zewnatrz i wewnatrz ( na sztywno przypisane)
class KlasaCzwartaSklep():
    def __init__(self, warzywa, owoce, soki):
        self.warzywa = warzywa
        self.owoce = owoce
        self.soki = soki
        self.nasiona = ()
        self.nabial = "cos tam"

    # funkcja korzystajaca z parametrow klasy
    def dostawy_do_sklepu_wewnetrzne(self):
        return f"Do sklepu dostarczono: warzywa: {self.warzywa}, owoce: {self.owoce}, soki: {self.soki}," \
               f" nasiona: {self.nasiona}, nabial: {self.nabial}"

    # funkcja korzystajaca z parametrow klasy plus parametru zewnetrznego - slodycze
    def dostawy_do_sklepu_wewnetrzne_plus_jedna_zewnetrzna(self, slodycze):
        # return f"Do sklepu dostarczono: warzywa: {self.warzywa}, owoce: {self.owoce}, soki: {self.soki}," \
        #        f" nasiona: {self.nasiona}, nabial: {self.nabial}, slodycze: {slodycze}"
        return f"{self.dostawy_do_sklepu_wewnetrzne()}, slodycze: {slodycze}"

    # funkcja korzystajaca tylko z parametrow zewnetrznych klasy
    # jest to metoda statyczna niekorzysta z konstruktorow klasy oraz nie korzysta z wewnetrznych metod klasy
    # taka metode nazywamy statyczna i dodajemy dekorator @staticmethod
    @staticmethod
    def dostawy_zewnetrzne(napoje, chemia):
        return f"Do sklepu dotarla dostawa zewnetrzna: napoje: {napoje}, chemia: {chemia}."

    # wszystkie dostawy
    def wszystkie_dostawy(self, slodycze, napoje, chemia):
        return f"Dostawa wewnetrzna: {self.dostawy_do_sklepu_wewnetrzne()} \n," \
               f"dostawa wewnetrzna plus jedna zewnetrzna: {self.dostawy_do_sklepu_wewnetrzne_plus_jedna_zewnetrzna(slodycze=slodycze)} \n," \
               f"dostawa zewnetrzna: {self.dostawy_zewnetrzne(napoje=napoje, chemia=chemia)}"

# inicjalizacja klasy
klasa_czwarta = KlasaCzwartaSklep(warzywa=1, owoce=2, soki=3)

# funkcja korzystajaca z parametrow klasy
dostawa_wewnetrzna = klasa_czwarta.dostawy_do_sklepu_wewnetrzne()

# funkcja korzystajaca z parametrow klasy plus parametru zewnetrznego - slodycze
dostawa_wewnetrzna_oraz_jedna_zewnetrzna= klasa_czwarta.dostawy_do_sklepu_wewnetrzne_plus_jedna_zewnetrzna(slodycze="czekolada")

# funkcja korzystajaca tylko z parametrow zewnetrznych klasy
# jest to metoda statyczna niekorzysta z konstruktorow klasy oraz nie korzysta z wewnetrznych metod klasy
 # taka metode nazywamy statyczna i dodajemy dekorator @staticmethod
dostawa_zewnetrzna = klasa_czwarta.dostawy_zewnetrzne(napoje="cola", chemia="e")

wszystkie_dostawy = klasa_czwarta.wszystkie_dostawy(slodycze="lizak", napoje="woda", chemia="domestos")
print(wszystkie_dostawy)
