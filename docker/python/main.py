import os
import redis
from flask import Flask
from flask import request

app = Flask(__name__)

redis_host = os.getenv('REDIS_HOST', 'localhost')
redis_port = int(os.getenv('REDIS_PORT', 6379))

r = redis.Redis(host=redis_host, port=redis_port, db=0)

# Function to fetch a record by key
def fetch_record_by_key(key):
    print(f"-> {key}", flush=True)
    field_names = r.hkeys(key)
    field_names_decoded = [field.decode('utf-8') for field in field_names]
    end_values = {}
    for x in field_names_decoded:
        value = r.hget(key, x)
        end_values[x] = value.decode('utf-8')
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

# test using: curl -X POST localhost:8000/set-data -H "Content-Type: application/json" -d '{"key": "mason:1", "values": { "date_of_birth": "07/18/2000","first_name": "Mason","middle_name": "Wynn", "last_name": "Lapine","gender": "male"}}'

@app.route("/set-data", methods=['POST'])
def set_data():
    data = request.get_json()
    try:
        r.hmset(data["key"], data["values"])
        r.save()
        print(f"Received data with key: {data['key']}", flush=True)
        return "Data received and loaded successfully"
    except:
        return "Error loading data"

@app.route("/")
def root_page():
    test_curl = "curl -X POST localhost:8000/set-data -H \"Content-Type: application/json\" -d '{\"key\": \"mason:1\", \"values\": { \"date_of_birth\": \"07/18/2000\",\"first_name\": \"Mason\",\"middle_name\": \"Wynn\", \"last_name\": \"Lapine\",\"gender\": \"male\"}}'"
    return f"Welcome to the root of the masonic k8 test suite.<br>  To get started you can query movies and actors by going to localhost:8000/get-data/actor:(some number) or localhost:8000/get-data/movie:(some number<br> To add records, direct your post requests to localhost:8000/set-data.<br>  Here is a test CURL Command: {test_curl}"

@app.route("/get-data/<param>", methods=['GET'])
def get_data(param: str):
    param = param.replace("-", ":")
    print(f"Getting value for {param}", flush=True)
    return fetch_record_by_key(param)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=5001)
