from main import Tanulo

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
print("24) Gyűjtse ki azon fiú diákok nevét, akik a hármas vagy négyes angol csoportban vannak és 0 vagy 2 testvérük van!")
print("25) Viszonylag kevés azon családok száma, ahol az együttlakók száma és a testvérek száma között nem három a különbség. Adja meg a számukat!")
print("26) Dári Dóra hiányzott a legutóbbi angol órán, szeretné bepótolni a hiányzást. Adja meg azon tanulók nevét, akik vele azonos angol csoportba járnak.")
print("27) Avon Mór hiányzott a legutóbbi angol órán, szeretné bepótolni a hiányzást. Adja meg azon tanulók nevét, akik vele azonos angol csoportba járnak. ")
print("28) Zúz Mara hiányzott a legutóbbi angol órán, szeretné bepótolni a hiányzást. Adja meg azon tanulók nevét, akik vele azonos angol csoportba járnak. ")
print("29) Citad Ella hiányzott a legutóbbi angol órán, szeretné bepótolni a hiányzást. Adja meg azon tanulók nevét, akik vele azonos angol csoportba járnak.")
print("30) Hát Izsák hiányzott a legutóbbi angol órán, szeretné bepótolni a hiányzást. Adja meg azon tanulók nevét, akik vele azonos angol csoportba járnak.")