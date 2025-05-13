from Agent.database.database import Base
import datetime
from sqlalchemy import Column, Integer, ForeignKey, DateTime, JSON

class SessionsUserCommands(Base):
    __tablename__ = 'sessions_user_commands'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user_details.id"))
    jsonb = Column(JSON)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)