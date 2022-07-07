moj_string = "moj string"
# sprawdzenie instancji
sprawdzam_instancje = isinstance(moj_string, str)
print(sprawdzam_instancje)

# sprawdzam typ
sprawdzam_typ = type(moj_string)
print(sprawdzam_typ)

#  wyciagam wartosc
wyciagam_indeks_5 = moj_string[5]
print(wyciagam_indeks_5)

#  iteruje po stringu
for element in moj_string:
    print(element)

#  robie f""
przykladowy_fstr = f"Tutaj wklejam zmienna moj string:{moj_string}"
print(przykladowy_fstr)

#  wykonuje operacje na instancji klasy moj_string

# capitalize()	podnies pierwsza litere
print(moj_string.capitalize())

# casefold()	zamienia str na wszystkie mala litera
print(moj_string.casefold())

# count()	zlicza ilosc podanej frazy w str, zwraca inta
print(moj_string.count("s"))

# endswith()	sprawdza czy str konczy sie na podana fraze
print(moj_string.endswith("inf"))

# find()	pokazuje pierwszy indeks w str, zwraca int
print(moj_string.find("st"))

# format()	wstawia w klamre podana fraze do funkcji format, czyli f"" tylko bardziej skomplikowany
print("{}".format(moj_string))

# index()	wyszukuje po wartosci str jego indeks
print(moj_string.index("o"))

# isalnum()	zwraca True lub False jesli str zawiera tylko liter z zakresu A-Z i cyfry z zakresu 0-9
print("AZ09".isalnum())

# isalpha()	zwraca True jesli w stringu sa same litery (bez spacji)
print(moj_string.isalpha())

# isdecimal()	zwraca True jeśli wszystkie znaki w str są ułamkami dziesiętnymi
print(moj_string.isdecimal())

# isdigit()	zwraca True jeśli wszystkie znaki w str są cyframi
print(moj_string.isdigit())

# # isidentifier()	zwraca True jeśli str jest identyfikatorem
print(moj_string.isidentifier())

# islower()	zwraca True jeśli wszystkie znaki w str są małymi literami
print(moj_string.islower())

# isnumeric()	zwraca True jeśli wszystkie znaki w str są numeryczne
print(moj_string.isnumeric())

# isprintable()	zwraca True jeśli wszystkie znaki w str można wyprintowac
print(moj_string.isprintable())

# isspace() zwraca True jeśli wszystkie znaki w str to spacje
print(" ".isspace())
print(moj_string.isspace())

# istitle()	zwraca True jeśli str przestrzega zasad tytułu
print(moj_string.istitle())

# join()	Łączy elementy stringa np. spacja ktora wprowadzilam do str
print(" ".join(("John", "Peter", "Vicky")))

# lower()	Konwertuje str na calosc malymi literami
print(moj_string.lower())

# lstrip()	Zwraca lewa wersja wykończenia string
print(moj_string.lstrip())

# replace()	Zwraca str gdzie okreslona  wartosc jest zastępowana inna określoną wartością
print(moj_string.replace("string", "dom"))

# rfind()	Przeszukuje str pod kątem określonej wartości i zwraca ostatnią pozycję, w której została znaleziona
print(moj_string.rfind("moj"))

# rpartition()	Zwraca tuple, w której łańcuch jest podzielony na trzy części
print(moj_string.rpartition("moj"))

# rsplit()	Dzieli ciąg znaków(str) według określonego separatora i zwraca listę
print("apple, banana, cherry".rsplit(", "))

# rstrip()	Zwraca odpowiednią wersję przycięcia str
print(moj_string.rstrip())

# split()	Dzieli str w określonym separatorze i zwraca listę
print(moj_string.split())

# splitlines()	Dzieli łańcuch w miejscu łamania linii i zwraca listę
print(moj_string.splitlines())

# startswith()	Zwraca true, jeśli str zaczyna się od określonej wartości
print(moj_string.startswith("m"))

# strip()	Zwraca przyciętą wersję str
print(moj_string.strip())

# swapcase()  # Zamienia litery, małe litery stają się dużymi i na odwrót
print(moj_string.swapcase())

# title()	Zamienia pierwszy znak każdego słowa na wielkie litery
print(moj_string.title())

# # translate()	Zwraca przetłumaczony str
# print(moj_string.translate())
# print()

# upper()	Konwertuje napis na wielkie litery
print(moj_string.upper())

# zfill()	Wypełnia str określoną liczbą wartości 0 na początku
print(moj_string.zfill(21))





moj_int = 1
moj_float = 5.55
moja_lista = [10, 100, 1000]
moj_dict = {"slownik":"wartosc", 20:[3,4]}
moja_tupla = (24, 86, "looop")
moj_boolean = True
moj_none = None


