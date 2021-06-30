
up:
	cd ./api_calculo && docker-compose -f up --build -d
	cd ./api_consulta && docker-compose -f up --build -d
down:
	cd ./api_calculo && docker-compose down
	cd ./api_consulta && docker-compose down
