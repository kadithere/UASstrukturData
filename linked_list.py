from node import Node


class DoublyLinkedList:
    def __init__(self):
        self.head = None   # node pertama
        self.tail = None   # node terakhir
        self.jumlah = 0     # jumlah data reservasi

    # TAMBAH DATA (di akhir list)
    def tambah_data(self, reservasi):
        node_baru = Node(reservasi)

        if self.head is None:
            # Jika list masih kosong
            self.head = node_baru
            self.tail = node_baru
        else:
            # Sambungkan node baru ke akhir list
            node_baru.prev_node = self.tail
            self.tail.next_node = node_baru
            self.tail = node_baru

        self.jumlah += 1
        return True


    # CARI DATA (searching)
  
    def cari_data(self, keyword):
        """
        Melakukan pencarian linear (linear search) pada
        doubly linked list. Keyword bisa berupa kode_reserv,
        nomor_meja, nama_cust, waktu, atau tanggal.
        Mengembalikan list berisi (posisi, node) yang cocok.
        """
        hasil = []
        current = self.head
        posisi = 1

        while current is not None:
            if current.data.cocok_dengan_keyword(keyword):
                hasil.append((posisi, current))
            current = current.next_node
            posisi += 1

        return hasil

    
    # CEK KODE RESERVASI SUDAH ADA ATAU BELUM
    
    def cek_kode_ada(self, kode_reserv):
        current = self.head
        while current is not None:
            if current.data.kode_reserv.lower() == kode_reserv.lower():
                return True
            current = current.next_node
        return False

    
    # HAPUS DATA BERDASARKAN POSISI
    
    def hapus_data(self, posisi):
        if self.head is None:
            return False, "Data masih kosong."

        if posisi < 1 or posisi > self.jumlah:
            return False, "Posisi tidak valid."

        current = self.head
        index = 1

        # Mencari node sesuai posisi
        while index < posisi:
            current = current.next_node
            index += 1

        # Atur ulang pointer prev & next
        if current.prev_node is not None:
            current.prev_node.next_node = current.next_node
        else:
            # Jika node yang dihapus adalah head
            self.head = current.next_node

        if current.next_node is not None:
            current.next_node.prev_node = current.prev_node
        else:
            # Jika node yang dihapus adalah tail
            self.tail = current.prev_node

        self.jumlah -= 1
        return True, current.data

    
    # TAMPILKAN SEMUA DATA
    
    def tampilkan_semua(self):
        hasil = []
        current = self.head
        posisi = 1

        while current is not None:
            hasil.append((posisi, current.data))
            current = current.next_node
            posisi += 1

        return hasil

   
    # CEK APAKAH LIST KOSONG
   
    def is_kosong(self):
        return self.head is None
