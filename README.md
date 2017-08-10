# Block Explorer Test Features

Test repository for new Block Explorer features

## Getting Started

For this project you will need python 2.7 or greater, pip, NodeJS and Angular cli

## For Debian/Ubuntu based distros

```
sudo apt-get install python-pip
npm install -g @angular/cli
curl -sL https://deb.nodesource.com/setup_8.x | sudo -E bash -
sudo apt-get install -y nodejs
```

After installing pip you will need to install dependencies for this project

```
pip install flask
pip install flask_socketio
```

## Running the project
Go to downloaded repository
### Example
```
cd Downloads/PythonFlask-WebSocket-Server-master
```
Run next three commands:
```
python rest-server.py
python app.py
cd angular-test && npm install
ng serve
```
### If no errors are shown flask server is running on
```
http://localhost:5004
```
### And angular on
```
http://localhost:9898
```
