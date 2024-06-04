FROM python:3.9

COPY  ./* .
RUN pip install -r requirements.txt
ENV REDIS_HOST=my_redis
ENV REDIS_PORT=6379
EXPOSE 5000
CMD ["python", "main.py"]