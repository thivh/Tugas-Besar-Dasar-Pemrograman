# F06 - pencarian wahana
# Data wahana dapat dicari berdasarkan beberapa faktor
# Faktor-faktor tersebut ditampilkan terlebih dahulu

def cari(datauser,wahana):
    print('Jenis batasan umur:')
    print('1. Anak-anak (<17 tahun)')
    print('2. Dewasa (>=17 tahun)')
    print('3. Semua umur')
    print('')
    print('Jenis batasan tinggi badan:')
    print('1. Lebih dari 170 cm')
    print('2. Tanpa batasan')
    print('')
    umur = int(input('Batasan umur pemain: '))
    while (umur != 1) and (umur != 2) and (umur != 3):
        #jika input umur tidak sesuai opsi
        print('Batasan umur tidak valid!')
        umur = int(input('Batasan umur pemain: '))
    tinggi = int(input('Batasan tinggi badan: '))
    while (tinggi != 1) and (tinggi != 2):
        #jika input tinggi tidak sesuai opsi
        print('Batasan umur tidak valid!')
        tinggi = int(input('Batasan tinggi badan: '))
    print('')
    print('hasil pencarian:')

    #kondisi belum ditemukan
    ketemu = False
    #empat kondisi agar data ditemukan dan menampilkan pilihan wahana yang sesuai
    if(umur == 1) and (tinggi == 1):
        i = 0
        while (wahana[i] != ''):
            data = wahana[i]
            if (data[3] == 'anak - anak') and (data[4] == '>=170 cm'):
                ketemu = True
                if (datauser[7] == 'Ya'): #jika akun pemain gold
                    #harga wahana menjadi setengahnya
                    hargabaru = int(data[2]) // 2
                    print(data[0],data[1],hargabaru,sep='|')
                else:
                    print(data[0],data[1],data[2],sep='|')
            i = i + 1
    elif(umur == 1) and (tinggi == 2):
        i = 0
        while (wahana[i] != ''):
            data = wahana[i]
            if (data[3] == 'anak - anak') and (data[4] == 'tanpa batasan'):
                ketemu = True
                if (datauser[7] == 'Ya'): #jika akun pemain gold
                    #harga wahana menjadi setengahnya
                    hargabaru = int(data[2]) // 2
                    print(data[0],data[1],hargabaru,sep='|')
                else:
                    print(data[0],data[1],data[2],sep='|')
            i = i + 1
    elif(umur == 2) and (tinggi == 1):
        i = 0
        while (wahana[i] != ''):
            data = wahana[i]
            if (data[3] == 'dewasa') and (data[4] == '>=170 cm'):
                ketemu = True
                if (datauser[7] == 'Ya'): #jika akun pemain gold
                    #harga wahana menjadi setengahnya
                    hargabaru = int(data[2]) // 2
                    print(data[0],data[1],hargabaru,sep='|')
                else:
                    print(data[0],data[1],data[2],sep='|')
            i = i + 1
    elif(umur == 2) and (tinggi == 2):
        i = 0
        while (wahana[i] != ''):
            data = wahana[i]
            if (data[3] == 'dewasa') and (data[4] == 'tanpa batasan'):
                ketemu = True
                if (datauser[7] == 'Ya'): #jika akun pemain gold
                    #harga wahana menjadi setengahnya
                    hargabaru = int(data[2]) // 2
                    print(data[0],data[1],hargabaru,sep='|')
                else:
                    print(data[0],data[1],data[2],sep='|')
            i = i + 1
    elif(umur == 3) and (tinggi == 1):
        i = 0
        while (wahana[i] != ''):
            data = wahana[i]
            if (data[3] == 'semua') and (data[4] == '>=170 cm'):
                ketemu = True
                if (datauser[7] == 'Ya'): #jika akun pemain gold
                    #harga wahana menjadi setengahnya
                    hargabaru = int(data[2]) // 2
                    print(data[0],data[1],hargabaru,sep='|')
                else:
                    print(data[0],data[1],data[2],sep='|')
            i = i + 1
    elif(umur == 3) and (tinggi == 2):
        i = 0
        while (wahana[i] != ''):
            data = wahana[i]
            if (data[3] == 'semua') and (data[4] == 'tanpa batasan'):
                ketemu = True
                if (datauser[7] == 'Ya'): #jika akun pemain gold
                    #harga wahana menjadi setengahnya
                    hargabaru = int(data[2]) // 2
                    print(data[0],data[1],hargabaru,sep='|')
                else:
                    print(data[0],data[1],data[2],sep='|')
            i = i + 1
    if (ketemu == False): #jika data tidak sesuai
        print('Tidak ada wahana yang sesuai dengan pencarian kamu.')
          
