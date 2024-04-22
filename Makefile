up:
	docker-compose up -d --build

init-db:
	docker-compose exec web aerich init -t app.prepare_database.TORTOISE_ORM && \
	docker-compose exec web aerich init-db

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
