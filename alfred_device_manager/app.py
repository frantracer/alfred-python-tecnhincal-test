import uuid

from flask import Flask, request

from alfred_device_manager.domain.device import Device, DeviceType, DeviceStatus
from alfred_device_manager.infrastructure.database import InMemoryDeviceDatabase


def create_app(device_db: InMemoryDeviceDatabase) -> Flask:
    app = Flask(__name__)

    @app.route("/devices/<device_id>", methods=["GET"])
    def one_device(device_id: str):
        if request.method == "GET":
            device = device_db.get(uuid.UUID(device_id))
            return {
                "id": str(device.id),
                "device_type": str(device.device_type.value),
                "status": str(device.status.value)
            }
        else:
            return "", 405

    @app.route("/devices", methods=["POST"])
    def devices():
        if request.method == "POST":
            device = Device(
                id=uuid.UUID(request.json["id"]),
                device_type=DeviceType(request.json["device_type"]),
                status=DeviceStatus(request.json["status"])
            )
            device_db.add(device)
            return "", 201
        else:
            return "", 405

    return app
