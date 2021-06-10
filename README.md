## Forecast
Forecast service built on top of Flask

## Docker usage
To build docker image:
```bash
docker build -t forecast:latest .
```
To run forecast image standalone:
```bash
docker run --name forecast -d -p 8000:5000 --rm forecast:latest
```
Create mysql container:
```bash
docker run --name mysql -d -e MYSQL_RANDOM_ROOT_PASSWORD=yes \
    -e MYSQL_DATABASE=forecast -e MYSQL_USER=forecast \
    -e MYSQL_PASSWORD=password \
    mysql/mysql-server:5.7
```

Start mysql container:
```bash
docker start mysql
```

To run forecast image:
```bash
docker run --name forecast -d -p 8000:5000 --rm -e SECRET_KEY=my-secret-key \
    --link mysql:dbserver \
    -e DATABASE_URL=mysql+pymysql://forecast:password@dbserver/forecast \
    forecast:latest
```



## Usage example

This example uses HTTPie library for HTTP requests.

First, you need to register a new user:
```bash
http POST http://localhost:8000/api/users username=alice password=dog email=alice@example.com
```
Then, grab the authentication token:
```bash
http --auth alice:dog POST http://localhost:8000/api/tokens
```

This example shows how to get current temperature in Moscow in Celsius units. \
For Fahrenheit consider to use F in the unit parameter.
```bash
http GET "localhost:8000/api/weather?cityname=Moscow&unit=C" "Authorization:Bearer <your token>"
```

## PS: Token expired
