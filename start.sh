#!/bin/bash
set -o xtrace
minikube start
eval $(minikube docker-env)
minikube image load k8-masonic-db
minikube image load redis-example-masonic
kubectl apply -f kubernetes/pv.yaml
kubectl apply -f kubernetes/pvc.yaml
kubectl apply -f kubernetes/namespace.yaml
kubectl apply -f kubernetes/db-deployment.yaml
kubectl apply -f kubernetes/webapp-deployment.yaml
minikube tunnel
set +o xtrace