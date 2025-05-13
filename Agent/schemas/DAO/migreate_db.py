
import models
from Agent.database.database import Base, engine

Base.metadata.create_all(engine)

print("✅ All tables created successfully.")