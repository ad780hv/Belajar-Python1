import math

class bangunRuang(object):
	"""docstring for bangunRuang"""
	def __init__(self):
			super(bangunRuang,self).__init__()
			self.nama='Bangun Ruang'
			self.luasa=None
			self.tinggi=None
	def volume(self,luasa,tinggi):
			self.volume=luasa*tinggi
			return self.volume
	def ubahvolume(self):
			self.luas=input("masukan luas:")
			self.tinggi=input("masukan tinggi:")

class tabung(bangunRuang):
	"""docstring for bangunRuang"""
	def __init__(self):
			self.nama='Tabung'
	def volume(self,jari2,tinggi):
			self.volume=math.pi*(jari2**2)*tinggi
			return self.volume
	def ubahvolume(self):
			self.jari2=input("masukan jari2:")
			self.tinggi=input("masukan tinggi:")

class balok(bangunRuang):
	"""dostring for bangunRuang"""
	def __init__(self):
			self.nama='balok'
	def volume(self,p,l,t):
			self.volume=p*l*t
			return self.volume
	def ubahvolume(self):
			self.panjang=input("masukan panjang:")
			self.lebar=input("masukan lebar:")
			self.tinggi=input("masukan tinggi:")

class bola(bangunRuang):
	"""docstring for bangunRuang"""
	def __init__(self):
			self.nama='bola'
	def volume(self,jari2):
			self.volume=4/3*math.pi*(jari2**3)
			return self.volume
	def ubahvolume(self):
			self.jari2=input("masukan jari2:")

br = bangunRuang()
print(br.volume(27,29))
br.ubahvolume()
print("===================")
tb = tabung()
print(tb.volume(32,36))
tb.ubahvolume()
print("====================")
bl = balok()
print(bl.volume(44,42,40))
print("====================")
bl.ubahvolume()
bo = bola()
print("====================")
print(bo.volume(52))
bo.ubahvolume()
print("====================")

a = tabung()
print("masukan volume tabung")
i=int
