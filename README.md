# my_docker_flask

```shell
docker build -t my_docker_flask:latest .
docker images
docker ps
docker run -d -p 5000:5000 my_docker_flask:latest
docker ps
# wait for container to start
sleep 3
curl localhost:5000
curl localhost:5000/ping
curl localhost:5000/healthcheck
#docker kill <container ID>
```

Based on: A simple Docker + Flask tutorial on [Medium](https://medium.com/@mtngt/docker-flask-a-simple-tutorial-bbcb2f4110b5).
