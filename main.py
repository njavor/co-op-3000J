"""
Balu: 1-10
Gábor: 11-20
Niki: 21-32
"""

class Tanulo:
	lista = []
	def __init__(self, tkod, dnev, mVt, acs, masodik, no, egylakok, testver):
		self.tanulokod=tkod
		self.nev=dnev
		self.mVt=mVt
		self.angolcs=acs
		self.mnyelv=masodik
		self.nem=no
		self.egyuttlakok=egylakok
		self.testverek=testver
		Tanulo.lista.append(self)

with open("input.txt","r",encoding="utf8") as f:
	for sor in f:
		s = sor.strip().split(";")
		t = Tanulo(int(s[0]), s[1], s[2], s[3], s[4], s[5], int(s[6]), int(s[7]))

#10.
egyes_a_számolás=0
for elem in Tanulo.lista:
    if elem.angolcs=="1. Sió":
        egyes_a_számolás+=1

print("10) Hány diák tanul, az egyes angol csoportban?")
print(egyes_a_számolás)
#-----------------------------------

#11.
kettes_a_számolás=0
for elem in Tanulo.lista:
    if elem.angolcs=="2. Bán":
        kettes_a_számolás+=1

print("11) Hány diák tanul, a kettes angol csoportban?")
print(kettes_a_számolás)
#----------------------------------------

#12

alfa_matek_számolás=0
for elem in Tanulo.lista:
    if elem.mVt=="alfa":
        alfa_matek_számolás+=1

print("12) Hány diák tanul, az alfa matematika csoportban?")
print(alfa_matek_számolás)
#---------------------------------------

#13

beta_matek_számolás=0
for elem in Tanulo.lista:
    if elem.mVt=="beta":
        beta_matek_számolás+=1

print("13) Hány diák tanul, az beta matematika csoportban?")
print(beta_matek_számolás)
#----------------------------------------

#14

alfa_matek_lányok =0
for elem in Tanulo.lista:
    if elem.nem=="L" and elem.mVt=="alfa":
        alfa_matek_lányok+=1

print("14) Hány lány diák tanul, az alfa matematika csoportban?")
print(alfa_matek_lányok)
#-----------------------------------------

#15

beta_matek_lányok =0
for elem in Tanulo.lista:
    if elem.nem=="L" and elem.mVt=="beta":
        beta_matek_lányok+=1

print("15) Hány lány diák tanul, a beta matematika csoportban?")
print(beta_matek_lányok)
#--------------------------------

#16
alfa_matek_fiuk =0
for elem in Tanulo.lista:
    if elem.nem=="F" and elem.mVt=="alfa":
        alfa_matek_fiuk+=1

print("16) Hány fiú diák tanul, az alfa matematika csoportban?")
print(alfa_matek_fiuk)
#--------------------------------

#17

beta_matek_fiuk =0
for elem in Tanulo.lista:
    if elem.nem=="F" and elem.mVt=="beta":
        beta_matek_fiuk+=1
print("17) Hány fiú diák tanul, a beta matematika csoportban?")
print(beta_matek_fiuk)
#------------------------------------

#18

oroszosok=False
i=0
while(not oroszosok and i<len(Tanulo.lista)):
    if Tanulo.lista[i]=="orosz":
        oroszosok=True
    i+=1

print("18) Van-e olyan diák, aki a 2. idegen nyelvként oroszt tanul?")
print(oroszosok)
#------------------------------------

#19

olaszosok=False
j=0
while(not olaszosok and j<len(Tanulo.lista)):
    if Tanulo.lista[j]=="olasz":
        oroszosok=True
    j+=1

print("19) Van-e olyan diák, aki a 2. idegen nyelvként olaszt tanul?")
print (olaszosok)
#-------------------------------------------

#20


spanyolosok=False
h=0
while(not spanyolosok and j<len(Tanulo.lista)):
    if Tanulo.lista[h]=="spanyol":
        spanyolosok=True
    h+=1

print("20) Van-e olyan diák, aki a 2. idegen nyelvként spanyolt tanul?")
print(spanyolosok)