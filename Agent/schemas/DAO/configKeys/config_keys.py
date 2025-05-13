from sqlalchemy import Column, Integer, String, DateTime
import datetime
from Agent.database.database import Base

class ConfigKeys(Base):
    __tablename__ = 'config_keys'

    id = Column(Integer, primary_key=True)
    config_key = Column(String, nullable=False)
    config_key_value = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)