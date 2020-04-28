def TulisPembelian(datauser, pembelian, TanggalPembelian, JumlahTiket, IDWahana): # Menulis data ke array pembelian
    i = 0
    found = False
    while (pembelian[i] != '') and (found == False): # Data belum ditemukan.
        if (pembelian[i][0] == datauser[3]) and (pembelian[i][1] == TanggalPembelian) and (pembelian[i][2] == IDWahana):
            found = True
        else:
            i = i + 1
    if (found == True): # Data ditemukan.
        pembelian[i][3] =  str(int(pembelian[i][3]) + JumlahTiket) # Penambahan jumlah tiket di indeks yang sudah ada.
    else: # Data tidak ditemukan.
        pembelian[i] = [datauser[3], TanggalPembelian, IDWahana, str(JumlahTiket)] # Penulisan data baru.
    return pembelian

def TulisKepemilikan(datauser, kepemilikan, IDWahana, JumlahTiket): # Menulis data ke array kepemilikan
    i = 0
    found = False
    while (kepemilikan[i] != "") and (found == False): # Data belum ditemukan.
        if (kepemilikan[i][0] == datauser[3]) and (kepemilikan[i][1] == IDWahana):
            found = True
        else:
            i = i + 1
    if (found == True): # Data ditemukan.
        kepemilikan[i][2] =  str(int(kepemilikan[i][2]) + JumlahTiket) # Penambahan jumlah tiket di indeks yang sudah ada.
    else: # Data tidak ditemukan.
        kepemilikan[i] = [datauser[3], IDWahana, str(JumlahTiket)] # Penulisan data baru.
    return kepemilikan

def TulisUser(datauser, user, JumlahTiket): # Menulis data ke array kepemilikan
    i = 0
    found = False
    while (user[i] != "") and (found == False): # Data belum ditemukan.
        if (user[i][3] == datauser[3]):
            found = True
        else:
            i = i + 1
    if (found == True): # Data ditemukan.
        user[i][6] =  str(int(user[i][6]) - JumlahTiket) # Pengurangan saldo di indeks yang sudah ada.
    else: # Data tidak ditemukan.
        user[i] = datauser # Penulisan data baru.
    return user

def belitiket(datauser, user, wahana, kepemilikan, pembelian):
    # Pembelian tiket hanya dapat dilakukan oleh pemain yang telah terdaftar dan melakukan login.
    if (datauser[5] == "Pemain"):
        IDWahana = str(input("Masukkan ID wahana: "))
        TanggalPembelian = str(input("Masukkan tanggal hari ini: "))
        JumlahTiket = int(input("Jumlah tiket yang dibeli: "))

        WaktuPembelian = TanggalPembelian.split("/") # [dd, mm, yyyy]
        WaktuLahir = datauser[1].split("/") # [dd, mm, yyyy]

        if ((int(WaktuPembelian[2]) - int(WaktuLahir[2])) < 17): # Jika 0 < tahun pembelian - tahun lahir < 17
            BatasanUmur = "anak-anak"
        else: # Jika tahun pembelian - tahun lahir >= 17
            BatasanUmur = "dewasa"

        # Pencarian ID Wahana di array wahana
        i = 0
        found = False # Wahana belum ditemukan.
        while (wahana[i] != "") and (found == False):
            if (wahana[i][0] == IDWahana):
                found = True
            else:
                i = i + 1

        # Validasi tinggi
        if (wahana[i][4] == "tanpa batasan"):
            tinggi = True
        elif (wahana[i][4] == ">=170 cm"):
            if (int(datauser[2]) >= 170):
                tinggi = True
            else:
                tinggi = False

        if (found == True): # Wahana ditemukan.
            #Pemain cukup umur dan cukup tinggi untuk memasuki wahana tersebut.
            if ((wahana[i][3] == "semua") or (wahana[i][3] == BatasanUmur)) and (tinggi == True):
                if (datauser[7] == "Ya"): # Pemain  gold
                    if (int(datauser[6]) >= (JumlahTiket * (int(wahana[i][2]))//2)): # Pemain memiliki saldo yang cukup untuk membeli tiket.
                        datauser[6] = int(datauser[6]) - JumlahTiket * (int(wahana[i][2]))//2 # Pengurangan saldo
                        pembelian = TulisPembelian(datauser, pembelian, TanggalPembelian, JumlahTiket, IDWahana) # Penulisan data ke array pembelian
                        kepemilikan = TulisKepemilikan(datauser, kepemilikan, IDWahana, JumlahTiket) # Penulisan data ke array kepemilikan
                        user = TulisUser(datauser, user, JumlahTiket) # Penulisan data ke array user
                        print("Selamat bersenang-senang di ", wahana[i][1])
                    else: # Pemain tidak memiliki saldo yang cukup untuk membeli tiket.
                        print("Saldo Anda tidak cukup")
                        print("Silakan mengisi saldo Anda")
                else: # Pemain  biasa
                    if (int(datauser[6]) >= (JumlahTiket * int(wahana[i][2]))): # Pemain memiliki saldo yang cukup untuk membeli tiket.
                        datauser[6] = str(int(datauser[6]) - JumlahTiket * int(wahana[i][2])) # Pengurangan saldo
                        pembelian = TulisPembelian(datauser, pembelian, TanggalPembelian, JumlahTiket, IDWahana) # Penulisan data ke array pembelian
                        kepemilikan = TulisKepemilikan(datauser, kepemilikan, IDWahana, JumlahTiket) # Penulisan data ke array kepemilikan
                        user = TulisUser(datauser, user, JumlahTiket) # Penulisan data ke array user
                        print("Selamat bersenang-senang di ", wahana[i][1])
                    else: # Pemain tidak memiliki saldo yang cukup untuk membeli tiket.
                        print("Saldo Anda tidak cukup")
                        print("Silakan mengisi saldo Anda")
            else: # Pemain tidak cukup umur atau tidak cukup tinggi untuk memasuki wahana tersebut.
                print("Anda tidak memenuhi persyaratan untuk memainkan wahana ini.")
                print("Silakan menggunakan wahana lain yang tersedia.")
    return (user, datauser, pembelian, kepemilikan)
