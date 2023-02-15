import enum
import uuid
from dataclasses import dataclass
from typing import Dict


class DeviceType(enum.Enum):
    """
    Type of devices
    """
    LIGHT_MODBUS = "LIGHT_MODBUS"
    SWITCH_ZWAVE = "SWITCH_ZWAVE"


class DeviceStatus(enum.Enum):
    """
    Possible statuses of devices
    """
    ON = "ON"
    OFF = "OFF"


class DeviceCommand(enum.Enum):
    """
    Possible commands for devices
    """
    TURN_ON = "TURN_ON"
    TURN_OFF = "TURN_OFF"


@dataclass
class Device:
    """
    Information about a device
    """
    id: uuid.UUID
    device_type: DeviceType
    status: DeviceStatus
    additional_info: Dict[str, str]

    def execute_command(self, command: DeviceCommand):
        """
        Execute a command
        :param command: Command to execute
        :return: None
        """
        raise NotImplementedError()
