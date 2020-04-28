# F10 - Kritik dan Saran
# Pemain dapat memberikan kritik dan saran untuk suatu wahana.
# Diasumsikan ID Wahana, tanggal pelaporan valid.

#ID wahana valid dan tanggal pelaporan dianggap sudah valid
def kritiksaran1(datauser, kritiksaran):
    #kritik dan saran diberikan oleh pemain
    if datauser[5] == "Pemain":
        a= input('Masukkan ID Wahana: ')
        b= input('Masukkan tanggal pelaporan: ')
        c= input('Kritik/saran Anda: ')
        i = 0
        while (kritiksaran[i] != ''):
            i = i + 1
        #kritik dan saran dari pengguna membentuk array baru
        print(i)
        kritiksaran[i] = [datauser[3],b,a,c]
        print()
        print('Kritik dan saran Anda kami terima.')

    return kritiksaran
