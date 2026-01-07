data_mobil = {
    
    '121': {
        'jenis': 'Sedan', 
        'merk': 'Honda', 
        'model': 'Civic RS Turbo', 
        'cc': '1498 cc', 
        'harga': '625.000.000'
        },
    
    '122': {
        'jenis': 'SUV', 
        'merk': 'Toyota', 
        'model': 'Fortuner 2.4 VRZ', 
        'cc': '2393 cc', 
        'harga': '620.000.000'
        },
    
    '123': {
        'jenis': 'MPV', 
        'merk': 'Mitsubishi', 
        'model': 'XPander Ultimate', 
        'cc': '1499 cc', 
        'harga': '330.000.000'
        }
}

def menu_mobil(data_mobil):
    print("\n" + "-" * 100)
    print("\t\t\t\t\tPILIHAN KENDARAAN MOBIL\t\t\t\t\t")
    print("-" * 100)
    print("Kode\tJenis Mobil\tMerk\t\tModel\t\t\tCC\t\tHarga")
    print("-" * 100)
    print(" 121\tSedan\t\tHonda\t\tCivic RS Turbo\t\t1498 CC\t\tRp. 625.000.000")
    print(" 122\tSUV\t\tToyota\t\tFortuner 2.4 VRZ\t2393 CC\t\tRp. 620.000.000")
    print(" 123\tMPV\t\tMitsubishi\tXPander ultimate\t1499 CC\t\tRp. 330.000.000")
    print("-" * 100)

    pesanan = []
    kode_terpilih = set()

    while True:
        kode = input("\nMasukkan Kode Mobil: ")

        if kode not in data_mobil:
            print("Kode Mobil tidak tersedia!")
            continue

        if kode in kode_terpilih:
            print("Mobil ini sudah dipilih sebelumnya!")
            continue

        jumlah = int(input("Jumlah Beli: "))
        harga = int(data_mobil[kode]['harga'].replace(".", ""))
        kode_terpilih.add(kode)

        pesanan.append({
            'jenis': data_mobil[kode]['jenis'],
            'harga_pembelian': harga,
            'banyak_beli': jumlah,
            'jumlah_harga': harga * jumlah
        })

        lanjut = input("\nTambah mobil lagi? (Yes/No): ").upper()
        if lanjut != 'YES':
            break

    return pesanan