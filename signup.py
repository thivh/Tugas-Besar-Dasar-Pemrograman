# F04 - Signup User
# Pendaftaran pemain hanya dapat dilakukan oleh admin dan tidak diizinkan
# memasukkan username yang sudah terdaftar.

#agar password dapat terenkripsi
import enkripsi

def signup(datauser,user):
    #pendaftaran hanya dilakukan oleh admin
    if (datauser[5] == "Admin"):
        # signup pemain
        Nama = input('Masukkan nama pemain: ')
        Tanggal_Lahir = input('Masukkan tanggal lahir pemain (DD/MM/YYYY): ')
        Tinggi_Badan = input('Masukkan tinggi badan pemain (cm): ')
        # username yang diinput tidak boleh sama dengan yang sudah terdaftar
        Username = input('Masukkan username pemain: ')
        i = 0
        while (user[i] != ''):
            #mengecek username yang diinput dengan yang sudah terdaftar
            cek = user [i]
            if (Username == cek[3]): #jika username telah digunakan
                print('Username sudah dipakai, silahkan pilih yang lain!')
                i = 0
                Username = input('Masukkan username pemain: ')
            else:
                i = i + 1
        #jika username yang diinput telah valid
        Password = input('Masukkan password pemain: ')
        #password terenkripsi
        enkrip = enkripsi.enkripsi(Password)
        #array untuk pengguna baru
        user[i] = [Nama,Tanggal_Lahir,Tinggi_Badan,Username,enkrip,'Pemain',0,'']
        print('Selamat menjadi pemain,',Nama,'. Selamat bermain.')

        return user
