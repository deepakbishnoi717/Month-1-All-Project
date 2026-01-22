from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

db_url = "postgresql://postgres:1234@localhost:5432/deepak"

engine = create_engine(db_url)

Sessionlocal = sessionmaker(autocommit=False, autoflush=False,bind=engine)