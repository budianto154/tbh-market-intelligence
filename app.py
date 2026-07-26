from database.database import init_database

def main():
    print("=" * 40)
    print("TBH Market Intelligence")
    print("=" * 40)

    init_database()

    print("Database berhasil dibuat.")
    print("Semua tabel berhasil dibuat.")

if __name__ == "__main__":
    main()