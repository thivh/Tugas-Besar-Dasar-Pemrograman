def tambahwahana(datauser,wahana): # data yang dibutuhkan adalah data pengguna program dann data file wahana
    if (datauser[5] == 'Admin'): # jika pengguna program adalah admin
        print('Masukkan Informasi Wahana yang ditambahkan:')
        a = input('Masukkan ID Wahana: ')
        b = input('Masukkan Nama Wahana: ') 
        c = input('Masukkan Harga Tiket: ')
        d = input('Batasan umur: ')
        e = input('Batasan tinggi badan: ')
        wahanabaru = [a,b,c,d,e] # data yang diinput dibuat menjadi array
        
        # kondisi awal untuk pengulangan
        i = 0
        
        # pengulangan dilakukan untuk mencari posisi kosong pada array agar bisa dtambahkan data baru
        while (wahana[i] != ''): # kondisi akan mengulang asalkan data ke-i pada array wahana tidak kosong
            i = i + 1
        wahana[i] = wahanabaru # ditambahkan data yang baru pada posisi yang kosong pada array
        print('Info wahana telah ditambahkan!')
    return wahana # hasil yang dikembalikan adalah data file wahana yang baru

