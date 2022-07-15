moj_float = 5.55

# zaokragla na koncu zera do jednego miejsca po przecinku (TYLKO ZERA)

x = float("3.500")
print(x)

 # sprawdzam instancje zwraca True lub False
sprawdzam_instancje = isinstance(moj_float, float)
print(sprawdzam_instancje)

# sprawdzam typ
sprawdzam_typ = type(moj_float)
print(sprawdzam_typ)

#  robie f""
przykladowy_fstr = f"Tutaj wklejam zmienna moj float: {moj_float}"
print(przykladowy_fstr)

#  przekonwertowanie liczby na liczbe zmienno przecinkowa
moj_float1 = float(55)
print(moj_float1)
