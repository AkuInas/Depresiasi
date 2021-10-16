c = 0
while(c < 1):
    aset = float(input("Menghitung Depresiasi\nNominal: "))
    lama = int(input("Lama Depresiasi(tahun): "))
    awal = int(input("Awal : "))
    akhir = int(input("Akhir : "))
    sisa = float(input("Residu Aset: "))

    def depr(aset, lama, awal, akhir, sisa):
        if (aset != None and lama != None and awal != None and akhir != None and sisa != None):
            if(awal < akhir):
                print()
                print("="*30)
                print(' '*5,'Tabel Depresiasi')
                print("="*30)
                print('Aset | Tahun | Akumulasi | Residu')
                print("-"*30)

                penyusutan = (aset - sisa) / lama
                for masa in range(awal, (akhir+1), 1):
                    akumulasi = masa * penyusutan
                    sisa = aset - akumulasi
                    print(aset, masa, akumulasi, sisa)
            else:
                print("False")
        else:
            print("Ingin hitung lagi? (y/t)" )
            jawab = input("y")
            if jawab =='t':
                c = 1


    depr(aset, lama, awal, akhir, sisa)