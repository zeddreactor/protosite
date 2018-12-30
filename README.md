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



[Using nginx with the config file in protosite dir]

First, need to kill our existing nginx processes started with old config:

```sh
brew services stop nginx  # might not do anything? check up on it
sudo nginx -s stop
```

Start nginx with the config file in our protosite nginx config folder:

```sh
sudo nginx -c ~/Desktop/repos/web/nginx/protosite_nginx.conf

# restart uwsgi to listen on the port we set in protosite_nginx.conf:
sudo uwsgi --socket :8002 -b 10000 --module protosite.wsgi
```

Static & dynamic files will now serve on localhost

> localhost/ff <br>
> localhost/ <br>
> localhost/index.html


Now, can update & test nginx config as such:

```sh
sudo nginx -t -c ~/Desktop/repos/web/nginx/protosite_nginx.conf
sudo nginx -s reload -c ~/Desktop/repos/web/nginx/protosite_nginx.conf
```


#### Debug

[Nginx logs]

`cat /usr/local/var/log/nginx/error.log`

[Bad gateway error for dynamic files]

Static files will be served as long as nginx daemon is running; however dynamic files from django need the uwsgi daemon to run. Try start:

```sh
sudo uwsgi --socket :8002 -b 10000 --module protosite.wsgi
```

or if not working, check that nginx service is using the correct config in log (above). <br>
If not, restart:

```sh
sudo nginx -s stop
sudo nginx -c ~/Desktop/repos/web/nginx/protosite_nginx.conf
```

[Which port is used?]

```sh
netstat -p tcp
lsof -i :8002
kill [PID]

ps ax | grep nginx
```
