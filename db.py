from sqlalchemy.orm import sessionmaker,declarative_base
from sqlalchemy import create_engine


conn  = "postgresql://postgres:1234@localhost:5432/postgres"
engine  = create_engine(conn)

sessionLocal = sessionmaker(bind = engine)

Base = declarative_base()