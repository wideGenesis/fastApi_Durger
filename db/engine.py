from databases import Database
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import declarative_base, sessionmaker


DB_URL = "sqlite:///sqlite.db"
METADATA = MetaData()
DATABASE = Database(DB_URL)

ENGINE = create_engine(DB_URL)
SESSION = sessionmaker(ENGINE)

BASE = declarative_base()

# BASE.metadata.create_all(bind=ASYNC_ENGINE)
