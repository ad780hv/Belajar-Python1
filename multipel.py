class induk(object):
	def __init__(self):
			self.nilai=5

	def get_nilai(self):
			return self.nilai

class anak(induk):
	def get_nilai(self):
			return self.nilai + 1

anak1 = anak()
induk1 = induk()
print(induk1.get_nilai())
print(anak1.get_nilai())
