

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