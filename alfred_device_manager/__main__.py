from alfred_device_manager.app import create_app
from alfred_device_manager.infrastructure.database import InMemoryDeviceDatabase


def main() -> None:
    """
    
    :return:
    """
    device_db = InMemoryDeviceDatabase()
    app = create_app(device_db)
    app.run(debug=True)


if __name__ == '__main__':
    main()
