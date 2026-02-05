# Tugas-Proyek-KKA_Avis-Zola-R.K-XI-RPL-7-

ANALISIS 1
- Mengubah hero1.hp = 500 secara langsung diperbolehkan di Python karena secara default atribut bersifat publik.
-  dengan output Nilai HP Layla berubah dari 100 menjadi 500. Ini membuktikan bahwa state sebuah objek dapat dimanipulasi setelah instansiasi.

ANALISIS 2
- Mengirim objek utuh (lawan) memungkinkan method serang mengakses semua kapabilitas lawan (atribut dan methodnya).
- dengan output Interaksi dua arah terjadi; saat Layla menyerang Zilong, HP Zilong berkurang secara otomatis melalui method diserang miliknya sendiri

ABALISIS 3
- Jika super().__init__ dihapus, muncul AttributeError dengan penyebab Class Mage tidak menjalankan logika inisialisasi Hero, sehingga atribut name dan hp tidak pernah dibuat di memori untuk objek Mage tersebut.
- Fungsi super() Sebagai jembatan untuk memastikan semua atribut dasar dari class induk tetap terpasang pada class anak.

ANALISIS 4
- Akses paksa _Hero__hp tetap berhasil karena Python hanya mengubah nama variabel secara internal untuk menghindari konflik, bukan benar-benar menguncinya secara absolut. Namun, ini dianggap praktik buruk.
- Tanpa validasi di set_hp, HP bisa bernilai negatif (-100). Keberadaan Setter menjaga integritas data agar objek selalu berada dalam kondisi logis (misal: HP minimal 0).

ANALISIS 5 
- Jika Hero tidak mengimplementasikan serang(), akan muncul error saat pembuatan objek. Ini memastikan setiap unit di game memiliki fungsi dasar yang sama.
- GameUnit() dilarang dibuat menjadi objek karena ia hanyalah "ide" atau "cetakan dasar", bukan entitas nyata yang siap digunakan.

ANALISIS 6
- Menambahkan class Healer sangat mudah. Kita tidak perlu mengubah kode looping utama, cukup tambahkan class baru dan masukkan ke dalam list pasukan.
- Jika nama method diubah (misal: tembak_panah), polimorfisme gagal karena mesin pencari method hanya mencari nama yang seragam (kontrak) yang didefinisikan di induk.
