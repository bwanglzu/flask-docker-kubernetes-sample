#### A test app

Build:
```python
# docker build -t <username>/<appname> .
docker build -t bo/sampleapp .
```

Run:
```python
docker run -d -p 5000:5000 bo/sampleapp
```
