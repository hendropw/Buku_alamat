from database import SessionLocal
from models import User

db = SessionLocal()
try:
    users = db.query(User).all()
    print("Koneksi OK, jumlah user:", len(users))
finally:
    db.close()
