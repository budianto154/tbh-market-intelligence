from database.database import engine
from database.models import Base


def main():
    print("=" * 40)
    print("TBH Market Intelligence")
    print("=" * 40)

    Base.metadata.create_all(bind=engine)

    print("Database berhasil dibuat.")
    print("Semua tabel berhasil dibuat.")


if __name__ == "__main__":
    main()