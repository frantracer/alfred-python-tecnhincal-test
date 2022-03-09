import uuid
from typing import Optional
from src.device import Device, DeviceStatus


class InMemoryDeviceDatabase:
    """
    In-memory database for devices
    """
    def __init__(self):
        """
        Initialize the database
        """
        self._devices = {}

    def get(self, device_id: uuid.UUID) -> Optional[Device]:
        """
        Get a device by its id
        :param device_id: Device id
        :return: Device
        """
        return self._devices.get(device_id, None)

    def add(self, device: Device):
        """
        Add a device to the database
        :param device: New device to add
        :return: None
        """
        self._devices[device.id] = device

    def set_status(self, device_id: uuid.UUID, status: DeviceStatus):
        """
        Set the status of a device
        :param device_id: Device id
        :param status: New status of the device
        :return:
        """
        self._devices[device_id].status = status
