# Dockerising-Flask-application
## steps:
- docker login
- docker build --tag docker_flask_image .
- docker run -d -p 8080:8080 docker_flask_image
