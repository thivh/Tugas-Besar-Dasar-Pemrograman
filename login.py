def login(user): # data yang dibutuhkan adalah data file user
    username = str(input('Masukkan username: '))
    password = str(input('Masukkan password: '))
    
    import enkripsi
    
    # kondisi awal
    ketemu = False
    i = 0
    
    while (user[i] != '') and (ketemu == False): # pengulangan dilakukan asalkan data file user ke-i tidak kosong dan username belum ditemukan
        user1 = user[i]
        if(user1[3] == username) and (user1[4] == enkripsi.enkripsi(password)): 
        # jika username dan password pada data ke-i dari array file user sama dengan yang dicari
            ketemu = True # username ditemukan
        else: # jika username dan password pada data ke-i dari array file user berbeda dengan yang dicari
            i = i + 1
    if (ketemu == True): # jika username ditemukan
        print(str('Selamat bersenang-senang, ') + user1[0] + '!',sep = '')
        return user1 # hasil yang dikembalikan adalah data pengguna
    else: # jika username tidak ditemukan atau password salah
        print('Ups, password salah atau kamu tidak terdaftar dalam sistem kami. Silakan coba lagi!')
        return [] # data pengguna menjadi nilai default kosong []


            

