# klasa abstrakcyjna jest to klasa ktora sie dziedziczy do innych klas o danym modelu klasy,
# klasy dziedziczonce ta klase musza posiadac te same funkcje wewnatrz.
from abc import ABCMeta, abstractmethod


class KlasaAbstrakcyjna(metaclass=ABCMeta):
    @abstractmethod

