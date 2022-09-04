# napisz klase kolo z ktorej bedzimey dziedziczyc
# w klasie ma sie znajdowac funkcja ktora bedzie zwracala ilosc przedmiotow ktore zawiera klasa

class Kolo():
    def __init__(self, opony, detka, odblaski):
        self.ilosc_kol = 2
        self.opony = opony
        self.detka = detka
        self.odblaski = odblaski

    def ilosc_przedmiotow_w_kolach(self):
        return f"Ilosc przedmiotow w kolach zawiera: opony: {self.opony}, detki: {self.detka}, odblaski: {self.odblaski}."


class Rama():
    def __init__(self, rama, kierownica, siodelko):
        self.rama = rama
        self.kierownica = kierownica
        self.siodelko = siodelko

    def ilosc_przedmiotow_w_ramie(self):
        return f"Rama zawiera: rame: {self.rama}, kierownica: {self.kierownica}, siodelko: {self.siodelko}."


# klasa dziedziczaca po klasie kolo, rama. Zeby dziedziczyc musimy wrzucic klase w nawias przy nazwie klasy, a pozniej
# zainicjowac wszystkie zmienne z tych klas.
class Rower(Kolo, Rama):
    def __init__(self, marka, jakosc, wersja, opony, detka, odblaski, rama, kierownica, siodelko):
        super(Rower, self).__init__(opony, detka, odblaski)
        super(Rower, self).__init__(rama, kierownica, siodelko)
        self.marka = marka
        self.jakosc = jakosc
        self.wersja = wersja
        self.opony = opony
        self.detka = detka
        self.odblaski = odblaski
        self.rama = rama
        self.kierownica = kierownica
        self.siodelko = siodelko

    def zwraca_calosc(self):
        return f"Calosc zawiera: ilosc_przedmiotow_w_ramie: {self.ilosc_przedmiotow_w_ramie()}, \n" \
               f"ilosc_przedmiotow_w_kolach: {self.ilosc_przedmiotow_w_kolach()}, \n" \
               f"marka: {self.marka}, jakosc: {self.jakosc}, wersja: {self.wersja}."


kl_rower = Rower(marka="xd", jakosc=10/10, wersja="sport", opony=2, detka=4, odblaski=6, rama=1, kierownica=1, siodelko=1.25)
zwraca_calosc = kl_rower.zwraca_calosc()
print(zwraca_calosc)
