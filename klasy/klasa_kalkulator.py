class Kalkulator():
    # np. Kalkulator(liczba_jeden=2, liczba_dwa=4) -> przyklad wywolania klasy
    def __init__(self, liczba_jeden, liczba_dwa): # konstruktory klasy, dodajemy w inicie ( konstruktory przekazują
                                                  # zmienną przy wywoływaniu, którą podstawimy do zmiennych wewnatrz funkcji init)
        self.liczba_1 = liczba_jeden
        self.liczba_2 = liczba_dwa
        self.lista = []

    def dodawanie(self):
        return self.liczba_1 + self.liczba_2

    def odejmowanie(self):
        return self.liczba_1 - self.liczba_2

    def dzielenie(self):
        return self.liczba_1 / self.liczba_2

    def mnozenie(self):
        return self.liczba_1 * self.liczba_2

    def monozenie_plus_dzielenie(self):
        return self.mnozenie() + self.dzielenie()

    def dodaj_do_listy_wyniki(self):
        self.lista.extend([self.mnozenie(), self.dzielenie(), self.dodawanie(), self.odejmowanie()])

    def print_liczba_jeden_liczba_dwa(self):
        return f"liczba_jeden to: {self.liczba_1}, liczba_dwa to: {self.liczba_2}"

kal = Kalkulator(liczba_jeden=1, liczba_dwa=2)


zmienna_kl = Kalkulator(liczba_jeden=2, liczba_dwa=4)
zmienna_kl.dodaj_do_listy_wyniki()
print(zmienna_kl.lista)

zm_mnozenie = Kalkulator(liczba_jeden=3, liczba_dwa=6)
wynik = zm_mnozenie.mnozenie()
print(zm_mnozenie.mnozenie())
print(zm_mnozenie.lista)
zm_mnozenie.dodaj_do_listy_wyniki()
print(zm_mnozenie.lista)

lista_imion_do_zmiany = ["antek", "jola", "kasia", "artur", "magda"]
lista_imion_do_zmiany_2 = ["oskar", "tosia", "klara", "ewa"]


lista_imion_duze = []


def zmien_imie(lista_imion):
    for imie in lista_imion:
        imie_new = imie.capitalize()
        lista_imion_duze.append(imie_new)


zmien_imie(lista_imion=lista_imion_do_zmiany)
print(lista_imion_duze)
lista_imion_duze.clear()


zmien_imie(lista_imion=lista_imion_do_zmiany_2)
print(lista_imion_duze)





