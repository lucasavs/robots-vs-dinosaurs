run:
	uvicorn app.main:app --reload

lint:
	black . --check

beautify:
	black .

test:
	python3 -m pytest
