curl -X POST -H "Content-Type: application/json" -d '{"query": "{ client(id: \"1\") { name age documents { type number } relatives { name relationType } } }"}' http://localhost:8080
curl -X POST -H "Content-Type: application/json" -d '{"query": "{ client(id: \"2\") { name age documents { type number } relatives { name relationType } } }"}' http://localhost:8080
curl -X POST -H "Content-Type: application/json" -d '{"query": "{ client(id: \"2\") { name age } }"}' http://localhost:8080
curl -X POST -H "Content-Type: application/json" -d '{"query": "{ client(id: \"1\") { name age relatives { name relationType } } }"}' http://localhost:8080
curl -X POST -H "Content-Type: application/json" -d '{"query": "{ client(id: \"1\") { name age documents { type number } } }"}' http://localhost:8080
curl -X POST -H "Content-Type: application/json" -d '{"query": "{ client(id: \"1\") { name age documents { number } } }"}' http://localhost:8080
curl -X POST -H "Content-Type: application/json" -d '{"query": "{ client(id: \"1\") { name age relatives { name } } }"}' http://localhost:8080
