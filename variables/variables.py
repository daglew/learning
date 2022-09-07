string = "zmienna"
name = "dagmara"

print(name)
print(string)

print(name.upper())
# print(name.upper()) -> nazwa duzymi literami np. DAGMARA

print(name.capitalize())
# print(name.capitalize()) -> nazwa pierwsza litera duża np. Dagmara

imie, nazwisko = "dagmara", "lewandowska"
print(imie, nazwisko)
print(nazwisko[2])
# print(nazwisko[2]) -> trzecia litera nazwiska

print(len(nazwisko))
#  print(len(nazwisko)) -> wyciaga dlugosc znakow

print(f"{imie} {string}")
# print(f"{imie} {string}") -> formatowanie stringow

intiger = 1
print(intiger)

piec = 5
jeden = 1
print(piec+jeden)
# print(piec+jeden) -> dodawanie intow

print(type(piec))
# print(type(piec)) -> sprawdzenie typu zmiennej piec

string_piec = str(piec)
# string_piec = str(piec) -> konwersja int piec do stringa

print(type(string_piec))
# print(type(string_piec)) -> sprawdzalismy typ zmiennej string_piec

print(f"{string_piec}+{jeden}")

moja = "moja"
kotka = "kotka"
dostala = "dostala"
druga = 2
myszke = "myszke"
print(f"{moja} {kotka} {dostala} {druga} {myszke}")

liczba_zmienno_przecinkowa = 1.23
# float -> liczba zmienno przecinkowa
print(liczba_zmienno_przecinkowa)
print(type(liczba_zmienno_przecinkowa))

tupla = (1, 2, 3, "4", 1.25)
print(tupla)
print(tupla[0])
tupla[0] = 0
print(tupla)
# tupla - jest niemutowalna co oznacza ze niemozna w niej podmieniac elementow rozni sie tym od listy oraz nawiasem

lista = [1, 2, 3, "4", 1.25]
print(lista)
print(lista[0])
lista[0] = 0
print(lista)
# lista - jest mutowalna co oznacza w niej podmieniac elementy rozni sie nawiasem

dictionary = {"imie": "dagmara", "nazwisko": "lewandowska"}
print(dictionary)
print(dictionary["imie"])
print(dictionary["nazwisko"])
print(dictionary.values())
print(dictionary.keys())
print(type(dictionary))
# dicty charakteryzuja sie klamrami {} oraz tym ze posiadaja klucz wartosc

string_jeden = "string1"
int_1 = 1
float_1 = 2.22
tupla_1 = (2, 4, 6)
lista_1 = [3, 6, 9, 1.25, "wwww", (), []]
dictionary_1 = {"ma": "moja", "tupla": (), "lista": []}
print(dictionary_1["ma"])
print(dictionary_1["tupla"])
print(dictionary_1["lista"])

# str() -> string np. "string"
# int() -> intiger np.1
# float() -> float np. 1.23
# tuple() -> tupla np. ()
# list() -> lista np. []
# dict() -> dict np. {"klucz": "wartość"}
# None -> nic
# bool() -> boolean np. True albo False

string = "Jol, Hello"
print(string.upper())
# return JOL, HELLO -> podnosi string do gory

print(string.lower())
# return jol, hello -> wszystko z malej

print(string.strip("o"))
# return Jol, Hell -> ucina ostatnie o

print(string.replace("H", "J"))
# return Jol, Jello -> zamienia wszystkie H na J

print(string.split(","))
# return ['Jol', ' Hello'] -> dzieli wyrazy po przecinku (separatorze) wrzuca po przecinku do listy

print(string.capitalize())
# return Jol, hello -> Pierwszy wyraz z duzej

#Nadpisywanie zmiennej
cos = None
print(cos)
# return None

cos = 1
print(cos)
# return 1

#Konwertowanie zmiennych
zmienna = "1"
print(type(zmienna))

zmienna_str_to_int = int(zmienna)
print(type(zmienna_str_to_int))

# warunki
a = 1
b = 2
c = 3

print(a > b)
print(a == b)
print(a <= b)
print(a >= b)
print(a < b > c)


"""
Print 5 position from str variable "Hello World"
"""
str1 = "Hello World"
print(str1[4])

"""
Print first 5 position from str variable "Hello World"
"""
str2 = "Hello World"
print(str2[0:4])

"""
Print last 5 position from str variable "Hello World"
"""
str3 = "Hello World"
print(str3[-5:])

"""
Print variable "Hello World" as "dlroW olleH"
"""
str4 = "Hello World"
print(str4[::-1])

"""
Check if "is" in str "Situation on the world is dangerous now"
"""
str5 = "Situation on the world is dangerous now"
str6 = "is"
print(str6 in str5)
assert str6 in str5, f"If not True than False, {str6} not in {str5}"

"""
Check if "is" not in str "Situation on the world is dangerous now"
"""
str7 = "Situation on the world is dangerous now"
str8 = "is"
print(str8 not in str7)

print()

list_1 = [2, 5, 6, 7, 8]
list_3 = [3, 5, 7, 2, 1]


def element_przez_element(lista):
    list_2 = []
    for element in lista:
        nowy_el = element * element
        list_2.append(nowy_el)
    print(list_2)

element_przez_element(lista=list_1)
print()
element_przez_element(lista=list_3)

x = "Asdads Ttsd"
print(x.rstrip("tsd"))
print("s" in "string")

lista = [1, 3.45, "org", 56]
lista_stringow_z_wykrzyknikami = []
for element in lista:
    konwertowanie_do_stringa = str(element)
    string_plust_wykrzyknik = f"{konwertowanie_do_stringa}!"
    lista_stringow_z_wykrzyknikami.append(string_plust_wykrzyknik)
print(lista_stringow_z_wykrzyknikami)
print()

liczby = [1, 2, 3]
lista_z_liczbami_razy_dwa = [element*2 for element in liczby]
print(lista_z_liczbami_razy_dwa)

fruits = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(fruits[2:5])

