def topup(datauser,user):
#Melakukan top up pada akun pemain dilakukan oleh admin saja
    if datauser[5] == 'Admin':
        user_dicari = str(input('Masukkan username: '))
        topup = int(input('Masukkan saldo yang di-top up: '))

        #kodisi awal untuk pengulangan
        i = 0
        ketemu = False

        while (user[i] != '') and (ketemu == False):
            user1 = user[i]

            if (user1[3] == user_dicari):
                ketemu = True
            else: #belom ditemukan
                i = i + 1

        if (ketemu == True):
            saldo_baru = str(int(user[i][6]) + topup)
            user[i][6] = saldo_baru
            print('Top up berhasil. Saldo',user[i][0],'bertambah menjadi',user[i][6])
        else: #ketemu = False
            print('username tidak ditemukan')

    else:
        print('Hanya admin yang dapat melakukan aksi ini!')

    return (user,datauser)
