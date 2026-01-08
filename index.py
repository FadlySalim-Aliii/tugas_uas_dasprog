from motor import menu_motor, data_motor
from mobil import menu_mobil, data_mobil

print("=" * 100)
print("MASUKAN DATA DIRI ANDA UNTUK REGISTRASI!")
nama = input("\n=> Masukan Nama Lengkap Anda: ")
nomor = input("\n=> Masukan Nomor Telepon Anda: ")
print("=" * 100)

print(f"\nSELAMAT DATANG {nama} DI SHOWROOM BIFARY OTOMOTIVE".upper())
jawaban = input("\n=> Apakah Anda Ingin Melanjutkan Pembelian? (Yes/No): ").upper()

if jawaban == "YES":
    pilihan = input("\n=> Kendaraan Apa yang Anda Inginkan? (Motor/Mobil): ").upper()

    pesanan = []
    if pilihan == "MOTOR":
        pesanan_motor = menu_motor(data_motor)
        pesanan.extend(pesanan_motor)

        jawaban = input("\nApakah anda ingin melanjutkan untuk pembelian Mobil? (Yes/No): ").upper()
        if jawaban == "YES":
            pesanan_mobil = menu_mobil(data_mobil)
            pesanan.extend(pesanan_mobil)

    elif pilihan == "MOBIL":
        pesanan_mobil = menu_mobil(data_mobil)
        pesanan.extend(pesanan_mobil)

        jawaban = input("\nApakah anda ingin melanjutkan untuk pembelian Motor? (Yes/No): ").upper()
        if jawaban == "YES":
            pesanan_motor = menu_motor(data_motor)
            pesanan.extend(pesanan_motor)

    else:
        print("Pilihan tidak tersedia!")
        exit()
else:
    print("Terima kasih telah berkunjung.")
    exit()

print("\n" + "-" * 100)
print("\t\t\t\t\tSHOWROOM BIFARY OTOMOTIVE\t\t\t\t")
print("-" * 100)
print("No\tJenis Kendaraan\t\tHarga Pembelian\t\tTotal Pembelian\t\tTotal Harga Pembelian")
print("-" * 100)

total = 0
no = 1

for item in pesanan:
    harga = f"{item['harga_pembelian']:,}".replace(",", ".")
    jumlah = f"{item['jumlah_harga']:,}".replace(",", ".")
    print(f"{no:>2}\t{item['jenis']:<13}\t\tRp.{harga:<12}\t\t{item['banyak_beli']:^12}\t\tRp.{jumlah}")
    total += item['jumlah_harga']
    no += 1

pajak = total * 0.20
total_bayar = total + pajak

print("-" * 100)
print(f"\t\t\t\t\t\t\t\tTotal\t: Rp.{int(total):,}".replace(",", "."))
print(f"\t\t\t\t\t\t\t\tPajak 20%\t: Rp.{int(pajak):,}".replace(",", "."))
print(f"\t\t\t\t\t\t\t\tTotal Bayar\t: Rp.{int(total_bayar):,}".replace(",", "."))
print("\nKami Keluarga Besar SHOWROOM BIFARY OTOMOTIVE Mengucapkan")
print(f"Terima Kasih Banyak Kepada {nama} Karna Telah Melakukan Pembelian Kendaraan di Showroom Kami :)")
print("\nMohon untuk di tunggu Konfirmasi dari Tim kami perihal Kesiapan Kendaraan anda untuk di kirim")
print(f"Sesegera mungkin kami menghubungi anda melalui Telepon yang sudah terdaftar, yaitu {nomor}")
print("--------------------------------------------TERIMA KASIH----------------------------------------------")
