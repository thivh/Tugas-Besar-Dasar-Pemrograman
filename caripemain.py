def caripemain(datauser,user):
#Mencari data pemain
#kamus
    if datauser[5] == 'Admin':  #validasi role admin
        a = str(input('Masukkan username: ')) #Nama pemain yang dicari

        #kondisi awal untuk pengulangan
        i = 0 
        ketemu = False
        
        while (user[i] != '') and (ketemu == False):
            user1 = user[i]
            if (user1[3] == a):
                ketemu = True #Nama pemain ditemukan
            else: #belom ditemukan
                i = i + 1
                
        if ketemu == False:
            print('Pemain tidak ditemukan')
        else: #user[i][3] == a
            print('Nama Pemain: ',user[i][0])
            print('Tinggi Pemain: ',user[i][2],' cm')
            print('Tanggal Lahir Pemain: ',user[i][1])
    else :
        print()
        print('Hanya admin yang dapat melakukan aksi ini!')
    return
