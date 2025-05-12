from Agent.schemas.schemas import User
from Agent.database.database import SessionLocal

def get_users():
    db = SessionLocal()
    users = db.query(User).all()
    db.close()
    return users

def create_user(user_data):
    db = SessionLocal()
    user = User(**user_data.dict())
    db.add(user)
    db.commit()
    db.refresh(user)
    db.close()
    return user
