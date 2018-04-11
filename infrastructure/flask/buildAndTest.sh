sudo docker stop flaskapp
sudo docker rm flaskapp
sudo docker build -t elba-applet:latest .
sudo docker run --name flaskapp -p 5000:5000 -d elba-applet