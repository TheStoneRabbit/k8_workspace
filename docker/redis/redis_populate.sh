#!/bin/sh

# Start Redis server in the background
redis-server --appendonly yes &

# Wait for Redis server to start
sleep 5

# Import data from .redisfile
redis-cli < import_actors.redis
redis-cli < import_movies.redis

# Keep the container running
tail -f /dev/null