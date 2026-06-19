class Reservasi:
    def __init__(self, kode_reserv, nomor_meja, nama_cust, waktu, tanggal):
        self.kode_reserv = kode_reserv
        self.nomor_meja = nomor_meja
        self.nama_cust = nama_cust
        self.waktu = waktu
        self.tanggal = tanggal

    def __str__(self):
        return (
            f"Kode: {self.kode_reserv} | "
            f"Meja: {self.nomor_meja} | "
            f"Nama: {self.nama_cust} | "
            f"Tanggal: {self.tanggal} | "
            f"Waktu: {self.waktu}"
        )

    def cocok_dengan_keyword(self, keyword):
        """
        Mengecek apakah keyword cocok dengan salah satu
        field dari reservasi ini (untuk fitur searching).
        Pencarian tidak membedakan huruf besar/kecil.
        """
        keyword = keyword.lower()
        gabungan = (
            f"{self.kode_reserv} {self.nomor_meja} "
            f"{self.nama_cust} {self.waktu} {self.tanggal}"
        ).lower()
        return keyword in gabungan
