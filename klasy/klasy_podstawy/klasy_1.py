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