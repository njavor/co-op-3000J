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