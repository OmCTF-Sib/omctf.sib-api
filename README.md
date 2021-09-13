# OmCTF.Sib - API

## Preparation for production
###Add your domain in production.yml
```bash
- traefik.http.routers.nginx.rule=Host(`example.com`)
```

### Set Up .env
Example:
```bash
SECRET_KEY=secret
DEBUG=True

POSTGRES_HOST=psql
POSTGRES_PORT=5432
POSTGRES_DB=sibctf
POSTGRES_USER=sibctf
POSTGRES_PASSWORD=sibctf
```

### Up docker-compose
```bash
docker-compose -f production.yml up --build
```

### Create superuser
```bash
docker-compose -f production.yml -it ctf_django python manage.py createsuperuser
```
