#!bin/bash
cd /data/www/ && /usr/local/bin/gunicorn --log-file /data/www/backend/logs/gunicorn.log --access-logfile - --daemon --timeout 600 --workers 1 --bind unix:/data/service/backend.sock backend.wsgi:app && nginx -g 'daemon off;'
