class waktu:
		#def __init__(self,jam=0, menit)=0, detik=0):
		def __init__(self, jam=0, menit=0, detik=0):
				self.jam=jam
				self.menit=menit
				self.detik=detik
		def ubahWaktu(self,jam,menit,detik=0):
				self.jam=jam
				self.menit=menit
				self.detik=detik

class tempat:
		#def __init__(self,nama,latitude,longitude):
		def __init(self):
				self.namaTempat=namaTempat
				self,lattitudr=latitude
				self.longitude

class kalender:
		#def __init__(self,hari,tanggal,bulan,tahun):
		def __init__(self):
				self.hari=hari
				self.tanggal=tanggal
				self.bulan=bulan
				self.tahun=tahun

		def ubahKalender(self,hari,tanggal,bulan,tahun):
				self.hari=hari
				self.tanggal=tanggal
				self.bulan=bulan
				self.tahun=tahun

class jadwal(waktu,tempat,kalender):
		def __init__(self):
				self.namaKegiatan='Kuliah PBO'
				self.jenisKegiatan='Kuliah Teori'
				self.hari='Rabu'
				self.tanggal=6
				self.bulan=3
				self.tahun=2019
				self.jam=11
				self.menit=30
				self.namaTempat='Kampus 1 UNJANI'

		def tampilJadwal(self):
					print('Jadwal')
					print('--------')
					print('Nama Kegiatan:',self.namaKegiatan)
					print('Jenis Kegiatan:',self.jenisKegiatan)
					print('Hari/tgl:',self.hari,',',self.tanggal,'/',self.bulan,'/',self.tahun)
					print('Waktu :',self.jam,':',self.menit,'WIB')
					print('Tempat:',self.namaTempat)
kuliah=jadwal()
kuliah.tampilJadwal()


