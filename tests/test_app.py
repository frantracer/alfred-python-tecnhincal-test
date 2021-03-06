import uuid
from unittest.mock import MagicMock
from src.app import create_app
from src.device import DeviceType, Device, DeviceStatus


def test_get_a_device() -> None:
    db_mock = MagicMock()
    db_mock.get = MagicMock(return_value=Device(
        id=uuid.UUID('12345678-1234-1234-1234-123456789012'),
        device_type=DeviceType.SWITCH,
        status=DeviceStatus.ON))
    app = create_app(db_mock)

    with app.test_client() as client:
        response = client.get('/devices/12345678-1234-1234-1234-123456789012')
        assert response.status_code == 200
        assert response.json == {
            'id': '12345678-1234-1234-1234-123456789012',
            'device_type': 'SWITCH',
            'status': 'ON'
        }


def test_create_a_device() -> None:
    db_mock = MagicMock()
    db_mock.add = MagicMock(return_value=None)
    app = create_app(db_mock)

    with app.test_client() as client:
        response = client.post('/devices', json={
            'id': '12345678-1234-1234-1234-123456789012',
            'device_type': 'SWITCH',
            'status': 'ON'
        })
        assert response.status_code == 201
