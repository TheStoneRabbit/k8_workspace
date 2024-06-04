# k8 Workspace

Very simple redis python Flask application.



## To run:

clone then do the following

`cd docker/python && docker build -f Dockerfile -t k8-masonic-webapp .`

`cd docker/redis && docker build -f Dockerfile -t k8-masonic-db .`

`docker-compose up -d`
