# Guppi-backend
Guppi-backend is the back-end code from de app Guppi. This project is associated in my TCC of the university.

![alt-text](prototype.gif)

# Installation
To install this application you will need **Python 3.9** and free Mysql. 

# Docker
Execute this command in your server do build a image from this app.

```sh
git clone https://github.com/FelipeMaeda/Guppi-backend.git
cd .\Guppi-back-end\
docker image build -e SQLALCHEMY_DATABASE_URI='mysql://User:Password@uri_server.com:3306/database' -t guppi:1.0.0 .
```

### For Linux
Clone this repo and install the dependencies.

```sh
git clone https://github.com/FelipeMaeda/Guppi-backend.git
cd ./Guppi-back-end
python3 -m venv ./venv
source ./venv/bin/activate
pip3 install -r requirements.txt
export SQLALCHEMY_DATABASE_URI='mysql://User:Password@uri_server.com:3306/database'
```

### For Windows
Clone this repo and install the dependencies.

```sh
git clone https://github.com/FelipeMaeda/Guppi-backend.git
cd .\Guppi-back-end\
python -m venv .\venv
.\venv\Scripts\activate.bat
pip install -r requirements.txt
SET SQLALCHEMY_DATABASE_URI='mysql://User:Password@uri_server.com:3306/database'
```

# Usage

### Configuration
To run this app, you need to change credentials and configs in the file "app/config.py". The next step is create a database in your MySQL with the name you have configured.

### Init DB for the App

```sh
flask db init
flask db migrate
flask db upgrade
```

### Start the server

```sh
python app.py
```

or

```sh
./app.py
```
