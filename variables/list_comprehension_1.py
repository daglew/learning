# wykonaj akcje na elemencie a dla kazdego elementu a w liscie w zaleznosci
lista_liczb = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# stworz nowa liste z listy liczb jesli liczba jest podzielna przez 2

lista_1 = [liczba for liczba in lista_liczb if liczba % 2 == 0]
print()

# stworz nowa liste z kazdym elementem pomnozonym przez 2 z listy liczb
lista_2 = [liczba * 2 for liczba in lista_liczb]
print()

# stworz nowa liste z kazdym elementem pomnozonym przez 2 z listy liczb jesli liczba jest wieksza od 5
lista_3 = [liczba * 2 for liczba in lista_liczb if liczba > 5]
print()

# stworz liste z listy liczb ktora bedzie zawierala liczby pomnozone przez 5 jesli liczba jest niearzysta jesli liczba jest wieksza od 3
lista_4 = [liczba * 5 for liczba in lista_liczb if liczba % 2 if liczba > 3]
print()


# result = ['h', 'u', 'm', 'a', 'n']
string1 = 'human'
human = [e for e in string1]
print(human)

# liczby w zakresie do 20 ale tylko parzyste (w zakresie in range(liczba))
# result [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
zakres = [a for a in range(0, 20) if a % 2 == 0]
print(zakres)

# result ['Chb', 'Tdb']
# use lower().endswith('b'), len(name) > 2
names = ['Ch', 'Dh', 'Eh', 'cb', 'Tb', 'Td', 'Chb', 'Tdb']
names_lc = [b for b in names if b.lower().endswith('b') and len(names) > 2]
print()

# sprawdź czy słowo ma a w wyrazie
# result ['apple', 'banana', 'mango']
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
owoce = [c for c in fruits if 'a' in c]
print()

# result ["Apple", "Banana", "Cherry", "Kiwi", "Mango"]
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
owoce_1 = [d.capitalize() for d in fruits]
print()

# result = [iks, igrek, iks, igrek, iks, igrek, iks, igrek]
lista_liter = ["x", "y", "x", "y", "x", "y", "x", "y"]
# lista = [x, y, x, y, x, y, x, y]
litery_wymowa = [e.replace("x", "iks").replace("y", "igrek") for e in lista_liter]
print()
