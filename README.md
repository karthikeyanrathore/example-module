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

## Sample API calls

1. products in inventory
```cURL
curl --request GET \
  --url 'http://0.0.0.0:80/v1/products?offset=3&limit=2'
```

2. order products
```cURL
curl --request POST \
  --url http://0.0.0.0:9000/v1/order \
  --header 'Content-Type: application/json' \
  --data '{
	"items": [
		{
			"productId": "65b76c98263d7bafcae46778",
			"boughtQuantity": 2
		},
		{
			"productId": "65b76c98263d7bafcae46778",
			"boughtQuantity": 2
		}
		],
	"user_address":{
		"city": "delhi",
		"country": "IN",
		"zipcode": 112122
	}
}'
```
