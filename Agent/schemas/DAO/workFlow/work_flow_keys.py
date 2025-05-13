from sqlalchemy import Column, Integer, String, DateTime
import datetime
from Agent.database.database import Base

class Workflow(Base):
    __tablename__ = 'workflow_keys'

    id = Column(Integer, primary_key=True)
    workflow_key = Column(String, nullable=False, unique=True)
    workflow_description = Column(String)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)