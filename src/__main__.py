from src.app import create_app
from src.database import InMemoryDeviceDatabase


def main() -> None:
    device_db = InMemoryDeviceDatabase()
    app = create_app(device_db)
    app.run(debug=True)


if __name__ == '__main__':
    main()
