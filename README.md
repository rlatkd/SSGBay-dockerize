## How to dockerize

./client/Dockerfile-react

./server/Dockerfile-flask

./server/Dockerfile-mysql

./server/init.sql

docker network create mynetwork

docker image build -t react -f Dockerfile-react .
docker image build -t flask -f Dockerfile-flask .
docker image build -t mysql -f Dockerfile-mysql .

docker container run -d --network mynetwork --name mysql mysql
docker container run -d -p 5000:5000 --network mynetwork --name flask flask
docker container run -d -p 3000:80 --network mynetwork --name react react
