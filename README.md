# Steps

First make sure you've installed Docker.

```bash
git clone github.com/rgamba/postman-demo
cd postman-demo
docker-compose up 
```

Open http://localhost:5000/ to view the **auth** service dashboard.

Open http://localhost:5001/ to view the **api** service dashboard.

Finally, send a new request to the actual **api** service via HTTP.

```
curl --user user:123 localhost:4000/status
```