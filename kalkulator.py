print ("--------------------------------")
print ("Author: Localhost@15 a.k.a Yudha")
print ("Team: BCA-X666X")
print ("--------------------------------")


angka1 = int(input("Angka1 : "))
angka2 = int(input("Angka2 : "))

def tambah():
	hasil= angka1+angka2
	print (hasil)
	
def kurang():
	hasilPengurangan= angka1 - angka2
	print (hasilPengurangan)
	
def kali():
	hasil= angka1* angka2
	print (hasil)
	
def bagi():
	hasil= angka1/angka2
	print (hasil)
	
print ("hasil pejumlahan adalah:"),tambah()
print ("hasilnya adalah pengurangan:"),kurang()
print ("hasil perkalian adalah:"),kali()
print ("hasil pembagian adalah:"),bagi()