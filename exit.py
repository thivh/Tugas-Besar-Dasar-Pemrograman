def exit(user,wahana,pembelian,penggunaan,kepemilikan,refund,kritiksaran,savefile):
    #Menanyakan kepada user apakah user akan menyimpan data atau tidak
    opsi = input('Apakah anda mau melakukan penyimpanan file yang sudah dilakukan (Y/N) ? ')

    #melakukan aksi
    if (opsi == 'Y'):
        savefile.save(user,wahana,pembelian,penggunaan,kepemilikan,refund,kritiksaran)
    else: #opsi == 'N'
        print('Data tidak disimpan')
        
    return


