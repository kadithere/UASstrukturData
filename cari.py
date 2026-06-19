def jalankan_cari(linked_list):
    print("=" * 55)
    print("              CARI DATA RESERVASI")
    print("=" * 55)

    if linked_list.is_kosong():
        print("Data reservasi masih kosong, tidak ada yang bisa dicari.\n")
        return

    keyword = input(
        "Masukkan kata kunci pencarian\n"
        "(bisa kode reservasi, nomor meja, nama customer,\n"
        "tanggal, atau waktu): "
    ).strip()

    if keyword == "":
        print("Keyword tidak boleh kosong!\n")
        return

    hasil = linked_list.cari_data(keyword)

    if len(hasil) == 0:
        print(f"\nData dengan kata kunci '{keyword}' tidak ditemukan.\n")
    else:
        print(f"\nDitemukan {len(hasil)} data yang cocok:\n")
        for posisi, node in hasil:
            print(f"  Posisi {posisi} -> {node.data}")
        print()
