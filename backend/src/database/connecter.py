import os

from dotenv import load_dotenv
from pyodbc import drivers
from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

load_dotenv()

driver = drivers()[-1]


connection_url = URL.create(
    "mssql+pyodbc",
    host=os.getenv("DB_HOST", ""),
    database=os.getenv("DB_NAME", ""),
    password=os.getenv("DB_PASSWORD", ""),
    port=int(os.getenv("DB_PORT", "0")),
    username=os.getenv("DB_USER", ""),
    query={"driver": driver, "Encrypt": "yes", "TrustServerCertificate": "no"},
)
engine = create_engine(
    connection_url,
    echo=True,
    connect_args={"TrustServerCertificate": "yes"},
    pool_pre_ping=True,
    pool_recycle=3600,
    pool_timeout=30,
)


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
