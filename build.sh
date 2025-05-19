set -o errexit

pip install -r requirements.txt

export DATABASE_PATH=/opt/render/project/src/db/db.sqlite3

python manage.py collectstatic --no-input

python manage.py makemigrations

python manage.py migrate