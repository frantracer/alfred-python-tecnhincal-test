import enum
import uuid
from dataclasses import dataclass


class DeviceType(enum.Enum):
    """
    Type of devices
    """
    LIGHT = "LIGHT"
    SENSOR = "SENSOR"
    SWITCH = "SWITCH"


class DeviceStatus(enum.Enum):
    """
    Possible statuses of devices
    """
    ON = "ON"
    OFF = "OFF"


@dataclass
class Device:
    """
    Information about a device
    """
    id: uuid.UUID
    device_type: DeviceType
    status: DeviceStatus
