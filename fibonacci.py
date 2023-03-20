#Menghitung huruf vokal
#FauzanBurhanuddin/V3922020
nama = input ("Masukkan Nama Lengkap Anda : ") #Untuk Memasukkan nama dan menyimpan dalam variabel nama

huruf = len(nama.replace(" ", "")) #menghitung jumlah huruf dalam nama lengkap pengguna. 
                                   #Fungsi replace() digunakan untuk menghapus spasi dalam nama lengkap, sehingga hanya huruf yang dihitung.

vokal = "aiueoAIUEO" # String yang berisikan semua huruf vokal
jumlah_vokal = len([char for char in nama if char in vokal]) # menghitung jumlah huruf vokal dalam nama lengkap pengguna. 
                                                             #List comprehension digunakan untuk memeriksa setiap karakter dalam nama lengkap dan menghitung karakter yang termasuk dalam string vokal

jumlah_konsonan = huruf - jumlah_vokal # menghitung jumlah huruf konsonan dalam nama lengkap dengan mengurangi jumlah huruf vokal dari jumlah huruf total.

print("Jumlah huruf dari nama lengkap Anda adalah :", huruf)
print("Jumlah huruf vokal dari nama lengkap Anda adalah :", jumlah_vokal)
print("Jumlah huruf konsonan dari nama lengkap Anda adalah :", jumlah_konsonan)
