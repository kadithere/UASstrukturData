def jalankan_tampilkan(linked_list):
    print("=" * 70)
    print("                    DAFTAR SEMUA RESERVASI")
    print("=" * 70)

    if linked_list.is_kosong():
        print("Data reservasi masih kosong.\n")
        return

    semua_data = linked_list.tampilkan_semua()

    print(f"Total reservasi: {linked_list.jumlah}\n")
    for posisi, data in semua_data:
        print(f"  {posisi}. {data}")
    print()
