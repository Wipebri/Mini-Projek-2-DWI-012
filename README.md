# Mini-Projek-2-DWI-012
DWI PEBRIYANTO PRADANA | 2409116012 | SISTEM INFORMASI A 2024

Tema : Program Penyewaan Tempat Karaoke

# Flowchart
![mini projek 2 drawio (3)](https://github.com/user-attachments/assets/16fc4e57-4de5-46cd-9a1a-0e97b59f1d17)

# Penjelasan Output
## Menu Login
![Cuplikan layar 2024-10-14 130045](https://github.com/user-attachments/assets/cdb40433-5164-4535-b44e-07cb373e0d41)

saat memulai program user akan di ucapkan selamat datang, dan diberi pilihan untuk memilih role.
- Admin, dengan role ini user dapat melakukan Create, Read, Update, dan Delete (CRUD), pada database.
- Customer, dengan role ini user hanya dapat melakukan transaksi yaitu penyewaan.

![Cuplikan layar 2024-10-14 130115](https://github.com/user-attachments/assets/fc702bdc-1914-47a5-a5fe-9b59399c7983)

jika user memilih selain angka 1 dan 2, akan muncul tulisan "pilihan tidak tersedia", kemudian memerintahkan user untuk memilih pilhan yang tersedia.

## Menu Admin
![Cuplikan layar 2024-10-14 130137](https://github.com/user-attachments/assets/2e179774-59ce-433d-9b7c-b91d5ec4b7d2)


dengan memilih pilihan nomor 1, user akan memasuki mode admin. user diminta memasukan nama, kemudian memasukan PIN dengan benar.

### Memasukan PIN
![Cuplikan layar 2024-10-14 131023](https://github.com/user-attachments/assets/6eb53775-0746-4804-8484-f4da91559615)

user hanya diberi 3 kesempatan memasukan PIN hingga benar, jika user sudah 3 kali salah memasukan PIN, mmaka login gagal, dan user diiberi pilihan apakah ingin kembali kemenu login atau keluar dari program.

![Cuplikan layar 2024-10-14 131045](https://github.com/user-attachments/assets/adeff1fc-2402-457c-854e-8e3655051e76)

jika user mengetik "Kembali" maka user kembali ke menu pilih role.

![Cuplikan layar 2024-10-14 132533](https://github.com/user-attachments/assets/623a5431-ee7a-4407-9716-81763ec6587e)

jika user mengetik "Keluar" maka program selesai.

![Cuplikan layar 2024-10-14 131336](https://github.com/user-attachments/assets/2f5adb57-53e7-4357-b973-e4f62ad92865)

ketika user berhasil memasukan PIN dengan benar, user akan lanjut ke pilihan menu fitur yang dimiliki admin.

### Memilih pilihan 1
![Cuplikan layar 2024-10-14 131354](https://github.com/user-attachments/assets/ec462a37-a364-4a8f-a600-ac76038d80c4)

pilihan 1 akan menampilkan list harga yang tersedia di database, setelah itu program menawarkan apakah ingin kembali ke menu pilihan atau ke menu login memilih role.

![Cuplikan layar 2024-10-14 133236](https://github.com/user-attachments/assets/328ca0ec-4a55-4751-9468-3dc37bf4d6d5)

jika user mengetik "pilihan" sistem otomatis menampilkan kembali menu pilihan untuk fitur admin

![Cuplikan layar 2024-10-14 133251](https://github.com/user-attachments/assets/e6c46479-1c0d-46f8-83df-3c78630ba26e)

jika user mengetik "Login" maka sistem otomatis mengembalikan user ke menu pilihan role.

![Cuplikan layar 2024-10-14 133643](https://github.com/user-attachments/assets/a45b1647-a3d0-4e35-836f-a30c3c913392)

jika user asal-asalan mengetik maka akan muncul tulisan input tidak tersedia, dan muncul perintah untuk mengetik sesuai opsi yang diberikan.

### Memilih Pilihan 2
![Cuplikan layar 2024-10-14 133838](https://github.com/user-attachments/assets/d9ca29e9-7dcc-4da9-8619-3b8dca6bee65)

jika user memilih pilihan 2, sistem otomatis menampilkan tabel list terakhir, kemudian memerintahkan user mengisi data list terbaru yang dimasukan (Nomor, hari, room type, harga, dan nama pemesan jika sudah booking duluan)

![Cuplikan layar 2024-10-14 133904](https://github.com/user-attachments/assets/859ebeeb-2180-479f-9e90-354dbd0b6f86)

setelah user selesai mengisi data list terbaru, sistem otomatis menampilkan tabel list terbaru, kemudian menawarkan ingin menambah lagi atau kembali ke menu pilihan.
jika user mengetik "y" maka user bisa menambahkan list lagi, jika mengetik "n" maka user akan kembali ke menu list fitur admin.

### Memilih Pilihan 3
![Cuplikan layar 2024-10-14 134409](https://github.com/user-attachments/assets/bc9d3be5-ddad-495d-9213-de1d5af42ca5)

jika user memilih pilihan 3, sistem otomatis menampilkan tabel list terakhir, kemudian memerintahkan user memasukan nomor list yang ingin dihapus.

![Cuplikan layar 2024-10-14 134417](https://github.com/user-attachments/assets/ef14ba61-4db7-4bc1-bc05-16f92657bd61)

setelah mengetik nomor list yang ingin dihapus, sistem akan menampilkan tabel terbarunya, kemudia menawarkan apakah ingin menghapus lagi atau tidak.

### Pilihan 4
![Cuplikan layar 2024-10-14 135455](https://github.com/user-attachments/assets/05e87a56-826f-4050-96c7-e99d6a3e6aff)

jika user memilih pilihan 4, sistem otomatis menampilkan tabel list terakhir, kemudian memerintahkan user memasukan nomor list yang ingin diubah.

![Cuplikan layar 2024-10-14 135517](https://github.com/user-attachments/assets/83f1cdf7-ef16-4f8a-9aaf-64968b9c6433)
kemudian sistem menanyakan bagian mana yang ingin diubah oleh user.

![Cuplikan layar 2024-10-14 135542](https://github.com/user-attachments/assets/fc0c7ec5-26f8-47dc-9c32-e4a3ca9a51b2)
setelah user mengubah bagian yang ingin diubahnya sistem akan menampilkan tabel terbaru, kemudian menawarkan ingin mengubah lagi atau tidak.

### Memilih Pilihan 5
![Cuplikan layar 2024-10-14 140038](https://github.com/user-attachments/assets/d8562885-1e65-4b20-a06c-a207a9c572f3)

jika user memilih pilihan nomor 5, sistem akan menanyakan apakah user ingin keluar atau kembali ke menu login.
jika user mengetik "kembali" maka user akan kembali ke menu pemilihan role.
jika user mengetik "keluar" maka program akan selesai.

![Cuplikan layar 2024-10-14 140059](https://github.com/user-attachments/assets/c97cc19d-2b99-4b95-8ed3-0035602fe1ce)

kalau user asal mengetik maka akan muncul tulisan input tidak tersedia.

## Menu Customer
