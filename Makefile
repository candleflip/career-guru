up:
	docker-compose up -d --build

down:
	docker-compose down --volumes

local-up:
	poetry run uvicorn app.main:app --reload --port 8000

lint:
	poetry run ruff format && poetry run ruff check

lint-fix:
	poetry run ruff format && poetry run ruff check --fix

type:
	poetry run mypy . --strict
