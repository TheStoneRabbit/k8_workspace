FROM redis:latest

RUN mkdir /db
WORKDIR /db
COPY ./* /db/
RUN chmod +x redis_populate.sh
CMD ["./redis_populate.sh"]
EXPOSE 6379