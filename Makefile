.PHONY: build
build:
	docker-compose build

.PHONY: up
up:
	docker-compose up -d

.PHONY: down
down:
	docker-compose down --remove-orphans

.PHONY: migrate
migrate:
	docker exec -i api bash -c "python manage.py makemigrations client"
	docker exec -i api bash -c "python manage.py migrate"
	docker-compose restart customers

.PHONY: createsuperuser
createsuperuser:
	docker exec -it api python manage.py createsuperuser