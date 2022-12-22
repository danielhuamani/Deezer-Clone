build:
	docker-compose -f ./docker/docker-compose.yml build 
run:
	docker-compose -f ./docker/docker-compose.yml up 
migrate:
	docker-compose -f ./docker/docker-compose.yml exec silabuz python ./src/manage.py migrate 
migrations:
	docker-compose -f ./docker/docker-compose.yml exec silabuz python ./src/manage.py 
pytest:
	# FUNCTION="unit/apps/test_product.py"
	# FUNCTION="./src/"
	# PARAMS="-rm"
	docker-compose -f ./docker/docker-compose.yml run silabuz pytest ./src/tests/${FUNCTION} ${PARAMS}