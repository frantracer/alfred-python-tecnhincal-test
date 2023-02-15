from alfred_device_manager.app import create_app
from alfred_device_manager.infrastructure.in_memory_device_repository import InMemoryDeviceRepository


def main() -> None:
    """
    
    :return:
    """
    device_db = InMemoryDeviceRepository()
    app = create_app(device_db)
    app.run(debug=True)


if __name__ == '__main__':
    main()
