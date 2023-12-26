all: fix lint build-dev build-prod up-dev up-prod down-dev down-prod prune

SRC = src/test_django/
TESTS = tests/

fix:
	poetry run autoflake -r --remove-all-unused-imports --remove-unused-variables --remove-unused-variables --in-place ${SRC}	
	poetry run black ${SRC}
	poetry run isort ${SRC}
	poetry run toml-sort --in-place pyproject.toml

lint:
	poetry run flake8 --exclude __init__.py ${SRC}
	poetry run mypy ${SRC}	

build-dev:
	docker compose -f docker-compose.dev.yaml --env-file .env.dev build

build-prod:
	docker compose -f docker-compose.prod.yaml --env-file .env.prod build

build-up-dev:
	docker compose -f docker-compose.dev.yaml --env-file .env.dev up --build

build-up-prod:
	docker compose -f docker-compose.prod.yaml --env-file .env.prod up --build

down-dev:
	docker compose -f docker-compose.dev.yaml --env-file .env.dev down

down-prod:
	docker compose -f docker-compose.prod.yaml --env-file .env.prod down

prune:
	docker container prune -f
	docker volume prune -f
	docker volume rm test_django_cache_data
	docker volume rm test_django_db_data

migrate:
	docker compose -f docker-compose.dev.yaml --env-file .env.dev \
		run app python3 src/test_django/manage.py makemigrations -n $(NAME) src
	docker compose -f docker-compose.dev.yaml --env-file .env.dev \
		run app python3 src/test_django/manage.py migrate
	docker compose -f docker-compose.dev.yaml --env-file .env.dev down
	docker container prune -f
	docker volume rm test_django_cache_data
	docker volume rm test_django_db_data



	