dist=$1
. venv/bin/activate
export FLASK_APP=app
pip install $dist
sudo systemctl restart gsapi
flask db migrate
flask db upgrade
systemctl status gsapi