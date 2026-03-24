from sqlalchemy import Column, BigInteger, String, Integer, Float, TIMESTAMP, func,TEXT
from sqlalchemy.orm import declarative_base
from db import Base
from sqlalchemy.dialects.postgresql import JSONB


class DeviceRawData(Base):
    __tablename__ = "device_raw_data"

    created_at = Column(TIMESTAMP,server_default=func.now(),primary_key=True)
    signature_id = Column(String(255),primary_key=True)
    timestamp = Column(Integer)
    device_address = Column(String(50))
    request_type = Column(Integer)
    is_location = Column(Integer)
    latitude = Column(TEXT)
    longitude = Column(TEXT)
    peripherals = Column(JSONB)
