# pętla for dla listy [1,2,3,4,5,6, True, False, []]
# wyprintuj
a = [1, 2, 3, 4, 5, 6, True, False, []]
for element in a:
    print(element)

# pętla for dla listy [1,2,3,4,5,6, True, False, []]
# element zamień na stringa dodaj "str"
# stwórz nową listę dodaj element

pusta = []
for elementt in a:
    element_na_str = pusta.append(str(elementt))
print(pusta)


# pętla for in range 1-20
# wyprintuj

for elemen in range(1, 21):
    print(elemen)

print()
# pętla z enumerate(licznikiem) dla listy [1,2,3,4,5,6, True, False, []]
# zobacz -> https://realpython.com/python-enumerate/
# wyprintuj
a = [1, 2, 3, 4, 5, 6, True, False, []]

for elem, aa in enumerate(a):
    print(elem, aa)

# pętla dla dicta={1:2, 2:4, 3:5, 6:7, 7:8, 8:9, 10:15}
# wyprintuj
dicta = {1: 2, 2: 4, 3: 5, 6: 7, 7: 8, 8: 9, 10: 15}
petla_dicta = {a: b for a, b in dicta.items()}
print(petla_dicta)

# pętla dla kluczy z dicta={1:2, 2:4, 3:5, 6:7, 7:8, 8:9, 10:15}
# wyprintuj
petla_dla_klucza_dicta = {a for a, b in dicta.items()}
print(petla_dla_klucza_dicta)

# pętla dla wartości z dicta={1:2, 2:4, 3:5, 6:7, 7:8, 8:9, 10:15}
# wyprintuj
petla_dla_wartosci_dicta = {b for a, b in dicta.items()}
print(petla_dla_wartosci_dicta)

# pętla while
# zobacz -> https://analityk.edu.pl/python-petla-for-oraz-while/ przerób przykłady

# krok = 0 to liczba od jakiej zaczyna sie petla, nastepnie dodaje po kazdym okrazeniu +1 i printuje je
#  do 10 jak podane ponizej.
krok = 0
while krok < 10:
    print(krok)
    krok = krok + 1


# niekończąca się petla while True
# Po instrukcji while, następuje warunek, który zawsze jest prawdziwy,
# w związku z czym, pętla powtarza się nieustannie.
while True:
    print("hi")

#  z petli while mozna wyjsc za pomoca break np.
licznik_0 = 0

while True:
    licznik_0 = licznik_0 + 1
    print(licznik_0)
    if licznik_0 > 7:
        print("Wychodzimy z petli za pomoca break.")
        break
print("Petla zostala zakonczona.")