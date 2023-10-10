import os
from prettytable import PrettyTable
iphone = PrettyTable()
def tampilkan_iphone(iphone):
    print(iphone)

def show_menu():
    print("\nMenu Admin:")
    print("1. Barang yang ada di toko")
    print("2. Menambahkan barang")
    print("3. Update Barang")
    print("4. Hapus Barang")
    print("5. Keluar")

#=== MENU ADMIN ===
def admin():
    while True:
        iphone.field_names = ["No","Merk_Iphone","Harga"]
        iphone.add_rows([        
        ["1","Iphone 15 Pro Max","30000000",],
        ["2","Iphone 14 Pro Max","25000000",],
        ["3","Iphone 13 Pro Max","20000000",],
        ["4","Iphone 12 Pro Max","15000000",],
        ["5","Iphone 11 Pro Max","10000000",],
        ])
        while True:
            show_menu()
            pilihan = int(input("Pilihlah menu (1/2/3/4/5): "))

            #Program Read
            if pilihan == 1:
                print('Inilah beberapa barang yang ready di dalam toko..')
                print(iphone)

            #Program Create
            elif pilihan == 2:
                noIphone = input('Masukkan No Iphone baru: ')
                iphoneBaru = input('Masukkan Iphone baru : ')
                hargaBaru = input('Masukkan Harga baru: ')
                iphone.add_row([noIphone,iphoneBaru,hargaBaru])
                print(iphone)

            #Program Update
            elif pilihan == 3:
                update = input('Masukkan No Iphone yang akan di update: ')
                for Ip in iphone._rows:
                    if Ip["No"] == update:
                        noIphone = input('Masukkan nomor Iphone Updatean: ')
                        iphoneUpdate = input('Masukkan Iphone yang ingin di update: ')
                        hargaBaru = input('Masukkan Updatean harga baru: ')
                        Ip[1] = noIphone
                        Ip[2] = iphoneUpdate
                        Ip[3] = hargaBaru
                        print(iphone)
                        print('Selamat anda berhasil mengUpdate list Iphone yang baru!')
                        return True
                    else:
                        print('Kesalahan input mohon coba ulang')

            # Program Delete
            elif pilihan == 4:
                hapus_iphone = input("Masukkan nomor Iphone yang ingin dihapus: ")
                found = False
                for i, row in enumerate(iphone._rows):
                    if row[0] == hapus_iphone:
                        found = True
                        del iphone._rows[i]
                        print(f"Barang dengan nomor Iphone {hapus_iphone} berhasil dihapus.")
                        print(iphone)
                        break

                if not found:
                    print(f"Barang dengan nomor Iphone {hapus_iphone} tidak ditemukan.")

            elif pilihan == 5:
                print("Terimakasih telah menggunakan program ini!.")
                return True

            else:
                print("Pilihan tidak valid. Silakan coba lagi.")

#=== LOGIN ADMIN ===
def loginAdmin():
    usernameAdmin = '1'
    passwordAdmin = '1'
    
    while True:
        print('Selamat datang di RufPhone')
        print('--Silahkan Login--')
        username = input('Masukkan Nama anda: ')
        password = input('Masukkan Password anda: ')
        
        if username == usernameAdmin and password == passwordAdmin:
            print('Selamat anda berhasil login!')
            admin()
            return True
        else:
            print('Username atau Password anda salah, coba lagi..')

#=== Program CheckOut User ===
def sistemPembelian():
    iphone = PrettyTable()
    iphone.field_names = ["No", "Merk_Iphone", "Harga"]
    iphone.add_rows([        
        ["1", "Iphone 15 Pro Max", "30000000"],
        ["2", "Iphone 14 Pro Max", "25000000"],
        ["3", "Iphone 13 Pro Max", "20000000"],
        ["4", "Iphone 12 Pro Max", "15000000"],
        ["5", "Iphone 11 Pro Max", "10000000"],
    ])

    noIphone = input('Masukkan nomor Iphone yang ingin anda beli: ')
    merkIphone = ''
    
    # Menangani input untuk jumlah total iPhone
    total_input = input('Berapa Iphone yang ingin anda beli: ')
    while not total_input.isdigit():
        print("Input harus berupa angka. Silakan coba lagi.")
        total_input = input('Berapa Iphone yang ingin anda beli: ')

    total = int(total_input)

    # Mencari iPhone yang dipilih
    ditemukan = False
    for baris in iphone._rows:
        if baris[0] == noIphone:
            ditemukan = True
            merkIphone = baris[1]
            hargaSatuan = int(baris[2])
            jumlahHarga = hargaSatuan * total
            print(f'Terimakasih sudah membeli {merkIphone} sebanyak {total} dengan harga {jumlahHarga}')
            print('Pembayaran di transfer ke rekening ini (914819591)')
            break

    if not ditemukan:
        print(f"Barang dengan nomor Iphone {noIphone} tidak ditemukan.")



#=== MENU USER ===
def loginPembeli():
    while True:
        from prettytable import PrettyTable
        iphone.field_names = ["No","Merk_Iphone","Harga"]
        iphone.add_rows([        
        ["1","Iphone 15 Pro Max","30000000",],
        ["2","Iphone 14 Pro Max","25000000",],
        ["3","Iphone 13 Pro Max","20000000",],
        ["4","Iphone 12 Pro Max","15000000",],
        ["5","Iphone 11 Pro Max","10000000",],
        ])
        print(iphone)
        sistemPembelian()
        return True

if __name__ == "__main__":
    masuk = PrettyTable()
    masuk.field_names = ["Hi! Welcome to RufPhone"]
    masuk.add_row(['1.Admin'])
    masuk.add_row(['2.Konsumen'])
    print(masuk)

    masukKan = int(input('Pilihlah terlebih dahulu: '))

    if masukKan == 1:
        loginAdmin()
    elif masukKan == 2:
        loginPembeli()
    else:
        print('Pilihan tidak valid')
