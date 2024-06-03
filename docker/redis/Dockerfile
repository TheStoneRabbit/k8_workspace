FROM redis:latest

RUN mkdir /db
WORKDIR /db
ADD . /db/
RUN redis-cli -h localhost -p 6379 < ./import_movies.redis
RUN redis-cli -h localhost -p 6379 < ./import_actors.redis
EXPOSE 6379
CMD [ "redis-server" ]