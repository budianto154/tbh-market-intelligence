from database.database import SessionLocal
from database.models import MarketSnapshot

#digunakan untuk membersihkan snapshot yang ada di database

db = SessionLocal()

db.query(MarketSnapshot).delete()

db.commit()

print("Snapshot cleaned")