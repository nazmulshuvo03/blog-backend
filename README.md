# blog-backend


### Start virtual env
`pipenv shell`

### Install packages
`pipenv install`

### Start Django server
`python manage.py runserver`

### Make new database migrations
`python manage.py makemigrations`

### Migrate database update
`python manage.py migrate`

### Heroku migrations
`heroku run python manage.py makemigrations`

### Heroku database update
`heroku run python manage.py migrate`
### Heroky deployment
`git push heroku master`