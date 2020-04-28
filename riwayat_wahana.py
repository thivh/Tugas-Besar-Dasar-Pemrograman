def riwayatwahana(datauser, penggunaan):
    # Hanya admin yang bisa melihat riwayat penggunaan wahana.
    if (datauser[5] == "Admin"):
        IDWahana = input("Masukkan ID Wahana: ") # Dapat diasumsikan ID Wahana valid.
        print("Riwayat:")
        # Mencari ID Wahana di array penggunaan
        i = 0
        found = False
        while (penggunaan[i] != "") and (found == False):
            if (penggunaan[i][2] == IDWahana):
                found = True
            else:
                i = i + 1
        if (found == True): # ID Wahana ditemukan
            print(penggunaan[i][1], " | ", penggunaan[i][0], " | ", penggunaan[i][3]) # Format: Tanggal_Bermain | Username Pengguna| Jumlah Tiket
    return
