# word_summary
gives info of given word through wikipedia




### to call microservice
something like this
'''bash
curl -X 'POST' \
  'https://cautious-enigma-7v5795wpx645hrrjg-8082.app.github.dev/wiki' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "name": "Microsoft",
  "sentences": 2
}'
'''

#### build container
'docker build .'
'docker image ls'
### Run container
'docker run -p 127.0.0.1:8082:8082 e128f97604a7'

### Invoke
run 'invoke.sh'
