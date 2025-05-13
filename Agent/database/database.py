from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.engine.url import make_url
from sqlalchemy import create_engine
from sqlalchemy import create_engine, text
from sqlalchemy.exc import OperationalError
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DB_URL")


db_url = make_url(os.getenv("DB_URL"))
db_name = db_url.database

admin_url = db_url.set(database="postgres") 

def create_database_if_not_exists():
    try:
        admin_engine = create_engine(admin_url, isolation_level='AUTOCOMMIT')
        with admin_engine.connect() as conn:
            result = conn.execute(text(f"SELECT 1 FROM pg_database WHERE datname = '{db_name}';"))
            exists = result.scalar()
            if not exists:
                conn.execute(text(f'CREATE DATABASE "{db_name}"'))
                print(f"✅ Database '{db_name}' created.")
            else:
                print(f"✅ Database '{db_name}' already exists.")
    except OperationalError as oe:
        print("❌ Could not connect to PostgreSQL server. Is it running?")
        raise oe
    except Exception as e:
        print("❌ Error checking/creating database:", str(e))
        raise

create_database_if_not_exists()


engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
Base = declarative_base()