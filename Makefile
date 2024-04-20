run:
	docker-compose up -d --build

stop:
	docker-compose down --volumes

local-run:
	poetry run uvicorn app.main:app --reload --port 8000

lint:
	poetry run ruff format && poetry run ruff check
