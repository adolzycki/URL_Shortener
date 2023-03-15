DOCKER_COMPOSE=docker-compose

default: docker-run

down:
	${DOCKER_COMPOSE} down

destroy:
	${DOCKER_COMPOSE} down -v --remove-orphans

makemigrations:
	${DOCKER_COMPOSE} run --rm backend python manage.py makemigrations

makemigrations-merge:
	${DOCKER_COMPOSE} run --rm backend python manage.py makemigrations --merge

migrate:
	${DOCKER_COMPOSE} run --rm backend python manage.py migrate

cli:
	${DOCKER_COMPOSE} run --rm backend bash

shell:
	${DOCKER_COMPOSE} run --rm  backend python manage.py shell

docker-build:
	${DOCKER_COMPOSE} build

docker-rebuild: docker-purge-images docker-build

docker-run:
	${DOCKER_COMPOSE} up -d

docker-logs:
	${DOCKER_COMPOSE} logs -tf
