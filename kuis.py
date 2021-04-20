from __future__ import print_function
	
class dosen:
	def __init__(self, NIP, NAMADOS):
		self.nip = NIP
		self.namados = NAMADOS
	def ubahdos(self):
		self.nip = input("masukan NIP :")
		self.namados = input("masukan NAMA DOSEN:")
class mahasiswa:
	def __init__(self, NIM, NAMA, SEMESTER):
		self.nim = NIM
		self.nama = NAMA
		self.semester = SEMESTER
	def ubahmhs(self):
		self.nim = input("NIM :")
		self.nama = input("Nama Mahasiswa :")
		self.semester = input("Semester :")
class kelas:
	def __init__(self, KODE, LANTAI, GEDUNG):
		self.kodekelas = KODE
		self.lantai = LANTAI
		self.gedung = GEDUNG
	def ubahkls(self):
		self.kodekelas = input("Kode Kelas :")
		self.lantai = input("Lantai :")
		self.gedung = input("Gedung :")
class jadwal(dosen,mahasiswa,kelas):
	def __init__(self):
		self.kode = "-"
		self.hari="-"
		self.tanggal="-"
		self.bulan="-"
		self.tahun="-"
		self.jam = "-"
		self.menit = "-"
		self.nip = "-"
		self.nama ="-"
		self.nim = "-"
		self.nama = "-"
		self.semester = "-"
		self.kodekelas = "-"
		self.lantai = "-"
		self.gedung = "-"
	def ubahjwl(self):
		self.kode = input("masukan kode jadwal :")
		self.hari=input("masukan hari :")
		self.tanggal=input("masukan tanggal :")
		self.bulan=input("masukan bulan :")
		self.tahun=input("masukan tahun :")
		self.jam = input("masukan jam :")
		self.menit = input("masukan menit :")
	def ubahjadwal(self):
		self.kode = input("masukan kode jadwal :")
		self.hari=input("masukan hari :")
		self.tanggal=input("masukan tanggal :")
		self.bulan=input("masukan bulan :")
		self.tahun=input("masukan tahun :")
		self.jam = input("masukan jam :")
		self.menit = input("masukan menit :")
		print("-----DATA DOSEN-----")
		self.nip = input("masukan NIP :")
		self.namados = input("masukan NAMA DOSEN:")
		print("-----DATA MAHASISWA-----")
		self.nim = input("NIM :")
		self.nama = input("Nama Mahasiswa :")
		self.semester = input("Semester :")
		print("------DATA KELAS-----")
		self.kodekelas = input("Kode Kelas :")
		self.lantai = input("Lantai :")
		self.gedung = input("Gedung :")
	def tampilJadwal(self):
		print()
		print('-------------JADWAL--------------')
		print('kode Jadwal :', self.kode)
		print('Hari/tgl :', self.hari,',',self.tanggal,'/',self.bulan,'/',self.tahun)
		print('Waktu :', self.jam,':',self.menit,'WIB')
		print("-------------DOSEN---------------")
		print("NIP :",self.nip)
		print("NAMA DOSEN :",self.namados)
		print("-------------MAHASISWA------------")
		print("NIM :",self.nim)
		print("NAMA MAHASISWA :",self.nama)
		print("SEMESTER :",self.semester)
		print("------------KELAS-------------")
		print("KODE KELAS :", self.kodekelas)
		print("LANTAI :",self.lantai)
		print("GEDUNG :",self.gedung)

k= jadwal()
print("------------masukan jadwal--------------")
k.ubahjadwal()
print("------data jadwal sekarang-------")
k.tampilJadwal()
for i in range(5):
	print()
	j=input("apa ada data yang salah : ")
	if j=="ya":
		print("pilihan :")
		print("1. ubah DOSEN")
		print("2. ubah MAHASISWA")
		print("3. ubah KELAS")
		print("4. ubah JADWAL")
		t=input("masukan pilihan :")
		if t=="1":
			k.ubahdos()
			print()
			print("--------JADWAL SEKARANG--------")
			k.tampilJadwal()
		elif t=="2":
			k.ubahmhs()
			print()
			print("--------JADWAL SEKARANG--------")
			k.tampilJadwal()
		elif t=="3":
			k.ubahkls()
			print()
			print("-------JADWAL SEKARANG---------")
			k.tampilJadwal()
		else:
			k.ubahjwl()
			print()
			print("-------JADWAL SEKARANG---------")
			k.tampilJadwal()
	else:
		k.tampilJadwal()
		print("------TERIMA KASIH------")
		break;