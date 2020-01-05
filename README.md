A minimum example of using k8s to deploy a flask web application.

Apply k8s secrets:
```python
kubectl apply -f k8s/local/secret.yml
kubectl apply -f k8s/local/configmap.yml
kubectl apply -f k8s/deployment.yml
kubectl apply -f k8s/service.yml
```

working in progress:
1. healthcheck with liveness and readness probe.
2. yml management with [kustomize](https://github.com/kubernetes-sigs/kustomize)