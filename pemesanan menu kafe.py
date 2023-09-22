pilihan = "y"

while pilihan.lower() == "y":
    print("""
    ==============================
    Kelompok 8
    List Menu Minuman Kopi 
    ==============================
    A. ES Kopi Susu : Rp 11.000
    B. ES Kopi Coklat : Rp 12.000
    C. ES Kopi Hitam : Rp 11.000
    D. Ice Americano : Rp 14.000
    ==============================
    """)
    
    pesan = input("Masukkan huruf menu kopi (A/B/C/D): ").lower()
    jumlahpesan = int(input("Masukkan jumlah pesanan: "))

    if pesan == "a":
        listnama = "ES Kopi Susu"
        harga = 11000 * jumlahpesan
    elif pesan == "b":
        listnama = "ES Kopi Coklat"
        harga = 12000 * jumlahpesan
    elif pesan == "c":
        listnama = "ES Kopi Hitam"
        harga = 11000 * jumlahpesan
    elif pesan == "d":
        listnama = "Ice Americano"
        harga = 14000 * jumlahpesan
    else:
        print("Menu tidak tersedia.")
        pilihan = input("Apakah Anda ingin memesan lagi? (Y/N): ").lower()
        continue

    ppn = int(harga * 0.1)
    diskon = 0

    if jumlahpesan >= 2:
        diskon = int(harga * 0.2)

    totalharga = harga - diskon + ppn

    print("--------------------------")
    print("Kelompok 8")
    print("--------------------------")
    print("Menu:", listnama)
    print("Jumlah Pesan:", jumlahpesan)
    print("Harga:", harga)
    print("Diskon:", diskon)
    print("PPN:", ppn)
    print("--------------------------")
    print("Jumlah Bayar:", totalharga)
    print("--------------------------")
    
    pilihan = input("Apakah Anda ingin order kembali? (Y/N): ").lower()

print("Terima kasih telah menggunakan layanan kami!")
