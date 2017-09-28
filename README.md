# Steps

First make sure you've installed [Docker](https://www.docker.com/).

Then, [create a Docker Hub account](https://hub.docker.com/) if you don't have one already.

Login to Docker Hub:

```bash
docker login
```

Then

```bash
git clone https://github.com/rgamba/postman-demo
cd postman-demo
docker-compose up 
```

Open http://localhost:5000/ to view the **auth** service dashboard.

Open http://localhost:5001/ to view the **api** service dashboard.

Finally, send a new request to the actual **api** service via HTTP.

```
curl --user user:123 localhost:4000/status
```