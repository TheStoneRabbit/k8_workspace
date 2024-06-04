# Kubernetes steps to run:
```
minikube start
eval $(minikube docker-env)
minikube image load k8-masonic-webapp
minikube image load k8-masonic-db
kubectl apply -f kubernetes/namespace.yaml
kubectl apply -f kubernetes/pv.yaml
kubectl apply -f kubernetes/pvc.yaml
kubectl apply -f kubernetes/db-deployment.yaml
kubectl apply -f kubernetes/webapp-deployment.yaml
minikube tunnel
```

# Check commands:

```
kubectl get services -n masonic-app
kubectl describe pods -n masonic-app
```

# Delete

```
minikube stop
minikube delete

```