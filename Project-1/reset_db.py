from sqlalchemy import create_engine, text
from database import db_url

def reset_db():
    engine = create_engine(db_url)
    with engine.connect() as conn:
        print("Dropping old tables...")
        conn.execute(text("DROP TABLE IF EXISTS transactions CASCADE;"))
        conn.execute(text("DROP TABLE IF EXISTS bankdata CASCADE;"))
        conn.commit()
    print("Database reset successful. Ready for fresh table creation.")

if __name__ == "__main__":
    try:
        reset_db()
    except Exception as e:
        print(f"Error: {e}")
