class mahasiswa:
	'dasar kelas untuk semua mahasiswa'
	jmlMhs = 0
	def __init__ (self,nama,prodi,nim,jenis_kelamin,umur):
		self.nama='nama'
		self.prodi='prodi'
		self.__jenis_kelamin='Perempuan'
		self.__umur='18 Tahun'
		mahasiswa.jmlMhs+=1
	def tampilJml(self):
		print("Total Mahasiswa:",mahasiswa.jmlMhs)
	def tampilProfil(self):
		print("Nama:",self.nama)
		print("Prodi:",self.prodi)
		print("Nim:",self.nim)
		print("jenis_kelamin:",self.__jenis_kelamin)
		print("umur:",self.__umur)
		

mhs1=mahasiswa('','','','','')

name=input("nama: ")
sp=input("prodi: ")
sn=input("nim: ")
sy=input("jenis_kelamin: ")
so=input("umur:")

setattr(mhs1,'nama',name)
setattr(mhs1,'prodi',sp)
setattr(mhs1,'nim',sn)
setattr(mhs1,'jenis_kelamin',sy)
setattr(mhs1,'umur',so)

print()
mhs1.tampilProfil()

