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

# isdecimal()	zwraca True jeśli wszystkie znaki w ciągu są ułamkami dziesiętnymi
print(moj_string.isdecimal())

# isdigit()	zwraca True jeśli wszystkie znaki w ciągu są cyframi
print(moj_string.isdigit())

# # isidentifier()	Returns True if the string is an identifier
# print(moj_string.isidentifier())

# islower()	zwraca True jeśli wszystkie znaki w ciągu są małymi literami
print(moj_string.islower())

# isnumeric()	zwraca True jeśli wszystkie znaki w ciągu są numeryczne
print(moj_string.isnumeric())

# isprintable()	zwraca True jeśli wszystkie znaki w ciągu można wyprintowac
print(moj_string.isprintable())
print()
# isspace() zwraca True jeśli wszystkie znaki w ciągu to spacje
# Returns True if all characters in the string are whitespaces
print(moj_string.isspace())

# istitle()	Returns True if the string follows the rules of a title



# isupper()	Returns True if all characters in the string are upper case
# join()	Joins the elements of an iterable to the end of the string
# ljust()	Returns a left justified version of the string
# lower()	Converts a string into lower case
# lstrip()	Returns a left trim version of the string
# maketrans()	Returns a translation table to be used in translations
# partition()	Returns a tuple where the string is parted into three parts
# replace()	Returns a string where a specified value is replaced with a specified value
# rfind()	Searches the string for a specified value and returns the last position of where it was found
# rindex()	Searches the string for a specified value and returns the last position of where it was found
# rjust()	Returns a right justified version of the string
# rpartition()	Returns a tuple where the string is parted into three parts
# rsplit()	Splits the string at the specified separator, and returns a list
# rstrip()	Returns a right trim version of the string
# split()	Splits the string at the specified separator, and returns a list
# splitlines()	Splits the string at line breaks and returns a list
# startswith()	Returns true if the string starts with the specified value
# strip()	Returns a trimmed version of the string
# swapcase()	Swaps cases, lower case becomes upper case and vice versa
# title()	Converts the first character of each word to upper case
# translate()	Returns a translated string
# upper()	Converts a string into upper case
# zfill()	Fills the string with a specified number of 0 values at the beginning





moj_int = 1
moj_float = 5.55
moja_lista = [10, 100, 1000]
moj_dict = {"slownik":"wartosc", 20:[3,4]}
moja_tupla = (24, 86, "looop")
moj_boolean = True
moj_none = None


