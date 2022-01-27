"""
Megoldatlan: 1-32
"""

from _1 import egy
from _2 import ketto
from _3 import harom
from _4 import negy
from _5 import ot
from _6 import hat
from _7 import het
from _8 import nyolc
from _9 import kilenc
from _10 import tiz
from _11 import tizenegy
from _12 import tizenketto
from _13 import tizenharom
from _14 import tizennegy
from _15 import tizenot
from _16 import tizenhat
from _17 import tizenhet
from _18 import tizennyolc
from _19 import tizenkilenc
from _20 import husz
from _21 import huszonegy
from _22 import huszonketto
from _23 import huszonharom
from _24 import huszonnegy
from _25 import huszonot
from _26 import huszonhat
from _27 import huszonhet
from _28 import huszonnyolc
from _29 import huszonkilenc
from _30 import harminc
from _31 import harmincegy
from _32 import harmincketto

lista = []
with open("input.txt","r",encoding="utf8") as f:
	for sor in f:
		lista.append(int(sor))

print("1) Hány diák tanul az osztályban?")
print("2) Hány fiú tanul az osztályban?")
print("3) Hány lány tanul az osztályban?")
print("4) Hány olyan diák van, akiknek több mint 1 testvére van!")
print("5) Gyűjtse ki azon diákok nevét, akiknek több mint 1 testvérük van!")
print("6) Hány olyan diák van, akiknek több mint 2 testvére van!")
print("7) Gyűjtse ki azon diákok nevét, akiknek több mint 2 testvérük van!")
print("8) Hány olyan diák van, akik a 2. idegen nyelvként a németet tanulják!")
print("9) Gyűjtse ki azon fiú diákok nevét, akik a 2. idegen nyelvként a németet tanulják!")
print("10) Hány diák tanul, az egyes angol csoportban?")
print("11) Hány diák tanul, a kettes angol csoportban?")
print("12) Hány diák tanul, az alfa matematika csoportban?")
print("13) Hány diák tanul, az beta matematika csoportban?")
print("14) Hány lány diák tanul, az alfa matematika csoportban?")
print("15) Hány lány diák tanul, a beta matematika csoportban?")
print("16) Hány fiú diák tanul, az alfa matematika csoportban?")
print("17) Hány fiú diák tanul, a beta matematika csoportban?")
print("18) Van-e olyan diák, aki a 2. idegen nyelvként oroszt tanul?")
print("19) Van-e olyan diák, aki a 2. idegen nyelvként olaszt tanul?")
print("20) Van-e olyan diák, aki a 2. idegen nyelvként spanyolt tanul?")
print("21) Mekkora a legnagyobb család az osztályban?")
print("22) Írjuk ki az egyik olyan diák nevét akinek e legtöbb testvére van!")
print("23) Gyűjtse ki azon lány diákok nevét, akik az egyes vagy kettes angol csoportban vannak!")
print("24) Gyűjtse ki azon fiú diákok nevét, akik a hármas vagy négyes angol csoportban vannak és 0 vagy 2 testvérük van!")
print("25) Viszonylag kevés azon családok száma, ahol az együttlakók száma és a testvérek száma között nem három a különbség. Adja meg a számukat!")
print("26) Dári Dóra hiányzott a legutóbbi angol órán, szeretné bepótolni a hiányzást. Adja meg azon tanulók nevét, akik vele azonos angol csoportba járnak.")
print("27) Avon Mór hiányzott a legutóbbi angol órán, szeretné bepótolni a hiányzást. Adja meg azon tanulók nevét, akik vele azonos angol csoportba járnak. ")
print("28) Zúz Mara hiányzott a legutóbbi angol órán, szeretné bepótolni a hiányzást. Adja meg azon tanulók nevét, akik vele azonos angol csoportba járnak. ")
print("29) Citad Ella hiányzott a legutóbbi angol órán, szeretné bepótolni a hiányzást. Adja meg azon tanulók nevét, akik vele azonos angol csoportba járnak.")
print("30) Hát Izsák hiányzott a legutóbbi angol órán, szeretné bepótolni a hiányzást. Adja meg azon tanulók nevét, akik vele azonos angol csoportba járnak.")
print("31) A spanyol vagy a német nyelvet tanulják-e többben az osztáyban?")
print("32) Kérjen be a felhasználótól egy nyelvet és írja ki, az adott nyelvet tanulók névsorát!")
