## example-module

## How to run the module?

0. prerequisite: Docker/ Docker Compose version v2.24.0

If you face any issue please write me karthikerathore@gmail.com

1. run services
```bash
docker-compose -f docker-compose-develop.yml down -v --remove-orphans; \
docker-compose -f docker-compose-develop.yml build; \
docker-compose -f docker-compose-develop.yml up
```

2. clean up.
```bash
docker-compose -f docker-compose-develop.yml down -v --remove-orphans;
```

vim  set tabstop=2
