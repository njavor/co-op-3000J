from main import Tanulo

def Hianyzott(nev):
    i = 0
    while not Tanulo.lista[i].nev == nev:
        i+=1
    for elem in Tanulo.lista:
        if not elem.nev == nev and Tanulo.lista[i].angolcs == elem.angolcs:
            print(elem.nev)

print("21) Mekkora a legnagyobb család az osztályban?")
legnagyobb = Tanulo.lista[0].egyuttlakok
for elem in Tanulo.lista:
    if legnagyobb < elem.egyuttlakok:
        legnagyobb = elem.egyuttlakok
print(legnagyobb)

print("22) Írjuk ki az egyik olyan diák nevét akinek e legtöbb testvére van!")
legnev = Tanulo.lista[0].nev
legnagyobb = Tanulo.lista[0].egyuttlakok
for elem in Tanulo.lista:
    if legnagyobb < elem.egyuttlakok:
        legnagyobb = elem.egyuttlakok
        legnev = elem.nev
print(legnev)

print("23) Gyűjtse ki azon lány diákok nevét, akik az egyes vagy kettes angol csoportban vannak!")
for elem in Tanulo.lista:
    if elem.nem == "L" and (elem.angolcs == "1. Sió" or elem.angolcs == "2. Bán"):
        print(elem.nev)

print("24) Gyűjtse ki azon fiú diákok nevét, akik a hármas vagy négyes angol csoportban vannak és 0 vagy 2 testvérük van!")
for elem in Tanulo.lista:
    if elem.nem == "F" and (elem.angolcs == "3. Joó" or elem.angolcs == "4. Kis"):
        print(elem.nev)

print("25) Viszonylag kevés azon családok száma, ahol az együttlakók száma és a testvérek száma között nem három a különbség. Adja meg a számukat!")
res = 0
for elem in Tanulo.lista:
    if not elem.egyuttlakok - elem.testverek == (3 or -3):
        res+=1
print(res)        

print("26) Dári Dóra hiányzott a legutóbbi angol órán, szeretné bepótolni a hiányzást. Adja meg azon tanulók nevét, akik vele azonos angol csoportba járnak.")
Hianyzott("Dári Dóra")

print("27) Avon Mór hiányzott a legutóbbi angol órán, szeretné bepótolni a hiányzást. Adja meg azon tanulók nevét, akik vele azonos angol csoportba járnak. ")
Hianyzott("Avon Mór")

print("28) Zúz Mara hiányzott a legutóbbi angol órán, szeretné bepótolni a hiányzást. Adja meg azon tanulók nevét, akik vele azonos angol csoportba járnak. ")
Hianyzott("Zúz Mara")

print("29) Citad Ella hiányzott a legutóbbi angol órán, szeretné bepótolni a hiányzást. Adja meg azon tanulók nevét, akik vele azonos angol csoportba járnak.")
Hianyzott("Citad Ella")

print("30) Hát Izsák hiányzott a legutóbbi angol órán, szeretné bepótolni a hiányzást. Adja meg azon tanulók nevét, akik vele azonos angol csoportba járnak.")