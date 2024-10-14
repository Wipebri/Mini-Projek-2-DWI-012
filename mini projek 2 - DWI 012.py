from prettytable import PrettyTable

tabel = PrettyTable()
tabel.field_names = ["No", "Hari", "Room Type","Harga", "pemesan"]

def listharga(no,hari, room_type, harga, nama):
    tabel.add_row([no, hari, room_type, harga, nama])

#database list
listharga("1", "Senin", "Small", "35.000", " ")
listharga("2", "Senin", "Medium", "45.000", " ")
listharga("3", "Selasa", "promo Small", "20.000", " ")
listharga("4", "Selasa", "Promo Medium", "30.000", " ")

#sambutan awal saat memulai program
def sambutan():
    print("\n*Selamat Datang di Happy Singing*")

#menu pilihan login
def login():
    while True:
        print("\nAnda masuk sebagai:")
        print("1. Admin")
        print("2. Customer")
        pilihan = input("Silakan Pilih = ")
        if pilihan == "1":
            admin()
        elif pilihan == "2":
            customer()
            break
        else:
            print("Pilihan tidak tersedia, silakan coba kembali!")
            return login()

#menu PIN untuk memastikan user adalah admin
def menupin():
    print("\nJika anda adalah admin, masukan PIN dengan benar!")
    for cobapin in range(3) :
        pin = input("Masukkan PIN = ")
        if pin == "131024" :
            print("PIN Sesuai, Login Berhasil!")
            break
        else :
            print(f"PIN salah. terisa {3-cobapin-1} kesempatan")
    if cobapin == 3-1 :
        print("\n*Login sebagai admin gagal*")
        keluarkembali()

#menu pilihan mode admin
def pilihanmenu():
    print("\nPilihan dibawah adalah hal yang dapat anda lakukan:")
    print("1. Lihat List")
    print("2. Tambah List")
    print("3. Hapus List")
    print("4. Perbarui List")
    print("5. Keluar atau Kembali ke Pilih Mode Login")
    menu = input("Input menu = ")
    if menu == "1":
        lihatlist()
    elif menu == "2":
        tambahlist()
    elif menu == "3":
        hapuslist()
    elif menu == "4":
        perbaruilist()
    elif menu == "5":
        print("\n ")
        keluarkembali()
    else:
        print("Menu tidak tersedia, silahkan input menu yang tersedia")
        return pilihanmenu()

#sistem pilihan keluar atau kembali ke menu pilihan login
def keluarkembali() :
    mode_login = input ("Keluar atau kembali ke mode login? (Keluar/Kembali) = ")
    if mode_login == "Keluar" or mode_login == "keluar" or mode_login == "KELUAR":
            print("\n*Terima kasih*")
            exit()
    elif mode_login == "Kembali" or mode_login == "kembali" or mode_login == "KEMBALI":
            login()
    else :
        print("Input tidak tersedia")
        keluarkembali()

#sistem pilihan keluar atau kembali ke pilihan menu admin
def keluarlist() :
    mode_login = input ("Ke menu login atau Kembali ke mode pilihan? (Login/Pilihan) = ")
    if mode_login == "Login" or mode_login == "login" or mode_login == "LOGIN":
            login()
    elif mode_login == "Pilihan" or mode_login == "pilihan" or mode_login == "PILIHAN":
            pilihanmenu()
    else :
        print("Input tidak tersedia")
        keluarlist()

#Mode Admin
def admin():
    print("\n*Selamat Datang di Mode Admin*")
    nama = input("Masukkan Nama = ")
    menupin()
    while True: 
        print(f"\n*Selamat Datang Admin {nama}!*")
        pilihanmenu()

#Fitur admin melihat list
def lihatlist():
    print("\nDibawah ini list yang sudah tersedia:")
    print(tabel)
    keluarlist()

#Fitur admin menambah list
def tambahlist():
    while True:
        print("\nDibawah ini list yang sudah tersedia:")
        print(tabel)
        print("Masukkan data list yang ingin ditambah :")
        no = input("Masukan Nomor List = ")
        hari = input("Masukan Hari = ")
        room_type = input("Masukan Room Type = ")
        harga = input("Masukan Harga = ")
        nama = input("Masukan Nama Pemesan = ")
        listharga(no ,hari, room_type, harga, nama)
        print("\n")
        print(tabel)
        print(f" List di hari {hari} dengan room type {room_type} Berhasil Ditambahkan seharga Rp.{harga}")
        pilihan = input("Apakah ingin menambahkan lagi? (y/n)= ")
        if pilihan == "n" or pilihan == "N":
            pilihanmenu()
        elif pilihan == "y" or pilihan == "Y":
            tambahlist()
        else :
            pilihanmenu()


#Fitur admin menghapus list
def hapuslist():
    while True:
        print("\nDibawah ini list yang sudah tersedia:")
        print(tabel)
        no = input("Masukan nomor list yang ingin dihapus = ")
        for row in tabel._rows:
            if row[0] == no:
                tabel.del_row(tabel.rows.index(row))
        print("\n")
        print(tabel)
        print(f"List telah dihapus")
        pilihan = input("Apakah ingin menghapus lagi? (y/n) = ")
        if pilihan == "n" or pilihan == "N":
            pilihanmenu()
        elif pilihan == "y" or pilihan == "Y":
            hapuslist()
        else :
            pilihanmenu()


#Fitur admin memperbarui list
def perbaruilist():
    while True :
        print("\nDibawah ini list yang sudah tersedia:")
        print(tabel)
        no = input("Masukan nomor list awal = ")
        ubah_list = input("Pilih yang akan dubah (Hari/Type/Harga/Nama) = ")
        nilai_baru = input(f"Masukan {ubah_list} baru = ")
        for row in tabel._rows:
            if row[0] == no:
                index = tabel._rows.index(row)
                if ubah_list == "Hari" or ubah_list == "hari" :
                    tabel._rows[index][1] = (nilai_baru)
                elif ubah_list == "Type" or ubah_list == "type":
                    tabel.rows[index][2] = (nilai_baru)
                elif ubah_list == "Harga" or ubah_list == "harga":
                    tabel.rows[index][3] = (nilai_baru)
                elif ubah_list == "Nama" or ubah_list == "nama":
                    tabel.rows[index][4] = (nilai_baru)
                else:
                    print ("\nPilihan Tidak Tersedia")
                    return perbaruilist()
        print("\n")
        print(tabel)
        print(f"list Nomor {no} berhasil diubah.")
        pilihan = input("Apakah ingin mengubah lagi? (y/n) = ")
        if pilihan == "n" or pilihan == "N":
            pilihanmenu()
        elif pilihan == "y":
            perbaruilist()
        else :
            pilihanmenu()


#Mode Customer
def customer():
    print("\n*Halo Customer Tercinta!*")
    nama_customer = input("Masukkan nama Anda = ")
    print(f"\n*Halo {nama_customer}, Selamat Datang di Happy Singing*")
    while True:
        print("Brikut adalah list yang kami sediakan :")
        print(tabel)
        while True:
            no = input("Masukan nomor yang ingin dipesan = ")
            found = False
            for row in tabel._rows:
                if row[0] == no:
                    found = True
                    index = tabel._rows.index(row)
                    print("\nKeterangan :")
                    tabel.rows[index][4] = (nama_customer)
                    print(tabel)
                    print(f"Anda telah memesan list hari {row[1]} dengan Room Type {row[2]}")
                    print("*Terima Kasih*")
                    exit()
            if not found:
                print("Nomor tidak tersedia di list. Silakan coba lagi.")

#memulai program
sambutan()
login()