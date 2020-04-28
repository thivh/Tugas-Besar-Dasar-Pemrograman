def uangkembali(user,wahana,datauser,kepemilikan,refund):
    
    #membuat fungsi menentukan nilai uang yang akan di refund
    def uang_refund(datauser,x):
        #kondisi awal
        o = 0
        ketemu = False
        while (wahana[o] != '') and (ketemu == False):
            if (wahana[o][0] == x):
                ketemu = True
                if (datauser[7] == 'Ya'): #user mempunyai golden ticket
                    uang_refund = (int(wahana[o][2]) // 2) - 10000
                else : # user pengguna biasa
                    uang_refund = int(wahana[o][2]) - 10000
            else :
                o = o + 1
                        
        if (ketemu == False):
            uang_refund = 0
                
                
        return uang_refund
    
    #Melakukan refund hanya dilakukan oleh pemain
    if datauser[5] == 'Pemain':
        wahana_cari = str(input('Masukkan ID wahana: '))#Input id wahana yg dicari
        tggl_refund = str(input('Masukkan Tanggal Refund: '))#dd/mm/yy
        jmlh_tiket = int(input('Jumlah kepemilikan yang di-refund: '))#input jmlh kepemilikan yang mau di refund
        uang_refund = uang_refund(datauser,wahana_cari) #menentukan nilai variabel uang_refund

        #kondisi awal
        i = 0
        ketemu1 = False
        
        #mencari data yang sesuai pada array kepemilikan dan mengurangi tiket pada array kepemilikan sejumlah tiket yang akan di refund
        while (kepemilikan[i] != '') and (ketemu1 == False):
            kepemilikan1 = kepemilikan[i]
            tiket_punya = int(kepemilikan1[2])
            if (kepemilikan1[0] == datauser[3]) and (kepemilikan1[1] == wahana_cari) and (tiket_punya >= jmlh_tiket):
                ketemu1 = True
            else: #belom ketemu
                i = i + 1
    
        if ketemu1 == True:

            #Menambahkan uang refund kepada saldo -- (1)
            saldo_baru = (int(datauser[6]) + (uang_refund*jmlh_tiket)) # menambahkan uang refund kepada saldo
            datauser[6] = str(saldo_baru)

            #(1) kondisi awal
            m = 0
            ketemu2 = False

            #(1) Mencari indeks sesuai
            while (user[m] == '') and (ketemu2 == False):
                if (user[m][3] == datauser[3]): #jika array dengan indeks m mempunya data sama dengan datauser[3]
                    ketemu2 = True
                else:
                    m = m + 1
                    
            #(1) Mengubah data pada array USER        
            if (ketemu2 == True):
                user[m][6] = str(saldo_baru)
                
            
            print()
            print('Uang refund sudah kami berikan pada akun Anda.')
            
            #mengubah jumlah tiket yang dimiliki user pada array
            kepemilikan[i][2] = str(int(kepemilikan[i][2]) - jmlh_tiket)
            
            #Menuliskan hasil refund tiket kedalam array refund -- (2)

            #Kondisi awal
            j = 0
            ketemu3= False

            #(2)Menetukan indeks array refund yang akan diubah
            while (refund[j] != '') and (ketemu3 == False):
                refund1 = refund[j]
                if (refund1[0] == datauser[3]) and (refund1[1] == tggl_refund) and (refund1[2] == wahanca_cari):  
                    ketemu3 = True
                else: #belom ketemu
                    j = j + 1
            #(2)Menuliskan data baru pada indeks array refund yang telah ditentukan
            if (ketemu3 == True):
                data_baru =  str(int(refund[j][3]) + jmlh_tiket)
                refund[j] = data_baru
            else: #(ketemu3 == False)
                data_baru = [datauser[3],tggl_refund,wahana_cari,str(jmlh_tiket)]
                refund[j] = data_baru
                    
        else: #pemain ternyata tidak memiliki tiket tersebut (ketemu1 = False)
            print()
            print('Anda tidak memiliki tiket terkait.')
    
    else:
        print()
        print('Hanya pemain yang dapat melakukan aksi ini!')
        
    return (user,kepemilikan,datauser,refund)
