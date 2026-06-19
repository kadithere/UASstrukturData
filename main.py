from linked_list import DoublyLinkedList
from data_kelompok import tampilkan_info_kelompok
from login import proses_login
from tambah import jalankan_tambah
from cari import jalankan_cari
from delete import jalankan_delete
from tampilkan import jalankan_tampilkan


def tampilkan_menu():
    print("=" * 55)
    print("     SISTEM RESERVASI TEMPAT MAKAN")
    print("=" * 55)
    print("1. Tambah Reservasi")
    print("2. Cari Reservasi")
    print("3. Batalkan / Hapus Reservasi")
    print("4. Tampilkan Semua Reservasi")
    print("5. Keluar")
    print("=" * 55)


def main():
    # Tampilkan info kelompok terlebih dahulu
    tampilkan_info_kelompok()
    print()

    # Proses login sebelum masuk ke menu utama
    if not proses_login():
        print("Program dihentikan.")
        return

    # Buat objek struktur data Doubly Linked List
    linked_list = DoublyLinkedList()

    while True:
        tampilkan_menu()
        pilihan = input("Pilih menu (1-5): ").strip()
        print()

        if pilihan == "1":
            jalankan_tambah(linked_list)
        elif pilihan == "2":
            jalankan_cari(linked_list)
        elif pilihan == "3":
            jalankan_delete(linked_list)
        elif pilihan == "4":
            jalankan_tampilkan(linked_list)
        elif pilihan == "5":
            print("Terima kasih telah menggunakan program ini. Sampai jumpa!")
            break
        else:
            print("Pilihan tidak valid, silakan coba lagi.\n")


if __name__ == "__main__":
    main()
