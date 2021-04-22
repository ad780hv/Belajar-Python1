d_nilai = { 
 'andi':'A', 
 'budi':'B', 
 'citra':'C', 
 'hendra':'A', 
 'baron':'D' 
} 
 
print("daftar nilai: ",d_nilai) 
# mengecek panjang dictionary 
print("panjang dictionary: ",len(d_nilai),"\n") 
 
# merubah entry yang sudah ada 
d_nilai['citra']='B' 
print("perubahan 1: ",d_nilai) 
 
# menambah entry baru 
d_nilai['tony']='A' 
print("perubahan 2: ",d_nilai) 
# mengecek panjang dictionary 
print("panjang dictionary: ",len(d_nilai),"\n") 
 
# menghapus entry 
del d_nilai['citra'] 
print("perubahan 3: ",d_nilai) 
print("panjang dictionary: ",len(d_nilai),"\n") 
 
# mengosongkan dictionary 
d_nilai.clear() 
print("perubahan 4: ",d_nilai) 
print("panjang dictionary: ",len(d_nilai),"\n") 
