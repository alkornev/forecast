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
Run containers:
```bash
docker-compose up
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
