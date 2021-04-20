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

class tabung(bangunRuang):
	"""docstring for bangunRuang"""
	def __init__(self):
			self.nama='Tabung'
	def volume(self,jari2,tinggi):
			self.volume=math.pi*(jari2**2)*tinggi
			return self.volume

class balok(bangunRuang):
	"""dostring for bangunRuang"""
	def __init__(self):
			self.nama='balok'
	def volume(self,p,l,t):
			self.volume=p*l*t
			return self.volume
	
class bola(bangunRuang):
	"""docstring for bangunRuang"""
	def __init__(self):
			self.nama='bola'
	def volume(self,jari2):
			self.volume=4/3*math.pi*(jari2**3)
			return self.volume

cs=bangunRuang()
jari2=int(input("masukan jari2:"))
tinggi=int(input("masukan tinggi:"))
print(cs.volume(jari2,tinggi))
print("================")

bl=balok()
pg=int(input("masukan panjang:"))
tn=int(input("masukan lebar:"))
ti=int(input("masukan tinggi:"))
print(bl.volume(pg,tn,ti))
print("====================")

bo=bola()
jr=int(input("masukan jari2:"))
print(bo.volume(jr))
print("=====================")
