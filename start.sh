echo "*/5 * * * *  blob_reading.py" | crontab -
service cron start
pip install -r requirements.txt && gunicorn --bind=0.0.0.0 --workers=4 main:app

