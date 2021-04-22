class buku:

	def __init__(self):
		self.judul_buku=input("judul_buku: ")
		self.tahun_terbit=input("tahun_terbit: ")
		self.nama_pengarang=input("nama_pengarang: ")
		self.penerbit=input("penerbit: ")

	def tampiljml(self):
		jmlbku = 10
		buku.jmlbuku+=10
		print("Total buku:",buku.jmlbku)

	def tampildata(self):
		print("judul_buku:",self.judul_buku)
		print("tahun_terbit:",self.tahun_terbit)
		print("nama_pengarang:",self.nama_pengarang)
		print("penerbit:",self.penerbit)
		print()

print=buku()
