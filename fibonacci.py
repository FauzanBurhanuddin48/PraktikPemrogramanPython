#FauzanBurhanuddin/V3922020
panjang = int(input('Masukkan Panjang Deret : ')) #digunakkan untuk mengisi inputan berupa bilangan bulat untuk menentukan panjang dari deret bilangan
fibo = [0, 1] #inisialisasi list 'fibo' dengan  elemen awal 0 dan 1, dimana elemen 0 dan 1 merupakan bilangan awal dari deret bilangan Fibonacci. elemen awal 0 dan 1, dimana elemen 0 dan 1 merupakan bilangan awal dari deret bilangan Fibonacci.
print(fibo)

for i in range (2, panjang): #perulangan for yang dimulai dari indeks ke-2 hingga 'panjang -1'. Karena elemen pertama (0) dan kedua (1) telah dimasukkan pada saat inisialisasi.
    angka1 = fibo[i-2]
    angka2 = fibo[i-1] #digunakan untuk menyimpan elemen sebelumnya yang dibutuhkan untuk menghasilkan nilai 'nextangka'
    nextangka = angka1 + angka2 #operasi penjumlahan yang menghasilkan nilai berikutnya pada deret bilangan Fibonacci.

    fibo.append(nextangka) #menambahkan nilai 'nextangka' pada akhir list fibo.

    print(fibo, end="") #mencetak isi dari list fibo pada setiap perulngan.
    print() #mencetak baris baru pada setiap perulangan.
