#!/bin/bash
set -o xtrace
# minikube start
docker build -f docker/python/Dockerfile -t k8-masonic-webapp docker/python/
docker build -f docker/redis/Dockerfile -t k8-masonic-db docker/redis/
# eval $(minikube docker-env)
# minikube image load k8-masonic-webapp
# minikube image load k8-masonic-db
kubectl apply -f kubernetes/namespace.yaml
kubectl apply -f kubernetes/pv.yaml
kubectl apply -f kubernetes/pvc.yaml
kubectl apply -f kubernetes/db-deployment.yaml
kubectl apply -f kubernetes/webapp-deployment.yaml
# minikube tunnel
# minikube stop
# minikube delete
set +o xtrace