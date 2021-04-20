class hewan:
		def __init__(self):
				self.suara = 'suara'
				self.bulu = 'bulu'
				print(self.suara)
				print(self.bulu)

class kucing(hewan):
		def __init__(self):
			print('==============')
			print('kucing')
			print('==============')
		def suara(self):
			self.suara = input('masukkan suara:')
		def bulu(self):
			self.bulu = input('masukkan bulu:')
		def tampil(self):
			print('suara kucing:',self.suara)
			print('bulu kucing:',self.bulu)

class anjing(hewan):
		def __init__(self):
			print('==============')
			print('anjing')
			print('==============')
		def suara(self):
			self.suara = input('masukkan suara:')
		def bulu(self):
			self.bulu = input('masukkan bulu:')
		def tampil(self):
			print('suara anjing:',self.suara)
			print('bulu anjing:',self.bulu)

h = hewan()
kc = kucing()
kc.suara()
kc.bulu()
anj = anjing()
anj.suara()
anj.bulu()
print()
kc.tampil()
anj.tampil()

