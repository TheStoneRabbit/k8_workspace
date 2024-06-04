#!/bin/sh

# Copy initialization files to /data
cp /db/import_actors.redis /data/
cp /db/import_movies.redis /data/

# Start Redis server with AOF enabled in the background
redis-server --appendonly yes --dir /data &

# Wait for Redis server to start
sleep 5

# Import data from .redis files
redis-cli < /data/import_actors.redis
redis-cli < /data/import_movies.redis

# Keep the container running
wait