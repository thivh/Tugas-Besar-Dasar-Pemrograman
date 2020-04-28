def load():
    import csv
    a = input('Masukkan nama File User: ') # variabel a sebagai file csv user yang akan digunakan
    with open(a) as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader) # baris pertama dilewati karena berisi header
        data = list(csvreader) # data dibuat menjadi array
        i = 0
        user = ['' for i in range(1000)] # array memiliki batas jumlah maksimal 1000
        for row in data: # memindahkan data pada file csv ke dalam array user
            user[i] = row
            i = i + 1
    
    a = input('Masukkan nama File Daftar Wahana: ') # variabel a sebagai file csv wahana yang akan digunakan
    with open(a) as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader) # baris pertama dilewati karena berisi header
        data = list(csvreader) # data dibuat menjadi array
        i = 0
        wahana = ['' for i in range(1000)] # array memiliki batas jumlah maksimal 1000
        for row in data: # memindahkan data pada file csv ke dalam array wahana
            wahana[i] = row
            i = i + 1
            
    a = input('Masukkan nama File Pembelian Tiket: ') # variabel a sebagai file csv pembelian tiket yang akan digunakan
    with open(a) as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader) # baris pertama dilewati karena berisi header
        data = list(csvreader) # data dibuat menjadi array
        i = 0
        pembelian = ['' for i in range(1000)] # array memiliki batas jumlah maksimal 1000
        for row in data: # memindahkan data pada file csv ke dalam array pembelian
            pembelian[i] = row
            i = i + 1
            
    a = input('Masukkan nama File Penggunaan Tiket: ') # variabel a sebagai file csv penggunaan tiket yang akan digunakan
    with open(a) as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader) # baris pertama dilewati karena berisi header
        data = list(csvreader) # data dibuat menjadi array
        i = 0
        penggunaan = ['' for i in range(1000)] # array memiliki batas jumlah maksimal 1000
        for row in data: # memindahkan data pada file csv ke dalam array penggunaan
            penggunaan[i] = row
            i = i + 1
            
    a = input('Masukkan nama File Kepemilikan Tiket: ') # variabel a sebagai file csv kepemilikan tiket yang akan digunakan
    with open(a) as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader) # baris pertama dilewati karena berisi header
        data = list(csvreader) # data dibuat menjadi array
        i = 0
        kepemilikan = ['' for i in range(1000)] # array memiliki batas jumlah maksimal 1000
        for row in data: # memindahkan data pada file csv ke dalam array kepemilikan
            kepemilikan[i] = row
            i = i + 1
            
    a = input('Masukkan nama File Refund Tiket: ') # variabel a sebagai file csv refund yang akan digunakan
    with open(a) as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader) # baris pertama dilewati karena berisi header
        data = list(csvreader) # data dibuat menjadi array
        i = 0
        refund = ['' for i in range(1000)] # array memiliki batas jumlah maksimal 1000
        for row in data: # memindahkan data pada file csv ke dalam array refund
            refund[i] = row
            i = i + 1
            
    a = input('Masukkan nama File Kritik dan Saran: ') # variabel a sebagai file csv kritik saran yang akan digunakan
    with open(a) as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader) # baris pertama dilewati karena berisi header
        data = list(csvreader) # data dibuat menjadi array
        i = 0
        kritiksaran = ['' for i in range(1000)] # array memiliki batas jumlah maksimal 1000
        for row in data: # memindahkan data pada file csv ke dalam array kritiksaran
            kritiksaran[i] = row
            i = i + 1
    csvfile.close() 
    print('File perusahaan Willy Wangky’s Chocolate Factory telah di-load.')
    return  (user,wahana,pembelian,penggunaan,kepemilikan,refund,kritiksaran) 
# hasil dari fungsi adalah array user,wahana,pembelian,penggunaan,kepemilikan,refund, dan kritiksaran
