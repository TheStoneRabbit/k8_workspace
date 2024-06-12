# k8 Workspace

Very simple redis python Flask application.

The app runs on localhost:8000


## To Run:

`./deploy.sh`

This utilizes docker-desktop to run everything (using `kubectl`).  All of the images get rebuilt upon running this command without caching to ensure all updates to the images are shown in the running containers.

## Argo Monitoring

To monitor changes with Argo use the following commands to access the webapp:

```bash
kubectl create namespace argocd
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml
kubectl port-forward svc/argocd-server -n argocd 8080:443
```

If you are running this for the first time, you may need to access the webapp with a default password (that you should change once you log in).  To access that password, use this command:

```bash
kubectl get secret argocd-initial-admin-secret -n argocd -o jsonpath=“{.data.password}” | base64 —decode
```