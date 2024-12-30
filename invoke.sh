curl -X 'POST' \
  'http://0.0.0.0:8082/wiki' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "name": "Microsoft",
  "sentences": 2
}'