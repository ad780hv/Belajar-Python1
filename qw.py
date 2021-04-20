class buku:

	def __init__(self):
		self.judul_buku=input("judul_buku: ")
		self.tahun_terbit=input("tahun_terbit: ")
		self.nama_pengarang=input("nama_pengarang: ")
		self.penerbit=input("penerbit: ")

	def tampildata(self):
		self.editor=input("editor:")
		self.desain=input("desain_cover:")
		self.daftar=input("daftar_pustaka:")
		print()

print("=============silakan pilih buku yang anda sukai==============")

print("buku")
bku=buku()
print("tampildata")
print("tampilkan editor:Ignas ")
print("tampilkan desain_cover:Andang")
print("tampilkan daftar_pustaka:http://www.w3schools.com/bootstrap/")
print("====================")

class novel(buku):
	def __init__(self):
		buku.__init__(self)
		self.tebal=input("tebal_halaman:")
		self.alur=input("alur_yang_digunakan:")
		self.genre=input("genre:")
		self.latar=input("latar_tempat:")
		self.tokoh=input("nama_tokoh:")

	def tampilkan_data(self):
		self.hak_cipta=input("Masukan hak_cipta:")
		self.larangan=input("Masukan hal yang tidak boleh dilakukan: ")

print("novel")
no=novel()
print("hak_cipta dilindungi oleh undang-undang")
print("dilarang keras memfotokopi atau memperbanyak sebagian atau seluruh isi buku tanpa izin tertulis dari penerbit")
print("=====================")

class komik(buku):
	def __init__(self):
		buku.__init__(self)
		self.gambar=input("gambar:")
		self.bahasa=input("bahasa_yang digunakan:")
		self.seri=input("seri_ke:")
		self.kategori=input("kategori:")

	def tampilkan_data(self):
		self.hak_cipta=input("Masukan hak_cipta:")
		self.larangan=input("Masukan hal yang tidak boleh dilakukan: ")

print("komik")
km=komik()
print("hak_cipta dilindungi oleh undang-undang")
print("dilarang keras memfotokopi atau memperbanyak sebagian atau seluruh isi buku tanpa izin tertulis dari penerbit")
print("=====================")

class majalah(buku):
	def __init__(self):
		buku.__init__(self)
		self.gambar=input("gambar:")
		self.website=input("website:")
		self.no_tlp=input("no_tlp:")
		self.volume=input("volume_ke:")

	def tampilkan_data(self):
		self.hak_cipta=input("Masukan hak_cipta:")
		self.larangan=input("Masukan hal yang tidak boleh dilakukan: ")
	
print("majalah")
mj=majalah()
print("hak_cipta dilindungi oleh undang-undang")
print("dilarang keras memfotokopi atau memperbanyak sebagian atau seluruh isi buku tanpa izin tertulis dari penerbit")
print("=====================")

class buku_pelajaran(buku):
	def __init__(self):
		buku.__init__(self)
		self.jumlah=input("jumlah_bab:")
		self.materi=input("materi_yang_dibahas:")
		self.gambar=input("gambar:")
		self.indeks=input("indeks:")

	def tampilkan_data(self):
		self.hak_cipta=input("Masukan hak_cipta:")
		self.larangan=input("Masukan hal yang tidak boleh dilakukan: ")

print("buku pelajaran")
bk=buku_pelajaran()
print("hak_cipta dilindungi oleh undang-undang")
print("dilarang keras memfotokopi atau memperbanyak sebagian atau seluruh isi buku tanpa izin tertulis dari penerbit")
print("=====================")


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
print("===============")