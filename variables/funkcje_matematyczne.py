# https://www.w3schools.com/python/python_math.asp

import math


lista_przykladowych_liczb = [-1, 7, 14, 8]

#  wyciagniecie minimalnej lub maksymalnej wartosci ze zmiennej lub podanych liczb
x = min(lista_przykladowych_liczb)
y = max(lista_przykladowych_liczb)
print(x)
print(y)

#  zwraca bezwzgledna (dodatnia) wartosc podanej liczby
z = abs(-90.76)
print(z)

# potegowanie - zwraca wartosc x podniesiona do potegi y
# np. x=5, y=3
a = pow(5, 3)
print(a)

# wyciagam pierwiastek z liczby
b = math.sqrt(64)
print(b)

# zaokraglanie do pelnej liczby (int) liczbe (zmiennoprzecinkowa, float)  w gore
c = math.ceil(2.34)
print(c)

# zaokraglanie do pelnej liczby (int) liczbe (zmiennoprzecinkowa, float)  w dol
d = math.floor(1.99)
print(d)

# liczba pi
e = math.pi
print(e)
