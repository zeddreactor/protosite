#### Simple nginx/django testing application

##### Development:

[Testing from Nginx]

Run website (static + dynamic) on localhost as specified in nginx.conf files

```sh
sudo nginx -t
sudo nginx -s reload
uwsgi --socket :8001 -b 10000 --module protosite.wsgi
```

> will run on localhost: <br>
-localhost/ff/ <br>
-localhost/js/main.js <br>
-localhost/index.html <br>
-localhost/

> uwsgi_params file is necessary

>currently reading from nginx.conf, not protosite_nginx.conf

[Testing from Django]

from web/protosite dir:

```sh
python manage.py collectstatic
# this will get files from STATICFILES_DIRS and put them in STATIC_ROOT, then serve when accessing STATIC_URL as the path

python manage.py runserver
```

> Will run on localhost:8000/ <br>
-localhost:8000/static/index.html <br>
-localhost:8000/static/js/main.js <br>
-localhost:8000/ff

> So, can run at same time as the nginx server
