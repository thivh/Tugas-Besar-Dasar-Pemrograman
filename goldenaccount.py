def upgrade(datauser,user): # data yang dibutuhkan adalah data file user dan data pengguna program
    if (datauser[5] == 'Admin'): # jika pengguna adalah admin
        a = input('Masukkan username yang ingin di-upgrade: ') # variabel a sebagai nama username yang ingin diupgrade
        
        # kondisi awal
        i = 0
        ketemu = False 
        valid = False
        
        while (user[i] != '') and (ketemu == False): 
        # kondisi akan mengulang jika data pada user ke-i pada array tidak kosong dan belum ditemukan username yang dicari
            b = user[i] 
            if (b[3] == a): # jika username pada data user ke-i adalah username yang dicari
                ketemu = True # username ditemukan
                if (int(b[6]) >= 50000) and (b[7] != 'Ya'): # jika saldo pemain mencukupi untuk upgrade dan akun belum diupgrade
                    b[6] = int(b[6]) - 50000  # saldo dikurangi biaya upgrade yaitu 50000
                    b[7] = 'Ya'  # akun berhasil diupgrade
            else: # jika username pada data user ke-i bukan username yang dicari
                i = i + 1 # mengecek data selanjutnya
        if (b[7] == 'Ya'): # jika akun berhasil diupgrade atau jika akun sudah diupgrade sebelumnya
            user[i] = b  # untuk menyimpan perubahan yang dilakukan
            print('Akun Anda telah diupgrade.')
    return user # nilai yang dikembalikan adalah data user yang terbaru

