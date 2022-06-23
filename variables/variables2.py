"""
Create new variable, content of this variable
"Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."

print this variable
"""

zdanie_do_wyprintowania = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut " \
                          "labore et dolore magna aliqua."
# print(zdanie_do_wyprintowania)
# print(f"ZADANIE DO WYPRINTOWANIA: {zdanie_do_wyprintowania}")

"""
Please create variables moj_str, moj_int, moj_float, moja_tuple, moja_lista, moj_dict with yours values and print values.
"""
moj_str = "test"
moj_int = 5
moj_float = 2.22
moja_tuple = (10, "jkl")
moja_lista = [20, "lkj"]
moj_dict = {"pies": "dog", "kot": "cat", "liczba": 3}

print(moj_str)
print(moj_int)
print(moj_float)
print(moja_tuple)
print(moja_lista)
print(moj_dict)

"""
Please create variables miejsce, rok, data with yours values
Please print it using "f string"
Result:
"Moje miejsce urodzenia: <miejsce urodzenia>, rok: <rok> , data: <data>"
"""
miejsce, rok, data = [], 2022, 25.05
print(f"Moje miejsce urodzenia:{miejsce}, rok:{rok}, data:{data}")

"""
Create variables imie, wiek in one line and print it, check type of variables
"""

imie, wiek = "Amelka", 3
print(f"imie to:{imie}, wiek to:{wiek}")
print(type(wiek))
print(type(imie))


"""
Create variables x, y, z, k= 1, 2.8, "3", "4.2"
Create new variables x1, y1, z1, k1. Convert old values to float, 
using float() function, print every single value.
"""
x, y, z, k = 1, 2.8, "3", "4.2"
x1 = float(x)
print(x1)
y1 = float(y)
print(y1)
z1 = float(z)
print(z1)
k1 = float(k)
print(k1)

"""
Create variables x, y, z = "s1", 2, 3.0
Create new variables x1, y1, z1. 
Convert old values to string, using str() function, print every single value.
"""
x, y, z = "s1", 2, 3.0
x1 = str(x)
y1 = str(y)
z1 = str(z)
print(x1, y1, z1)

"""
Create variables x, y, z = 1, 2.8, "3"
Create new variables x1, y1, z1. 
Convert old values to int, using int() function, print every single value.
"""

x, y, z = 1, 2.8, "3"
x1 = int(x)
y1 = int(y)
z1 = int(z)
print(x1, y1, z1)

"""
Create variable moja_lista, put into list int, str, empty tuple, list with 1 value.
Please check type of variable moja_list, please print last position of list
"""
moja_lista = [2, "op", (), [1]]
print(type(moja_lista))
print(moja_lista[3])

"""
Create new dict: keys: username, password, you can provide your values.
Print using "f string" values of yours keys:
Result should looks like "My value of key is:
<dict_value> , value of password is: <dict_value>"
"""
moj_slownik = {"username": "jan", "password": "blachowicz"}
print(moj_slownik["username"])
print(moj_slownik["password"])
print(f"My value of key username is:{moj_slownik['username']},"
      f" value of password is:{moj_slownik['password']} ")


# """
# Print 5 position from str variable "Hello World"
# """
# str1 = "Hello World"
# print(str1[4])
#
# """
# Print first 5 position from str variable "Hello World"
# """
# str2 = "Hello World"
# print(str2[0:4])
#
# """
# Print last 5 position from str variable "Hello World"
# """
# str3 = "Hello World"
# print(str3[-5:])
#
# """
# Print variable "Hello World" as "dlroW olleH"
# """
# str4 = "Hello World"
# print(str4[::-1])
#
# """
# Check if "is" in str "Situation on the world is dangerous now"
# """
# str5 = "Situation on the world is dangerous now"
# str6 = "is"
# print(str6 in str5)
# assert str6 in str5, f"If not True than False, {str6} not in {str5}"

# """
# Check if "is" not in str "Situation on the world is dangerous now"
# """
# str7 = "Situation on the world is dangerous now"
# str8 = "is"
# print(str8 not in str7)


# a = 1
# b = 2
# c = 3
#
# print(a > b)
# print(a == b)
# print(a <= b)
# print(a >= b)
# print(a < b > c)

# a = "125"
# b = 124
#
# a1 = int(a)
# print(a1)
# print(type(a1))
# assert b > a1, f"zmienna b:{b} nie jest wieksza od zmiennej a1:{a1}"
# # b > a
#
# tupla 2 pozycja
# lista ostatnia pozycja
# dict stworzyc 2 wartosci drugi klucz- key

okragle = (5, 10, 15, 20)
print(okragle[2])

kwadraty = [10, 20, 30, 40]
print(kwadraty[::-7])

klamry = {"pies":"bulka", "kot":"mial"}
print(klamry["kot"])