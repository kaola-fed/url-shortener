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

## Screenshots

![](https://cloud.githubusercontent.com/assets/2230882/25573918/12e95fc0-2e7c-11e7-9e8c-dde04935b34a.png)
![](https://cloud.githubusercontent.com/assets/2230882/25573917/12e6a938-2e7c-11e7-8c12-eddb6db26a97.png)

## License
MIT