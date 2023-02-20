class Ajanlat():
    def __init__(self, sorszam:int, csapat:str, helyezes:int, ev:int, helyszin:str):
        self.sorszam = sorszam
        self.csapat = csapat
        self.helyezes = helyezes
        self.ev = ev
        self.helyszin = helyszin

def beolvas(fajlnev:str):
    with open(fajlnev, "r", encoding = "utf8") as file:
        lista = []
        for sor in file:
            sortomb = sor.strip().split('\t')
            lista.append(Ajanlat(int(sortomb[0]), sortomb[1], int(sortomb[2]), int(sortomb[3]), sortomb[4]))
        return lista
lista =  beolvas("input.txt")

def orszaghelyezesek(orszag: str):
    return [(x.helyezes, x.ev, x.helyszin) for x in lista if x.csapat == orszag]
print(orszaghelyezesek("Magyarország"))
print(orszaghelyezesek("Anglia"))
print(orszaghelyezesek("Chile"))
print(orszaghelyezesek("Peru"))
print(orszaghelyezesek("Mongólia"))




