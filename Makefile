setup:
	python3 -m venv venv
	./venv/bin/pip3 install -r requirements.txt

run:
	./venv/bin/python3 -m alfred_device_manager

test:
	./venv/bin/pytest tests/

lint:
	./venv/bin/pylint --rcfile .pylintrc alfred_device_manager tests
	./venv/bin/mypy alfred_device_manager tests
