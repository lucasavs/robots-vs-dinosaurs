run:
	uvicorn main:app --reload

lint:
	black . --check

test:
	@echo "TODO"