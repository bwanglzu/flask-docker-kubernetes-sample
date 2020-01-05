from python:3.6
MAINTAINER Bo "kingbolanda@live.com"
COPY . /deploy
WORKDIR /deploy
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app/app.py"]
