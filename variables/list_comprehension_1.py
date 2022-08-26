# wykonaj akcje na elemencie a dla kazdego elementu a w liscie w zaleznosci
lista_liczb = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# stworz nowa liste z listy liczb jesli liczba jest podzielna przez 2

lista_1 = [liczba for liczba in lista_liczb if not liczba % 2]
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