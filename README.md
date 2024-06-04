# k8 Workspace

Very simple redis python Flask application.



## To run:

clone then do the following

`cd docker/python && docker build -f Dockerfile -t k8-masonic-db .`

`cd docker/redis && docker build -f Dockerfile -t redis-example-masonic .`

`docker-compose up -d`
