#!/bin/bash
set -o xtrace
docker build -f docker/python/Dockerfile -t k8-masonic-webapp docker/python/
docker build -f docker/redis/Dockerfile -t k8-masonic-db docker/redis/
kubectl apply -f kubernetes/namespace.yaml
kubectl apply -f kubernetes/pv.yaml
kubectl apply -f kubernetes/pvc.yaml
kubectl apply -f kubernetes/db-deployment.yaml
kubectl apply -f kubernetes/webapp-deployment.yaml
kubectl rollout restart deployment -n masonic-app
docker-compose up -d
set +o xtrace