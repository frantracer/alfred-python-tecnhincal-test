import uuid

from flask import Flask, request

from alfred_device_manager.domain.device import Device, DeviceType, DeviceStatus
from alfred_device_manager.domain.device_repository import DeviceRepository


def create_app(device_db: DeviceRepository) -> Flask:
    app = Flask(__name__)

    @app.route("/devices/<device_id>", methods=["GET"])
    def one_device(device_id: str):
        if request.method == "GET":
            device = device_db.get(uuid.UUID(device_id))
            if device is None:
                return "", 404

            return {
                "id": str(device.id),
                "device_type": str(device.device_type.value),
                "status": str(device.status.value),
                "additional_info": device.additional_info
            }

        return "", 405

    @app.route("/devices", methods=["POST"])
    def devices():
        if request.method == "POST":
            device = Device(
                id=uuid.UUID(request.json["id"]),
                device_type=DeviceType(request.json["device_type"]),
                status=DeviceStatus(request.json["status"]),
                additional_info=request.json["additional_info"]
            )
            device_db.add(device)
            return "", 201

        return "", 405

    @app.route("/devices/<device_id>/command/<command>", methods=["POST"])
    def send_command(device_id: str, command: str):
        print(f"Sending command {command} to device {device_id}")
        return "", 200

    return app
