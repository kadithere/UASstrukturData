def jalankan_delete(linked_list):
    print("=" * 55)
    print("              BATALKAN / HAPUS RESERVASI")
    print("=" * 55)

    if linked_list.is_kosong():
        print("Data reservasi masih kosong, tidak ada yang bisa dihapus.\n")
        return

    # Tampilkan dulu data yang ada agar user tahu posisinya
    print("Data reservasi saat ini:\n")
    for posisi, data in linked_list.tampilkan_semua():
        print(f"  {posisi}. {data}")

    try:
        posisi = int(input("\nMasukkan posisi data yang ingin dibatalkan/dihapus: "))
    except ValueError:
        print("Input harus berupa angka!\n")
        return

    berhasil, info = linked_list.hapus_data(posisi)

    if berhasil:
        print(f"\nReservasi '{info.kode_reserv}' (a.n. {info.nama_cust}) "
              f"berhasil dibatalkan/dihapus.\n")
    else:
        print(f"\nGagal menghapus data: {info}\n")
