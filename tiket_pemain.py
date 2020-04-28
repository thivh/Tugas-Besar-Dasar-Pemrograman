def tiketpemain(datauser, wahana, kepemilikan):
    # Hanya admin yang bisa melihat jumlah tiket yang dimiliki pemain.
    if (datauser[5] == "Admin"):
        username = str(input("Masukkan username: ")) # Dapat diasumsikan username valid.
        print("Riwayat:")
        # Mencari username di array kepemilikan
        i = 0
        found = False
        while (kepemilikan[i] != "") and (found == False):
            if (kepemilikan[i][0] == username):
                found = True
            else:
                i = i + 1
        if (found == True): # username ditemukan
            # Mencari ID Wahana di array wahana
            j = 0
            found1 = False
            while (wahana[j] != "") and (found1 == False):
                if (wahana[j][0] == kepemilikan[i][1]):
                    found1 = True
                else:
                    j = j + 1
            if (found1 == True): # ID Wahana ditemukan
                print(kepemilikan[i][1], " | ", wahana[j][1], " | ", kepemilikan[i][2]) # Format: ID_Wahana | Nama_Wahana | Jumlah Tiket
    return
