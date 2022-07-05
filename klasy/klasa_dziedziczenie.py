class OwoceIWarzywa():
    def __init__(self, warzywa:dict, owoce:dict):
        self.warzywa = warzywa
        self.owoce = owoce

    def marchewki(self):
        return self.warzywa["marchewka"]

    def ziemniaki(self):
        return self.warzywa["ziemniaki"]

    def kapusta(self):
        return self.warzywa["kapusta"]

    def jablka(self):
        return self.owoce["jablka"]

    def maliny(self):
        return self.owoce["maliny"]

    def jagody(self):
        return self.owoce["jagody"]


class Koszyk(OwoceIWarzywa):
    def __init__(self, warzywa: dict, owoce: dict, nabial: dict, slodycze: dict):
        super().__init__(warzywa, owoce)
        self.warzywa = warzywa
        self.owoce = owoce
        self.nabial = nabial
        self.slodycze = slodycze

    def jogurt(self):
        return self.nabial["jogurt"]

    def mleko(self):
        return self.nabial["mleko"]

    def twarog(self):
        return self.nabial["twarog"]

    def lizaki(self):
        return self.slodycze["lizaki"]

    def czekolada(self):
        return self.slodycze["czekolada"]

    def ciastka(self):
        return  self.slodycze["ciastka"]

    def sumuj_produkty(self, produkty):
        suma = 0
        for wartosc in produkty.values():
            suma = suma + wartosc
        return suma

    def sumuj_koszyk(self):
        nabial = self.sumuj_produkty(self.nabial)
        warzywa = self.sumuj_produkty(self.warzywa)
        owoce = self.sumuj_produkty(self.owoce)
        slodycze = self.sumuj_produkty(self.slodycze)
        suma_wszystkich= nabial+warzywa+owoce+slodycze
        return f"W koszyku znajdują się: nabial={nabial}, warzywa={warzywa}, owoce={owoce} slodycze={slodycze}." \
               f"Łączna kwota koszyka to: {suma_wszystkich}"




_nabial = {"jogurt": 1,"mleko": 5,"twarog": 3}
_warzywa = {"marchewka": 3, "ziemniaki": 1, "kapusta": 4}
_owoce = {"jablka": 2, "maliny": 12, "jagody": 22}
_slodycze = {"lizaki": 10, "czekolada": 13, "ciastka": 24}

koszyk = Koszyk(warzywa=_warzywa, owoce=_owoce, nabial=_nabial, slodycze=_slodycze)
suma_koszyka = koszyk.sumuj_koszyk()
print(suma_koszyka)
