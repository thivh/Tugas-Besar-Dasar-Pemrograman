def lihat_laporan(datauser,kritiksaran,):
    if (datauser[5] == 'Admin'):
        #kondisi awal
        N = 0
    
    
        #menentukan jumlah indeks untuk mendeklarasikan array baru
        while (kritiksaran[N] != ''):
            N = N + 1
        
        #mendeklarasi array baru
        ks1 = ['' for i in range (N)]

        #mengisi array ks1
        for i in range(N):
            ks1[i] = kritiksaran[i]

    
        #mensort array ks1 secara alfabetis berdasarkan ID WAHANA
        for j in range(N-1):
            #Tentukan minimum
            imax = j
            for k in range (j+1,N):
                if(ks1[imax][2] > ks1[k][2]):
                    imax = k
            #ks1[imax] adalah minimum ks1[j..N]
            temp = ks1[imax]
            ks1[imax] = ks1[j]
            ks1[j] = temp
    

        #Menulis kritik dan saran
        print('Kritik dan saran:')
        for p in range(N):
            print(ks1[p][2],ks1[p][1],ks1[p][0],ks1[p][3],sep = '|')
            
    else : #akun pemain yang mengakses fungsi ini
        print('Hanya Admin yang dapat melakukan aksi ini!')
    return   
    
