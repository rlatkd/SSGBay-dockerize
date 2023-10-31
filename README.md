## How to dockerize

./client/Dockerfile-react

./server/Dockerfile-flask

./server/Dockerfile-mysql

./server/init.sql

docker network create mynetwork

docker image build -t myreact -f Dockerfile-react .
docker image build -t myflask -f Dockerfile-flask .
docker image build -t mymysql -f Dockerfile-mysql .

docker container run -d --network mynetwork --name mysql mymysql
docker container run -d -p 5000:5000 --network mynetwork --name flask myflask
docker container run -d -p 3000:80 --network mynetwork --name react myreact
