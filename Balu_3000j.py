from cmath import tan
import imp
from main import Tanulo

with open("input.txt","r",encoding="utf8") as f:
	for sor in f:
		s = sor.strip().split(";")
		t = Tanulo(int(s[0]), s[1], s[2], s[3], s[4], s[5], int(s[6]), int(s[7]))

print("1) Hány diák tanul az osztályban?")
print(f"{len(Tanulo.lista)} diák tanul az osztályban!")

print("2) Hány fiú tanul az osztályban?")
fiukszama = 0
for tanulo in Tanulo.lista:  
    if(tanulo.nem == "F"):
        fiukszama += 1
print(f"{fiukszama} fiú tanul az osztályba!")

print("3) Hány lány tanul az osztályban?")
lanyokszama = 0
for tanulo in Tanulo.lista:  
    if(tanulo.nem == "F"):
        lanyokszama += 1
print(f"{lanyokszama} lány tanul az osztályba!")

print("4) Hány olyan diák van, akiknek több mint 1 testvére van!")
egytestveresek = 0
for tanulo in Tanulo.lista:  
    if(tanulo.testverek == 1):
        egytestveresek+= 1
print(f"{egytestveresek} egy testvérrel rendelkező diák tanul az osztályban!")

print("5) Gyűjtse ki azon diákok nevét, akiknek több mint 1 testvérük van!")
többtestveresek = 0
for tanulo in Tanulo.lista:  
    if(tanulo.testverek > 1):
        többtestveresek+= 1
print(f"{többtestveresek} több testvérrel rendelkező diák tanul az osztályban!")

print("6) Hány olyan diák van, akiknek több mint 2 testvére van!")
kettőnéltöbbtestveresek = 0
for tanulo in Tanulo.lista:  
    if(tanulo.testverek > 1):
        kettőnéltöbbtestveresek+= 1
print(f"{kettőnéltöbbtestveresek} kettőnél több testvérrel rendelkező diák tanul az osztályban!")

print("7) Gyűjtse ki azon diákok nevét, akiknek több mint 2 testvérük van!")
for tanulo in Tanulo.lista:  
    if(tanulo.testverek > 1):
        print(tanulo.nev)

print("8) Hány olyan diák van, akik a 2. idegen nyelvként a németet tanulják!")
németesek = 0
for tanulo in Tanulo.lista:  
    if(tanulo.mnyelv > "német"):
        németesek+= 1
print(f"{németesek} németes diák tanul az osztályban!")

print("9) Gyűjtse ki azon fiú diákok nevét, akik a 2. idegen nyelvként a németet tanulják!")
for tanulo in Tanulo.lista:  
    if(tanulo.mnyelv > "német" and tanulo.nem == "F"):
        print(tanulo.nev)
        