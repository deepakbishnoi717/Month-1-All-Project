from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Update this with your PostgreSQL credentials
# Format: postgresql://user:password@localhost:5432/dbname
db_url = "postgresql://postgres:1234@localhost:5432/deepak"

engine = create_engine(db_url)

sessionlocalbank = sessionmaker(autocommit=False, autoflush=False, bind=engine)
