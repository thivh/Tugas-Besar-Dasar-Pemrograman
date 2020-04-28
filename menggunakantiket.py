# F08 - Menggunakan tiket
# Pemain dapat menggunakan tiket tersebut untuk bermain.

def menggunakantiket(datauser, kepemilikan, penggunaan):
    a=input('Masukkan ID wahana: ')
    b=input('Masukkan tanggal hari ini: ')
    c=input('Jumlah tiket yang digunakan: ')
    #jika data tiket milik pengguna belum ditemukan
    i = 0
    ketemu = False
    while (kepemilikan[i] != '') and (ketemu == False):
        data = kepemilikan[i]
        if (datauser[3] == data[0]) and (data[1] == a) and (data[2] >= c):
            ketemu = True
        else:
            i = i + 1
    if (ketemu == True):
        #data tiket milik pengguna sudah ditemukan
        print()
        print('Terima kasih telah bermain.')
        #tiket milik pengguna berkurang karena telah digunakan
        kepemilikan[i][2]=str(int(data[2])-int(c))

        #jika data penggunaan tiket belum ditemukan
        j = 0
        ketemu1 = False
        while (penggunaan[j] != '') and (ketemu1 == False) :
            data1 = penggunaan[j]
            if datauser[3] == data1[0] and data1[1] == a and data1[2] >= c:
                ketemu1 = True
            else:
                j = j + 1
        if (ketemu1 == True):
            #data penggunaan tiket ditemukan dan penggunaan oleh pengguna bertambah
            penggunaan[j][3] = str(int(data1[3])+int(c))
        else: #ketemu1 == False
            #jika data penggunaan tiket tidak ditemukan, membentuk array penggunaan baru
            penggunaan[j]=[datauser[3],b,a,c]
    else: #ketemu == False
        #jika data kepemilikan tidak ditemukan
        print()
        print('Tiket Anda tidak valid dalam sistem kami')

    return (kepemilikan, penggunaan)
