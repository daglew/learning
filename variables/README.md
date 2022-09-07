```python

 str() #-> string np. "string"
 int() #-> intiger np.1
 float() #-> float np. 1.23
 tuple() #-> tupla np. ()
 list() #-> lista np. []
 dict() #-> dict np. {"klucz": "wartość"}
 None #-> nic
 bool() #-> boolean np. True albo False
```
```python

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
```
```python
string = "zmienna"
name = "dagmara"

print(name)
print(string)

print(name.upper())
print(name.upper()) #-> nazwa duzymi literami np. DAGMARA

print(name.capitalize())
print(name.capitalize()) #-> nazwa pierwsza litera duża np. Dagmara

imie, nazwisko = "dagmara", "lewandowska"
print(imie, nazwisko)
print(nazwisko[2])
print(nazwisko[2]) #-> trzecia litera nazwiska

print(len(nazwisko))
print(len(nazwisko)) #-> wyciaga dlugosc znakow

print(f"{imie} {string}")
print(f"{imie} {string}") #-> formatowanie stringow
```
```python
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
```

```python
# print(piec+jeden) -> dodawanie intow
piec = 5
jeden = 1
print(piec+jeden)

# print(type(piec)) -> sprawdzenie typu zmiennej piec
print(type(piec))

# string_piec = str(piec) -> konwersja int piec do stringa
string_piec = str(piec)

# print(type(string_piec)) -> sprawdzalismy typ zmiennej string_piec
print(type(string_piec))

print(f"{string_piec}+{jeden}")

```
```python
# float -> liczba zmienno przecinkowa
liczba_zmienno_przecinkowa = 1.23
print(liczba_zmienno_przecinkowa)
print(type(liczba_zmienno_przecinkowa))
```

```python
tupla = (1, 2, 3, "4", 1.25)
print(tupla)
print(tupla[0])
tupla[0] = 0
print(tupla)
# tupla - jest niemutowalna co oznacza ze niemozna w niej podmieniac elementow rozni sie tym od listy oraz nawiasem
```
```python
lista = [1, 2, 3, "4", 1.25]
print(lista)
print(lista[0])
lista[0] = 0
print(lista)
# lista - jest mutowalna co oznacza w niej podmieniac elementy rozni sie nawiasem
```
```python
dictionary = {"imie": "dagmara", "nazwisko": "lewandowska"}
print(dictionary)
print(dictionary["imie"])
print(dictionary["nazwisko"])
print(dictionary.values())
print(dictionary.keys())
print(type(dictionary))
# dicty charakteryzuja sie klamrami {} oraz tym ze posiadaja klucz wartosc
```
```python
string_jeden = "string1"
int_1 = 1
float_1 = 2.22
tupla_1 = (2, 4, 6)
lista_1 = [3, 6, 9, 1.25, "wwww", (), []]
dictionary_1 = {"ma": "moja", "tupla": (), "lista": []}
print(dictionary_1["ma"])
print(dictionary_1["tupla"])
print(dictionary_1["lista"])
```
```python

```