moj_int = 1


# zaokragla liczbe zmienno przecinkowa. Funkcja int() konwertuje określoną wartość na liczbę całkowitą.

x = int(3.5)
print(x)

# konwertowanie str na int
y = int("12")
print(y)

#  dodawanie
jeden = 1
dwa = 2
print(jeden+dwa)

#  odejmowanie
jeden_3 = 3
dwa_2 = 2
print(jeden_3-dwa_2)

# mnozenie
trzy = 3
dwa = 2
print(trzy*dwa)

# dzielenie
cztery = 4
dwa_2 = 2
print(cztery/dwa_2)

#  wywolanie funkcji dodawania


def dodawanie_liczb(liczba_1, liczba_2):
    wynik=liczba_1+liczba_2
    return wynik


wwyy = dodawanie_liczb(liczba_1=1, liczba_2=2)
print(wwyy)


# wywoływanie wartosci int po indeksie
d = 1, 2, 3
print(d[0])

 # sprawdzam instancje zwraca True lub False
sprawdzam_instancje = isinstance(moj_int, int)
print(sprawdzam_instancje)

# sprawdzam typ
sprawdzam_typ = type(moj_int)
print(sprawdzam_typ)

#  robie f""
przykladowy_fstr = f"Tutaj wklejam zmienna moj int:{moj_int}"
print(przykladowy_fstr)
