import uuid
from typing import Optional, Dict
from alfred_device_manager.domain.device import DeviceStatus, Device
from alfred_device_manager.domain.device_repository import DeviceRepository


class InMemoryDeviceRepository(DeviceRepository):
    """
    In-memory database for devices
    """
    def __init__(self):
        """
        Initialize the database
        """
        self._devices: Dict[uuid.UUID, Device] = {}

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

    def delete(self, device_id: uuid.UUID):
        """
        Delete a device from the database
        :param device_id: Device id
        :return: None
        """
        self._devices.pop(device_id, None)

    def set_status(self, device_id: uuid.UUID, status: DeviceStatus):
        """
        Set the status of a device
        :param device_id: Device id
        :param status: New status of the device
        :return:
        """
        self._devices[device_id].status = status
