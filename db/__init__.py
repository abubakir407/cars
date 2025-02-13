from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Тип базы данных
SQL_DATABASE_URI = "sqlite:///sm58.db"

# Движок базы данных
engine = create_engine(SQL_DATABASE_URI)

# Сессия для хранения данных
SessionLocal = sessionmaker(bind=engine)

# Полноценная база данных
Base = declarative_base()

# Функция для подключения к бд
def get_db():
    db = SessionLocal()
    try:
        yield db
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()
