ANGGOTA_KELOMPOK = [
    {"nama": "I Kadek Aditya Januarta", "nim": "2501010247"},
    {"nama": "Dewa Putu Winaya", "nim": "2501010261"},
]


def tampilkan_info_kelompok():
    print("=" * 55)
    print("                  DATA KELOMPOK")
    print("=" * 55)
    for i, anggota in enumerate(ANGGOTA_KELOMPOK, start=1):
        print(f"{i}. {anggota['nama']} - NIM: {anggota['nim']}")
    print("=" * 55)
