# Klasa
# Kalkulator
```python
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
```

```python
#funkcja,konstruktory, if,return, else.
class Przedszkole():
    def __init__(self, sala, lawki, tablica, liczba_dzieci):
        self.sala = sala
        self.lawki = lawki
        self.tablica = tablica
        self.liczba_dzieci = liczba_dzieci


    def policz_lawki(self):
        return f"Liczba lawek to: {self.lawki}"


    def policz_dzieci(self):
        return f"Liczba dzieci to: {self.liczba_dzieci}"

    def sprawdz_czy_starczy(self):
        if self.lawki >= self.liczba_dzieci:
            return f"Liczba lawek: {self.lawki} jest wystarczajaca dla {self.liczba_dzieci} dzieci"
        else:
            return f"Liczba lawek: {self.lawki} nie jest wystarczajaca dla {self.liczba_dzieci} dzieci"


prz = Przedszkole(sala=1, lawki=2, tablica=3, liczba_dzieci=4)
zrp = prz.sprawdz_czy_starczy()
print(zrp)


def sprawdz_imie(imie):
    if imie == "Dagmara":
        return f"Prawidlowe imie to: {imie}"
    else:
        return f"Imie {imie} nieprawidlowe"

spr = sprawdz_imie(imie="Dominika")
print(spr)


p = Przedszkole(sala=5, lawki=2, tablica=1, liczba_dzieci=9)
pol = p.policz_lawki()
print(pol)

p = Przedszkole(sala= 1, lawki=10, tablica=1, liczba_dzieci=20)

pol = p.policz_lawki()
print(pol)

spr = p.sprawdz_czy_starczy()
print(spr)

p.lawki = 20
spr = p.sprawdz_czy_starczy()
print(spr)
```