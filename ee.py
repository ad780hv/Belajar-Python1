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

