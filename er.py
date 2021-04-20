class anak:

	def __init__(self,merk,size,jumlah_isi,code_barkot):
		self.merk='Kenko'
		self.size='A5'
		self.jumlah_isi='50 lembar '
		self.code_barkot='8 998838 210116'

	def tampilData(self):
		print('merk:',self.merk)
		print('size:',self.size)
		print('jumlah_isi:',self.jumlah_isi)
		print('code_barkot:',self.code_barkot)

bk = anak("","","","")
q = input('merk:')
w = input('size:')
e = input('jumlah_isi:')
r = input('code_barkot:')

bk.tampilData()

