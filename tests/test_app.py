import uuid
from unittest.mock import MagicMock

from alfred_device_manager.app import create_app
from alfred_device_manager.domain.device import DeviceType, Device, DeviceStatus
from alfred_device_manager.domain.device_repository import DeviceRepository


def test_get_a_device() -> None:
    db_mock = MagicMock(spec=DeviceRepository)
    db_mock.get = MagicMock(return_value=Device(
        id=uuid.UUID('12345678-1234-1234-1234-123456789012'),
        device_type=DeviceType.LIGHT_MODBUS,
        status=DeviceStatus.ON,
        additional_info={
            "address": "0x42"
        }))
    app = create_app(db_mock)

    with app.test_client() as client:
        response = client.get('/devices/12345678-1234-1234-1234-123456789012')
        assert response.status_code == 200
        assert response.json == {
            'id': '12345678-1234-1234-1234-123456789012',
            'device_type': 'LIGHT_MODBUS',
            'status': 'ON',
            'additional_info': {
                "address": "0x42"
            }
        }


def test_create_a_device() -> None:
    db_mock = MagicMock(spec=DeviceRepository)
    db_mock.add = MagicMock(return_value=None)
    app = create_app(db_mock)

    with app.test_client() as client:
        response = client.post('/devices', json={
            'id': '66047efb-cce2-46da-a372-f51af9db16f9',
            'device_type': 'LIGHT_MODBUS',
            'status': 'ON',
            'additional_info': {
                "address": "0x84"
            }
        })
        assert response.status_code == 201
