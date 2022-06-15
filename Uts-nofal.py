print ("Aplikasi sederhana untuk dealer motor\n")


print ("Tugas Uts")
print ("Nama\t: Moh. Nofalul Umam")
print ("NPM\t: 2021020100120")
print ("Kelas\t: TID\n")


print ("Silahkan pilih motor yang anda minati di dealer kami")

print ("Untuk produk ada HONDA dan YAMAHA \n")
class HONDA():

    def __init__(self, Tipe, Silinder, Warna):
        self.Tipe = Tipe
        self.Silinder = Silinder
        self.Warna = Warna
        
    def cek_motor (self):    
        print("Tipe \t:", self.Tipe)
        print ("Silinder \t:", self.Silinder)
        print ("Warna \t:", self.Warna)

class YAMAHA(HONDA):
    pass

Motor1 = HONDA ("CB100","110cc","Hitam \n")
Motor2 = HONDA ("MEGAPRO","156cc","Hitam \n")
Motor3 = HONDA ("TIGER","196cc","Merah \n")
Motor4 = YAMAHA ("RXKING","132cc","Hitam \n")

Motor1.cek_motor()
Motor2.cek_motor()
Motor3.cek_motor()
Motor4.cek_motor()

Motor = input ("Pilih Tipe Motor Yang Di Inginkan :")

if Motor == "CB100":
    print("Harga 8.500.000\n")
elif Motor == "cb100":
    print ("Harga 8.500.000\n")
elif Motor == "MEGAPRO":
    print ("Harga 10.500.000\n")
elif Motor == "megapro":
    print ("Harga 10.500.000\n")
elif Motor == "TIGER":
    print ("Harga 14.500.000\n")
elif Motor == "tiger":
    print ("Harga 14.500.000\n")
elif Motor == "RXKING":
    print ("Harga 12.500.000\n")
elif Motor == "rxking":
    print ("Harga 12.500.000\n")

Transaksi = input("Apakah motor ini akan anda beli..?")

if Transaksi == "iya":
    print ("pilih metode pembayaran\n")
    print ("MANDIRI","BCA","BNI","BRI\n")
elif Transaksi == "tidak":
    print ("terimakasih sudah berkunjung di dealer kami")
elif Transaksi == "y":
    print ("pilih metode pembayaran\n")
    print ("MANDIRI","BCA","BNI","BRI\n")
elif Transaksi == "t":
    print ("terimakasih sudah berkunjung di dealer kami")
    
pembayaran = input ("Pembayaran Melalul :")
    
print ("Program Selesai")