# Kubernetes steps to run:
```
minikube start
eval $(minikube docker-env)
minikube image load k8-masonic-db
minikube image load redis-example-masonic
kubectl apply -f namespace.yaml
kubectl apply -f db-deployment.yaml
kubectl apply -f webapp-deployment.yaml
minikube tunnel
```

# Check commands:

```
kubectl get services -n masonic-app
kubectl describe pods -n masonic-app
```

# Delete and restart

```
minikube stop
minikube delete
minikube start
```