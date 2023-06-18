from sqlalchemy import String, Integer, Column
from config.database import Base


class Mock(Base):
    __tablename__ = 'mocks'

    id = Column(Integer, primary_key=True, index=True)
    endpoint = Column(String, index=True, unique=True)
    prompt = Column(String)
    response = Column(String)
