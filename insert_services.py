from models import ServiceStatus, SystemMetrics
from db import sessionLocal

def insert_data(payload: dict):
    session = sessionLocal()

    try:
        metrics = SystemMetrics(
            hostname=payload["HostName"],

            cpu_usage=payload["CPU"]["usage"],
            cpu_status=payload["CPU"]["status"],
            cpu_thershold = payload["CPU"]["THRESHOLD2"],

            ram_usage=payload["RAM"]["usage"],
            ram_free=payload["RAM"]["free"],
            ram_status=payload["RAM"]["status"],
            ram_thershold = payload["RAM"]["THRESHOLD3"],
            
            disk_usage=payload["Disk"]["usage"],
            disk_free=payload["Disk"]["free"],
            disk_status=payload["Disk"]["status"],
            disk_thershold =payload["Disk"]["THRESHOLD1"]
        )

        session.add(metrics)
        session.flush() 


        services = []
        for name, value in payload["Services"].items():
            services.append(
                ServiceStatus(
                    hostname=payload["HostName"],
                    service_name=name,
                    status=value["status"]
                )
            )

        session.bulk_save_objects(services)

        session.commit()

    except Exception as e:
        session.rollback()
        print("DB Error:", e)

    finally:
        session.close()