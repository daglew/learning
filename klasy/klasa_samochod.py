class Samochod():
    def __init__(self, kierowca, wiek, marka):
        self.kierowca= kierowca
        self.wiek = wiek
        self.marka = marka

    def info_o_kierowcy(self):
        return f"Kierowca to {self.kierowca} ma {self.wiek} lat. Jezdzi samochodem marki {self.marka}, " \
               f"sprawdz wiek kierowcy: {self.sprawdz_wiek_kierowcy()} "

    def sprawdz_wiek_kierowcy(self):
        if self.wiek >= 18:
            return f"Wiek kierowcy to:{self.wiek} jest uprawniony do prowadzenia pojazdow."
        else:
            return f"Wiek kierowcy to:{self.wiek} nie jest uprawniony do prowadzenia pojazdow."


c = Samochod(kierowca="Michal", wiek=20, marka= "ford")
inf = c.info_o_kierowcy()
print(inf)