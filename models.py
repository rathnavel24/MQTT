from sqlalchemy import Column, BigInteger, String, Integer, Float, TIMESTAMP, func
from sqlalchemy.orm import declarative_base
from db import Base



class SystemMetrics(Base):
    __tablename__ = "system_metrics"

    created_at = Column(TIMESTAMP(timezone=True), server_default=func.now(), primary_key=True)

    hostname = Column(String, primary_key=True)

    cpu_usage = Column(Integer)
    cpu_status = Column(Integer)
    cpu_thershold=Column(Integer)

    ram_usage = Column(Integer)
    ram_free = Column(Float)
    ram_status = Column(Integer)
    ram_thershold = Column(Integer)

    disk_usage = Column(Integer)
    disk_free = Column(Float)
    disk_status = Column(Integer)
    disk_thershold = Column(Integer)


class ServiceStatus(Base):
    __tablename__ = "service_status"

    created_at = Column(TIMESTAMP(timezone=True), server_default=func.now(), primary_key=True)

    hostname = Column(String, primary_key=True)
    service_name = Column(String, primary_key=True)
    status = Column(Integer)