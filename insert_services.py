from models import DeviceRawData
from db import sessionLocal

def insert_data(payload: dict):
    session = sessionLocal()

    try:
        metrics = DeviceRawData(
            signature_id = payload['signature'],
            timestamp = payload['timestamp'],
            device_address = payload['device_address'],
            request_type = payload['request_type'],
            is_location = payload['is_location'],
            latitude = payload['latitude'],
            longitude = payload['longitude'],
            peripherals = payload['peripherals']

        )
        session.add(metrics)
        session.commit()

    except Exception as e:
        session.rollback()
        print("DB Error:", e)

    finally:
        session.close()