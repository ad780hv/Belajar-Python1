list1 = ['UNJANI', 'sistem informasi', 2019, 2018] 
list2 = [4, 1, 2, 5, 3] 
list3 = ["a", "b", "c", "d"] 
print("List 1: ",list1) 
print("List 2: ",list2) 
print("List 3: ",list3) 
 
# perintah mengurutkan list 2 
list2.sort() 
 
# perintah menambahkan elemen list 3 
list3.append("e") 
 
# menghapus elemen dari list 1 
list1.remove(2019) 
 
print("Panjang List 1: ", len(list1)) 
print("Nilai terbesar pada List 2: ", max(list2)) 
print("Mengurutkan List 2: ", list2) 
print("Menambahkan elemen pada List 3: ", list3) 
print("Menghapus elemen pada List 1: ", list1) 
 