# Data akun yang valid (silakan ubah sesuai kebutuhan)
USERNAME_VALID = "admin"
PASSWORD_VALID = "12345"

MAX_PERCOBAAN = 3


def proses_login():
    """
    Menjalankan proses login.
    Mengembalikan True jika login berhasil, False jika gagal.
    """
    print("=" * 55)
    print("                      LOGIN")
    print("=" * 55)

    for percobaan in range(1, MAX_PERCOBAAN + 1):
        username = input("Username : ").strip()
        password = input("Password : ").strip()

        if username == USERNAME_VALID and password == PASSWORD_VALID:
            print("\nLogin berhasil! Selamat datang.\n")
            return True
        else:
            sisa = MAX_PERCOBAAN - percobaan
            print(f"Username/Password salah. Sisa percobaan: {sisa}\n")

    print("Anda telah melewati batas percobaan login.")
    return False
