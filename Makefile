
up:
	cd ./api_consulta && docker-compose up --build -d
	cd ./api_cotacao && docker-compose up --build -d
down:
	cd ./api_consulta && docker-compose down
	cd ./api_cotacao && docker-compose down

api-consulta-down:
	cd ./api_consulta && docker-compose down

api-consulta-up:
	cd ./api_consulta && docker-compose up --build -d

api-cotacao-down:
	cd ./api_cotacao && docker-compose down

api-cotacao-up:
	cd ./api_cotacao && docker-compose up --build -d

api-update:
	cd ./api_consulta && docker-compose down
	cd ./api_cotacao && docker-compose down
	git pull
	cd ./api_consulta && docker-compose up --build -d
	cd ./api_cotacao && docker-compose up --build -d
