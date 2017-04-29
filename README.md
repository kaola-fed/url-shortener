# url-shortener
URL Shortener

## How to run

### basic
 - `docker build -t url-shortener:latest .`
 - `docker run -d -p 5000:5000 url-shortener <URL_USER>`

### docker-compose
 - `echo 'URL_USER=<URL_USER>' > .env`
 - `docker-compose build`
 - `docker-compose up -d`

## License
MIT