git clone https://github.com/njha7/elbalang_orchestration
cd elbalang_orchestration/infrastructure/rabbitmq
gsutil cp gs://elba-project/config/.env ./
sudo iptables -w -A INPUT -p tcp --dport 4369 -j ACCEPT
sudo iptables -w -A INPUT -p tcp --dport 5671 -j ACCEPT
sudo iptables -w -A INPUT -p tcp --dport 5672 -j ACCEPT
sudo iptables -w -A INPUT -p tcp --dport 25672 -j ACCEPT
docker run docker/compose:1.19.0 version 
docker run \
    -v /var/run/docker.sock:/var/run/docker.sock \
    -v "$PWD:/rootfs/$PWD" \
    -w="/rootfs/$PWD" \
    docker/compose:1.19.0 up