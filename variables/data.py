# https://www.w3schools.com/python/python_datetime.asp
import datetime

#  zwraca aktualna date
x = datetime.datetime.now()
print(x)

#  zwraca rok i nazwe dnia tygodnia

x = datetime.datetime.now()

print(x.year)
print(x.strftime("%A"))

# utworz obiekt daty
x = datetime.datetime(2020, 5, 17)
print(x)

# zwraca nazwe miesiaca
x = datetime.datetime(2018, 6, 1)
print(x.strftime("%B"))


# odniesienie wszystkich kodow do formatowanego pliku
# % zazwraca nazwe dnia tygodnia, wersja skrocona
x = datetime.datetime.now()
print(x.strftime("%a"))

# %A zazwraca nazwe dnia tygodnia, wersja pelna
x = datetime.datetime.now()
print(x.strftime("%A"))

# %w zwraca dzien tygodnia jako liczba 0-6, 0 to niedziela
x = datetime.datetime.now()
print(x.strftime("%w"))

# %d zwraca dzien miesiaca 01-31
x = datetime.datetime.now()
print(x.strftime("%d"))

# %b zazwraca nazwe miesiaca, wersja skrocona
x = datetime.datetime.now()
print(x.strftime("%b"))

# %B zazwraca nazwe miesiaca, wersja pelna
x = datetime.datetime.now()
print(x.strftime("%B"))

# %m zwraca miesiac jako liczbe
x = datetime.datetime.now()
print(x.strftime("%m"))

# %y zwraca rok bez wieku
x = datetime.datetime.now()
print(x.strftime("%y"))

# %Y zraca rok, pelna wersje
x = datetime.datetime.now()
print(x.strftime("%Y"))

# %H zwraca godzine podana od 00 do 23	17
x = datetime.datetime.now()
print(x.strftime("%H"))

# %I zwraca godzine podana od 00 do 12	05
x = datetime.datetime.now()
print(x.strftime("%I"))

# %p zwraca czas wyrazony jako AM/PM	PM
x = datetime.datetime.now()
print(x.strftime("%p"))

# %M zwraca minuty w aktualnej godzinie 00-59	41
x = datetime.datetime.now()
print(x.strftime("%M"))

# %S zwraca sekundy w podanej  00-59	08
x = datetime.datetime.now()
print(x.strftime("%S"))

# %f	Mikrosekunda 000000-999999	548513
x = datetime.datetime.now()
print(x.strftime("%f"))

# %j zwraca numer dnia w ciagu roku 001-366	365
x = datetime.datetime.now()
print(x.strftime("%j"))

# %U Numer tygodnia roku, niedziela jako pierwszy dzień tygodnia,, 00-53	52
x = datetime.datetime.now()
print(x.strftime("%U"))

# %W Numer tygodnia roku, poniedziałek jako pierwszy dzień tygodnia,, 00-53	52
x = datetime.datetime(2018, 5, 31)
print(x.strftime("%W"))

# %c aktuana wersja daty i godziny	Mon Dec 31 17:41:00 2018
x = datetime.datetime.now()
print(x.strftime("%c"))

# %C wiek	20
x = datetime.datetime.now()
print(x.strftime("%C"))

# %x Lokalna wersja daty	12/31/18
x = datetime.datetime.now()
print(x.strftime("%x"))

# %X Lokalna wersja godziny	17:41:00
x = datetime.datetime.now()
print(x.strftime("%X"))
