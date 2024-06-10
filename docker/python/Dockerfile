FROM python:3.9

COPY  . .
RUN mkdir -p /templates
COPY templates/ /templates
RUN pip install -r requirements.txt
ENV REDIS_HOST=my-redis
ENV REDIS_PORT=6379
EXPOSE 5000
CMD ["python", "main.py"]