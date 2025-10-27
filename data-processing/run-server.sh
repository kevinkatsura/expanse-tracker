
# Create a temporary network
docker network inspect test-net >/dev/null 2>&1 || docker network create test-net

docker run -d \
  --name mysql-db \
  --network test-net \
  -e MYSQL_ROOT_PASSWORD=rootpass \
  -e MYSQL_DATABASE=employee \
  -v ./mysql/init.sql:/docker-entrypoint-initdb.d/init.sql:ro \
  -p 3306:3306 \
  mysql:8.0

# wait to server well running
sleep 10

# docker-compose up -d --build
docker exec -it mysql-db mysql -u root -prootpass -e "USE employee; SELECT * FROM employees;"
