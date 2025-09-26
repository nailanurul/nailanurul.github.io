#membuat file dan menulis isi
file = open("data.txt","w")
file.write("Halo, Semangat belajar coding!")
file.close

#membuat isi file
file = open("data.txt","r")
print("isi file:")
print(file.read())
file.close()

#menambahkan isi baru ke file
file = open("data.txt","a")
file.write("\nsemangat\yah!")
file.close()

#membuat ulang isi file setelah ditambah
file = open("data.txt","r")
print("isi file terbaru:")
print(file.read())
file.close()
