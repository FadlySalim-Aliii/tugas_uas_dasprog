data_motor = {
    
    '111': {
        'jenis': 'Matic', 
        'merk': 'Honda', 
        'model': 'Vario', 
        'cc': '160 cc', 
        'harga': '28.330.000'
        },
    
    '112': {
        'jenis': 'Sport', 
        'merk': 'Yamaha', 
        'model': 'R15', 
        'cc': '155 cc', 
        'harga': '40.000.000'
        },
    
    '113': {
        'jenis': 'Harley', 
        'merk': 'Harley-Davidson', 
        'model': 'Street 750', 
        'cc': '749 cc', 
        'harga': '285.000.000'
        }
}

def menu_motor(data_motor):
    print("\n" + "-" * 100)
    print("\t\t\t\t\tPILIHAN KENDARAAN MOTOR\t\t\t\t\t")
    print("-" * 100)
    print("Kode\tJenis Motor\tMerk\t\t\tModel\t\tCC\t\tHarga")
    print("-" * 100)
    print(" 111\tMatic\t\tHonda\t\t\tVario\t\t160 CC\t\tRp. 28.330.000")
    print(" 112\tSport\t\tYamaha\t\t\tR15\t\t155 CC\t\tRp. 40.000.000")
    print(" 113\tHarley\t\tHarley-Davidson\t\tStreet 750\t749 CC\t\tRp. 285.000.000")
    print("-" * 100)

    pesanan = []
    kode_terpilih = set()

    while True:
        kode = input("\nMasukkan Kode Motor: ")

        if kode not in data_motor:
            print("Kode motor tidak tersedia!")
            continue

        if kode in kode_terpilih:
            print("Motor ini sudah dipilih sebelumnya!")
            continue

        jumlah = int(input("Jumlah Beli: "))
        harga = int(data_motor[kode]['harga'].replace(".", ""))
        kode_terpilih.add(kode)

        pesanan.append({
            'jenis': data_motor[kode]['jenis'],
            'harga_pembelian': harga,
            'banyak_beli': jumlah,
            'jumlah_harga': harga * jumlah
        })

        lanjut = input("\nTambah motor lagi? (Yes/No): ").upper()
        if lanjut != 'YES':
            break

    return pesanan