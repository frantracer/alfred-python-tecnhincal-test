from dataclasses import dataclass

from alfred_device_manager.domain.device import Device, DeviceCommand


@dataclass
class ModbusLight(Device):
    """
    Modbus light device integration
    """
    address: int

    def execute_command(self, command: DeviceCommand):
        if command == DeviceCommand.TURN_ON:
            print(f"Sending 1 to modbus address {self.address}")
        elif command == DeviceCommand.TURN_OFF:
            print(f"Sending 0 to modbus address {self.address}")
