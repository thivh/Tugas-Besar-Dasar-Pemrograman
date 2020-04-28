import loadfile
import savefile
import login
import tambahwahana
import cariwahana
import goldenaccount
import enkripsi
import signup
import r3fund
import caripemain
import kritikdansaran
import menggunakantiket
import exit
import lihat_laporan
import topup
import riwayat_wahana
import tiket_pemain
import beli_tiket

print('Selamat datang ke wahana bermain Willy Wangky!')
print('')
print('Mohon memasukkan nama file:')

(user,wahana,pembelian,penggunaan,kepemilikan,refund,kritiksaran) = loadfile.load()
print('')

print('Silahkan login terlebih dahulu.')
datauser = []
datauser = login.login(user)
while (datauser == []):
    datauser = login.login(user)
print('')

if(datauser[5] == 'Pemain'):
    print('')
    print('Silahkan pilih nomor fitur yang diinginkan.')
    print('1. save file')
    print('2. mencari wahana')
    print('3. membeli tiket')
    print('4. menggunakan tiket')
    print('5. refund')
    print('6. menambahkan kritik dan saran baru')
    print('7. exit')
elif(datauser[5] == 'Admin'):
    print('')
    print('Silahkan pilih nomor fitur yang diinginkan.')
    print('1. save file')
    print('2. sign up user')
    print('3. mencari pemain')
    print('4. mencari wahana')
    print('5. melihat kritik dan saran')
    print('6. menambahkan wahana baru')
    print('7. top up saldo')
    print('8. melihat riwayat penggunaan wahana')
    print('9. melihat jumlah tiket pemain')
    print('10. upgrade golden account')
    print('11. exit')

masukan = str(input('Masukkan nomor fitur yang diinginkan: '))
while (masukan != '15'):
    if (masukan == '1'):
        savefile.save(user,wahana,pembelian,penggunaan,kepemilikan,refund,kritiksaran)
    elif(masukan == '2' and datauser[5] == 'Admin'):
        user = signup.signup(datauser,user)
    elif (masukan == '3' and  datauser[5] == 'Admin'):
        caripemain.caripemain(datauser,user)
    elif (masukan == '2' and datauser[5] == 'Pemain') or (masukan == '4' and datauser[5] == 'Admin'):
        cariwahana.cari(datauser,wahana)
    elif (masukan == '3' and datauser[5] == 'Pemain'):
        (user,datauser,pembelian,kepemilikan) = beli_tiket.belitiket(datauser, user, wahana, kepemilikan, pembelian)
    elif (masukan == '4' and datauser[5] == 'Pemain'):
        (kepemilikan,penggunaan) = menggunakantiket.menggunakantiket(datauser, kepemilikan, penggunaan)
    elif (masukan == '5' and datauser[5] == 'Pemain'):
        (user,kepemilikan,datauser,refund) = r3fund.uangkembali(user,wahana,datauser,kepemilikan,refund)
    elif (masukan == '6' and datauser[5] == 'Pemain'):
        kritiksaran = kritikdansaran.kritiksaran1(datauser, kritiksaran)
    elif (masukan == '5' and  datauser[5] == 'Admin'):
        lihat_laporan.lihat_laporan(datauser,kritiksaran)
    elif (masukan == '6' and  datauser[5] == 'Admin'):
        wahana = tambahwahana.tambahwahana(datauser,wahana)
    elif (masukan == '7' and  datauser[5] == 'Admin'):
        (user,datauser) = topup.topup(datauser,user)
    elif (masukan == '8' and  datauser[5] == 'Admin'):
        riwayat_wahana.riwayatwahana(datauser, penggunaan)
    elif (masukan == '9' and  datauser[5] == 'Admin'):
        tiket_pemain.tiketpemain(datauser, wahana, kepemilikan)
    elif (masukan == '10' and  datauser[5] == 'Admin'):
        user = goldenaccount.upgrade(datauser,user)
    elif (masukan == '7' and datauser[5] == 'Pemain') or (masukan == '11' and datauser[5] == 'Admin'):
        exit.exit(user,wahana,pembelian,penggunaan,kepemilikan,refund,kritiksaran,savefile)

    print()
    if(datauser[5] == 'Pemain'):
        print('')
        print('Silahkan pilih nomor fitur yang diinginkan.')
        print('1. save file')
        print('2. mencari wahana')
        print('3. membeli tiket')
        print('4. menggunakan tiket')
        print('5. refund')
        print('6. menambahkan kritik dan saran baru')
        print('7. exit')
    elif(datauser[5] == 'Admin'):
        print('')
        print('Silahkan pilih nomor fitur yang diinginkan.')
        print('1. save file')
        print('2. sign up user')
        print('3. mencari pemain')
        print('4. mencari wahana')
        print('5. melihat kritik dan saran')
        print('6. menambahkan wahana baru')
        print('7. top up saldo')
        print('8. melihat riwayat penggunaan wahana')
        print('9. melihat jumlah tiket pemain')
        print('10. upgrade golden account')
        print('11. exit')
    masukan = input('Masukkan nomor fitur yang diinginkan: ')
    print('')
