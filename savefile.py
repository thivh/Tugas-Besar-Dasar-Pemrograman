def save(user,wahana,pembelian,penggunaan,kepemilikan,refund,kritiksaran):
# Fungsi ini membutuhkan array data user, wahana, pembelian, penggunaan, kepemilikan, refund, dan kritiksaran
    import csv
    a = input('Masukkan nama File User: ') # variabel a sebagai file csv user sebagai tempat penyimpanan
    with open(a,'w',newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(['Nama','Tanggal_Lahir','Tinggi_Badan','Username','Password','Role','Saldo','Gold']) # sebagai header  
        i = 0
        while (user[i] != ''): # menuliskan setiap anggota dari array selama tidak kosong
            csvwriter.writerow(user[i])
            i = i + 1
    csvfile.close()
    
    a = input('Masukkan nama File Daftar Wahana: ') # variabel a sebagai file csv wahana sebagai tempat penyimpanan
    with open(a,'w',newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(['ID_Wahana','Nama_Wahana','Harga_Tiket','Batasan_Umur','Batasan_Tinggi'])  # sebagai header  
        i = 0
        while (wahana[i] != ''): # menuliskan setiap anggota dari array selama tidak kosong
            csvwriter.writerow(wahana[i])
            i = i + 1
    csvfile.close()
            
    a = input('Masukkan nama File Pembelian Tiket: ') # variabel a sebagai file csv pembelian tiket sebagai tempat penyimpanan
    with open(a,'w',newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(['Username','Tanggal_Pembelian','ID_Wahana','Jumlah_Tiket'])  # sebagai header   
        i = 0
        while (pembelian[i] != ''): # menuliskan setiap anggota dari array selama tidak kosong
            csvwriter.writerow(pembelian[i])
            i = i + 1
    csvfile.close()
            
    a = input('Masukkan nama File Penggunaan Tiket: ') # variabel a sebagai file csv penggunaan tiket sebagai tempat penyimpanan
    with open(a,'w',newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(['Username','Tanggal_Penggunaan','ID_Wahana','Jumlah_Tiket']) # sebagai header   
        i = 0
        while (penggunaan[i] != ''): # menuliskan setiap anggota dari array selama tidak kosong
            csvwriter.writerow(penggunaan[i])
            i = i + 1
    csvfile.close()
            
    a = input('Masukkan nama File Kepemilikan Tiket: ') # variabel a sebagai file csv kepemilikan tiket sebagai tempat penyimpanan
    with open(a,'w',newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(['Username','ID_Wahana','Jumlah_Tiket']) # sebagai header   
        i = 0
        while (kepemilikan[i] != ''): # menuliskan setiap anggota dari array selama tidak kosong
            csvwriter.writerow(kepemilikan[i])
            i = i + 1
    csvfile.close()
            
    a = input('Masukkan nama File Refund Tiket: ') # variabel a sebagai file csv refund sebagai tempat penyimpanan
    with open(a,'w',newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(['Username','Tanggal_Refund','ID_Wahana','Jumlah_Tiket']) # sebagai header   
        i = 0
        while (refund[i] != ''): # menuliskan setiap anggota dari array selama tidak kosong
            csvwriter.writerow(refund[i])
            i = i + 1
    csvfile.close()
            
    a = input('Masukkan nama File Kritik dan Saran: ') # variabel a sebagai file csv kritik saran sebagai tempat penyimpanan
    with open(a,'w',newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(['Username','Tanggal_Kritik','ID_Wahana','Isi_Kritik']) # sebagai header   
        i = 0
        while (kritiksaran[i] != ''): # menuliskan setiap anggota dari array selama tidak kosong
            csvwriter.writerow(kritiksaran[i])
            i = i + 1
    csvfile.close()
    
    print('Data berhasil disimpan!')
    return


