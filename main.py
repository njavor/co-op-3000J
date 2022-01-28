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
		
def F21():
    legnagyobb = Tanulo.lista[0].egyuttlakok
    for elem in Tanulo.lista:
        if legnagyobb < elem.egyuttlakok:
            legnagyobb = elem.egyuttlakok
    print(legnagyobb)
    
def F22():
    legnev = Tanulo.lista[0].nev
    legnagyobb = Tanulo.lista[0].egyuttlakok
    for elem in Tanulo.lista:
        if legnagyobb < elem.egyuttlakok:
            legnagyobb = elem.egyuttlakok
            legnev = elem.nev
    print(legnev)    

def F23_24(nem, elso, masodik):
    for elem in Tanulo.lista:
        if elem.nem == nem and (elem.angolcs == elso or elem.angolcs == masodik):
            print(elem.nev)

def F25():
    res = 0
    for elem in Tanulo.lista:
        if not elem.egyuttlakok - elem.testverek == (3 or -3):
            res+=1
    print(res)            

def F26_30(nev):
    i = 0
    while not Tanulo.lista[i].nev == nev:
        i+=1
    for elem in Tanulo.lista:
        if not elem.nev == nev and Tanulo.lista[i].angolcs == elem.angolcs:
            print(elem.nev)

def F31():
    sVn = 0
    for elem in Tanulo.lista:
        if elem.mnyelv == "német":
            sVn+=1
        if elem.mnyelv == "spanyol":
            sVn-=1
    print("Spanyolt tanulnak többen" if sVn>0 else "Németet tanulnak többen" if sVn<0 else "Ugyanannyian tanulnak spanyolt és németet")

def F32(input):
    for elem in Tanulo.lista:
        if elem.mnyelv == input:
            print(elem.nev)                    


print("21) Mekkora a legnagyobb család az osztályban?")
F21()

print("22) Írjuk ki az egyik olyan diák nevét akinek e legtöbb testvére van!")
F22()

print("23) Gyűjtse ki azon lány diákok nevét, akik az egyes vagy kettes angol csoportban vannak!")
F23_24("L","1. Sió","2. Bán")

print("24) Gyűjtse ki azon fiú diákok nevét, akik a hármas vagy négyes angol csoportban vannak és 0 vagy 2 testvérük van!")
F23_24("F","3. Joó","4. Kis")

print("25) Viszonylag kevés azon családok száma, ahol az együttlakók száma és a testvérek száma között nem három a különbség. Adja meg a számukat!")
F25()  

print("26) Dári Dóra hiányzott a legutóbbi angol órán, szeretné bepótolni a hiányzást. Adja meg azon tanulók nevét, akik vele azonos angol csoportba járnak.")
F26_30("Dári Dóra")

print("27) Avon Mór hiányzott a legutóbbi angol órán, szeretné bepótolni a hiányzást. Adja meg azon tanulók nevét, akik vele azonos angol csoportba járnak. ")
F26_30("Avon Mór")

print("28) Zúz Mara hiányzott a legutóbbi angol órán, szeretné bepótolni a hiányzást. Adja meg azon tanulók nevét, akik vele azonos angol csoportba járnak. ")
F26_30("Zúz Mara")

print("29) Citad Ella hiányzott a legutóbbi angol órán, szeretné bepótolni a hiányzást. Adja meg azon tanulók nevét, akik vele azonos angol csoportba járnak.")
F26_30("Citad Ella")

print("30) Hát Izsák hiányzott a legutóbbi angol órán, szeretné bepótolni a hiányzást. Adja meg azon tanulók nevét, akik vele azonos angol csoportba járnak.")
F26_30("Hát Izsák")

print("31) A spanyol vagy a német nyelvet tanulják-e többben az osztáyban?")
F31()       

print("32) Kérjen be a felhasználótól egy nyelvet és írja ki, az adott nyelvet tanulók névsorát!")
F32(input("Melyik második nyelvre vagy kíváncsi?  :  "))		
