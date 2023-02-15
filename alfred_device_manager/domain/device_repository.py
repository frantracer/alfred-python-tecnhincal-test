import uuid
from abc import ABC, abstractmethod
from typing import Optional

from alfred_device_manager.domain.device import Device, DeviceStatus


class DeviceRepository(ABC):
    """
    Abstract class for device repositories
    """
    @abstractmethod
    def get(self, device_id: uuid.UUID) -> Optional[Device]:
        raise NotImplementedError()

    @abstractmethod
    def add(self, device: Device):
        raise NotImplementedError()

    @abstractmethod
    def set_status(self, device_id: uuid.UUID, status: DeviceStatus):
        raise NotImplementedError()
