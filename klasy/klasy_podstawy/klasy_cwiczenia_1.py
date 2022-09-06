class Kalkulator():
    def __init__(self, liczba_1, liczba_2):
        self.liczba_1 = liczba_1
        self.liczba_2 = liczba_2

    def dodawanie(self):
        return self.liczba_1 + self.liczba_2

    def odejmowanie(self):
        return self.liczba_1 - self.liczba_2

    def mnozenie(self):
        return self.liczba_1 * self.liczba_2

    def dzielenie(self):
        return self.liczba_1 / self.liczba_2

    @property
    def liczba_trzy(self):
        return 3


kalkulator_wywolanie = Kalkulator(liczba_1=1, liczba_2=2)
kal_dodawanie = kalkulator_wywolanie.dodawanie()
kal_trzy = kalkulator_wywolanie.liczba_trzy
print()
