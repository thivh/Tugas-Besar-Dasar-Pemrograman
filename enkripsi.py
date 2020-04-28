def enkripsi(password):
    hasil = ''
    x = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    letters = [word[0] for word in password]
    for i in range (len(letters)):
        for j in range(62):
            if(letters[i] == x[j]): # nilai setiap character diubah menjadi nilai urutan character pada array
                hasil = hasil + str(j+1) # hasil angka digabung menjadi satu
    return hasil