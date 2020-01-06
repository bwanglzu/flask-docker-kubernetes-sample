A minimum example of using k8s to deploy a flask web application.

Build docker image:

```
docker build -t bo/sampleapp:latest .
```

Apply k8s configurations:
```
kubectl apply -f k8s/local/secret.yml
kubectl apply -f k8s/local/configmap.yml
kubectl apply -f k8s/deployment.yml
kubectl apply -f k8s/service.yml
```

Debug the app:
```
kubectl get pods # get pods id
kubectl describe pod sampleapp-56dcc478cb-qrnmx 
kubectl logs sampleapp-56dcc478cb-qrnmx # get logs
kubectl --context=minikube port-forward sampleapp-56dcc478cb-qrnmx 5001:5000
```

working in progress:
1. healthcheck with liveness and readness probe.
2. yml management with [kustomize](https://github.com/kubernetes-sigs/kustomize)
3. machine learning life cycle management with [kubeflow](https://github.com/kubeflow/kubeflow)