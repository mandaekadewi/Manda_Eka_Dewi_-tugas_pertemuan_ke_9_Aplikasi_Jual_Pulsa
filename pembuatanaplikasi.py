
nomor_kartu = input("Masukan Nomor Hp : ")
nama_kartu = input("Nama Kartu [indosat/ XL/ Telkomsel]: ")

if  nama_kartu == "Indosat" or "indosat" :
    kode_pulsa = "Indosat/indosat"
    if nomor_kartu > str (62814):
        nomor_kartu > str (62815)
        nomor_kartu > str (62816)
        nomor_kartu > str (62855)
        nomor_kartu > str (62856)
        nomor_kartu > str (62857)
        nomor_kartu > str (62858)
    else :
        nomor_kartu > 0
                
elif nama_kartu == "XL" :
     if nomor_kartu > str (62817):
         nomor_kartu > str (62818)
         nomor_kartu > str (62819)
         nomor_kartu > str (62859)
         nomor_kartu > str (62877)
         nomor_kartu > str (62878)
     else :
         nomor_kartu > 0 
        

elif nama_kartu == "Telkomsel" or "telkomsel" :
    if nomor_kartu > str (62852) :
        nomor_kartu > str (62853)
        nomor_kartu > str (62851)
        nomor_kartu > str (62811)
        nomor_kartu > str (62812)
    else :
        nomor_kartu > 0
        
elif nama_kartu == " Smartfreen" or "smartfreen":
    if nomor_kartu > str (62881):
        nomor_kartu > str (62882)
        nomor_kartu > str (62883)
        nomor_kartu > str (62884)
        nomor_kartu > str (62885)
        nomor_kartu > str (62886)
        nomor_kartu > str (62887)
        nomor_kartu > str (62888)
        nomor_kartu > str (62889)
    else:
        nomor_kartu > 0

elif nama_kartu == " Exis" or "exis" :
    if nomor_kartu > str (62813) :
        nomor_kartu > str (62832)
        nomor_kartu > str (62833)
        nomor_kartu > str (62838)
    else :
        nomor_kartu > 0

elif nama_kartu == "Trie" or "3" :
    if nomor_kartu > str (628998):
        nomor_kartu > str (628979)
        nomor_kartu > str (6289916)
        nomor_kartu > str (628963)
        nomor_kartu > str (628964)
    else :
        nomor_kartu > 0 

else : 
    nama_kartu == "Tidak Terdaftar"
    nomor_kartu > 0

saldo = int(1000000)
lanjut_beli = "ya"
def beli_pulsa (p) :
    global saldo 
    if saldo >= int (p) :
        saldo -= int (p)
        print("Selamat and sukses membeli pulsa Rp.", saldo )
    else :
        print("Maaf pembelian pulsa anda gagal")
        
def jenis_pulsa (j): 
    global pulsa 
    print("1.Beli pulsa Rp.5.000")
    print("2.Beli Pulsa Rp.10.000")
    print("3.Beli Pulsa Rp.20.000")
    print("4.Beli Pulsa Rp.25.000")
    print("5.Beli Pulsa Rp.30.000")
    print("7.Beli Pulsa Rp.40.000")
    print("8.Beli Pulsa Rp.45.000")
    print("9.Beli Pulsa Rp.50.000")
    print("10.Beli Pulsa Rp.100.000")
    a = int(input("Silakan Pilih Pulsa yang ingin di beli : "))
    if a == 1 : 
        jenis_pulsa(5000)
    elif a == 2 : 
        jenis_pulsa(1000)
    elif a == 3 :
        jenis_pulsa(20000)
    elif a == 4 : 
        jenis_pulsa(25000)
    elif a == 5 :
        jenis_pulsa(30000)
    elif a == 6 :
        jenis_pulsa(40000)
    elif a == 7 :
        jenis_pulsa(45000)
    elif a == 8 :
        jenis_pulsa(50000)
    elif a == 9 :
        jenis_pulsa(100000)
    else:
        print("Pulsa tidak tersedia")

while lanjut_beli == "ya":
    print ("=+=+=+=+=+ Manda Cell=+=+=+=+=+")
    print ("===============================")
    print ("Masukan Nomor : ", nomor_kartu)
    print ("Jenis Kartu : ", nama_kartu)
    print ("Pilih Jenis Pulsa : " )
    print ("Selamat Transaksi Anda Berhasil")


  


    