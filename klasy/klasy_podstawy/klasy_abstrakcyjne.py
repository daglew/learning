# klasa abstrakcyjna jest to klasa ktora sie dziedziczy do innych klas o danym modelu klasy,
# klasy dziedziczonce ta klase musza posiadac te same funkcje wewnatrz.
from abc import ABCMeta, abstractmethod


class KlasaAbstrakcyjna(metaclass=ABCMeta):
    @abstractmethod
    def jeden(self, parametr_jeden):
        return NotImplemented

    @abstractmethod
    def dwa(self, parametr_dwa, parametr_trzy):
        return NotImplemented

    @abstractmethod
    def trzy(self, parametr_cztery):
        return parametr_cztery


class KlasaDziedziczacaJeden(KlasaAbstrakcyjna):
    def jeden(self, parametr_jeden):
        return parametr_jeden

    def dwa(self, parametr_dwa, parametr_trzy):
        return parametr_dwa, parametr_trzy

    def trzy(self, parametr_cztery):
        return parametr_cztery


class KlasaDziedziczacaDwa(KlasaAbstrakcyjna):
    def jeden(self, parametr_jeden):
        return parametr_jeden * parametr_jeden

    def dwa(self, parametr_dwa, parametr_trzy):
        return parametr_dwa * parametr_dwa, parametr_trzy * parametr_trzy

    def trzy(self, parametr_cztery):
        return parametr_cztery * parametr_cztery


klasa_1 = KlasaDziedziczacaJeden()
Klasa_1_funkcja_3 = klasa_1.trzy(parametr_cztery=4)
print()

klasa_2 = KlasaDziedziczacaDwa()
klasa_2_funkcja_3 = klasa_2.trzy(parametr_cztery=2)
print()