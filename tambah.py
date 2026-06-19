from reservasi import Reservasi


def jalankan_tambah(linked_list):
    print("=" * 55)
    print("              TAMBAH DATA RESERVASI")
    print("=" * 55)

    kode_reserv = input("Kode Reservasi  : ").strip()
    if kode_reserv == "":
        print("Kode reservasi tidak boleh kosong!\n")
        return

    # Pastikan kode reservasi belum digunakan
    if linked_list.cek_kode_ada(kode_reserv):
        print(f"Kode reservasi '{kode_reserv}' sudah digunakan. "
              "Silakan gunakan kode lain.\n")
        return

    nomor_meja = input("Nomor Meja      : ").strip()
    nama_cust = input("Nama Customer   : ").strip()
    tanggal = input("Tanggal (dd-mm-yyyy) : ").strip()
    waktu = input("Waktu (hh:mm)   : ").strip()

    if nomor_meja == "" or nama_cust == "" or tanggal == "" or waktu == "":
        print("Semua data wajib diisi, tidak boleh ada yang kosong!\n")
        return

    reservasi_baru = Reservasi(
        kode_reserv=kode_reserv,
        nomor_meja=nomor_meja,
        nama_cust=nama_cust,
        waktu=waktu,
        tanggal=tanggal,
    )

    linked_list.tambah_data(reservasi_baru)
    print(f"\nReservasi dengan kode '{kode_reserv}' berhasil ditambahkan.\n")
