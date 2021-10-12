# Guppy-backend
 Backend of app Guppy.

# Init DB in Windows Env
python .\app.py db init
python .\app.py db migrate
python .\app.py db upgrade

# Init DB in Linux Env
flask db init
flask db migrate
flask db upgrade