from dataclasses import dataclass, field

from alfred_device_manager.domain.device import Device, DeviceCommand, DeviceType


@dataclass
class ModbusLight(Device):
    """
    Modbus light device integration
    """
    address: int = field(init=False)

    def __post_init__(self):
        try:
            self.address = int(self.additional_info["address"])
        except KeyError as exception:
            raise ValueError("Missing address in additional_info") from exception
        except ValueError as exception:
            raise ValueError("Invalid address in additional_info") from exception

        if self.device_type != DeviceType.LIGHT_MODBUS:
            raise ValueError("Invalid device type")

    def execute_command(self, command: DeviceCommand):
        if command == DeviceCommand.TURN_ON:
            print(f"Sending 1 to modbus address {self.address}")
        elif command == DeviceCommand.TURN_OFF:
            print(f"Sending 0 to modbus address {self.address}")
