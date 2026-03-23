from sqlalchemy import Column, BigInteger, String, Integer, Float, TIMESTAMP, func
from sqlalchemy.orm import declarative_base
from db import Base



class SystemMetrics(Base):
    __tablename__ = "system_metrics"

    id = Column(BigInteger, primary_key=True)
    created_at = Column(TIMESTAMP(timezone=True), server_default=func.now(), primary_key=True)

    hostname = Column(String, nullable=False)

    cpu_usage = Column(Integer)
    cpu_status = Column(Integer)

    ram_usage = Column(Integer)
    ram_free = Column(Float)
    ram_status = Column(Integer)

    disk_usage = Column(Integer)
    disk_free = Column(Float)
    disk_status = Column(Integer)


class ServiceStatus(Base):
    __tablename__ = "service_status"

    id = Column(BigInteger, primary_key=True)
    created_at = Column(TIMESTAMP(timezone=True), server_default=func.now(), primary_key=True)

    hostname = Column(String, nullable=False)
    service_name = Column(String, nullable=False)
    status = Column(Integer)