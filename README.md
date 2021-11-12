# Guppi-backend
Guppi-backend is the back-end code from de app Guppi. This project is associated in my TCC of the university.

![alt-text](prototype.gif)

# Installation
To install this application you will need Python and free Mysql. 

### For Windows
Clone this repo and install the dependencies.

```sh
git clone https://github.com/FelipeMaeda/Guppi-backend.git
cd .\Guppi-backend\
python -m venv .\venv
.\venv\Scripts\activate.bat
pip install -r requirements.txt
```

### For Linux
Clone this repo and install the dependencies.

```sh
git clone https://github.com/FelipeMaeda/Guppi-backend.git
cd ./Guppi-backend
python -m venv ./venv
source ./venv/Scripts/activate
pip install -r requirements.txt
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
python app.py
```
