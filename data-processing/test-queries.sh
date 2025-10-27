docker run --rm \
  -v ./src/test_script.py:/app/test_script.py \
  -e MYSQL_HOST=mysql-db \
  -e MYSQL_USER=root \
  -e MYSQL_PASSWORD=rootpass \
  -e MYSQL_DATABASE=employee \
  --network test-net \
  python:3.12-slim \
  bash -c "pip install --no-cache-dir mysql-connector-python && chmod +x /app/test_script.py && python /app/test_script.py"
