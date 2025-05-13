import datetime
from sqlalchemy import Column, Integer, String, Boolean,DateTime
from Agent.database.database import Base

class UserDetails(Base):
    __tablename__ = 'user_details'

    id = Column(Integer, primary_key=True)
    user_name = Column(String, nullable=False)
    email_id = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)