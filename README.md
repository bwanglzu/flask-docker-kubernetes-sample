#### A test app

Build & Run docker app:
```python
# docker build -t <username>/<appname> .
docker build -t bo/sampleapp:latest .
docker run -d -p 5000:5000 bo/sampleapp
```

Apply k8s secrets:
```python
kubectl apply -f k8s/local/secret.yml
```
