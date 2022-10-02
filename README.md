

# Employee managment Api
Install requirements first
```sh
pip install -m requirements.txt
```

Run server
```sh
python manage.py runserver
```
Server will be running on this url adn you can see Api Root for main endpoint on app
```sh
localhost:8000
```
Swagger is on 
```sh
localhost:8000/swagger
```
Run tests 
```sh
python manage.py test
```

See the test report
```sh
coverage run -m ./manage.py test
coverage report -m 
or
coverage html
```