from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLite database configuration: URL pointing to the SQLite database file
SQLALCHEMY_DATABASE_URL = "sqlite:///./f1.db"

# Create the SQLAlchemy engine that will connect to the SQLite database.
# The `connect_args` parameter is used to disable the check for the same thread,
# allowing multiple threads to use the same database connection.
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

# Create a new session factory. Sessions will not automatically commit or flush 
# unless specified, allowing for more controlled transactions.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a base class for declarative models. This class maintains a catalog of classes and tables relative to that base.
Base = declarative_base()
