import os
import redis
from flask import Flask

app = Flask(__name__)

redis_host = os.getenv('REDIS_HOST', 'localhost')
redis_port = int(os.getenv('REDIS_PORT', 6379))

r = redis.Redis(host=redis_host, port=redis_port, db=0)

# Function to fetch a record by key
def fetch_record_by_key(key):
    print(f"-> {key}", flush=True)
    field_names = r.hkeys(key)
    field_names_decoded = [field.decode('utf-8') for field in field_names]
    end_values = []
    for x in field_names_decoded:
        value = r.hget(key, x)
        end_values.append(f"{x}: {value.decode('utf-8')}")
    print(f"result: {value}")
    if value:
        return end_values
    else:
        return ""



# Function to fetch 100 records
def fetch_records(start=0, count=100):
    keys = [f'record:{i}' for i in range(start, start + count)]
    records = r.mget(keys)
    return {key.decode('utf-8'): value.decode('utf-8') for key, value in zip(keys, records)}

@app.route("/")
def root_page():
    return "Welcome to the root of the masonic example"

@app.route("/getdata/<param>", methods=['GET'])
def get_data(param: str):
    param = param.replace("-", ":")
    print(f"Getting value for {param}", flush=True)
    return fetch_record_by_key(param)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=5001)
