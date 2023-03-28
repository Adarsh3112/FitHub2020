# Fithub

Pre-requisite - 
- Python
- Django
- JavaScript
- HTML
- CSS
- db.sqlite

This is a Website for Fitness club/gym, where user can subscribe for tips and tricks to improve your fitness. 

## Run website on local desktop
- Clone the repository :-  ` git clone https://github.com/Nikhil26112/Fithub.git `
- Open project folder in terminal :- `pip install -r requirement.txt`
- Migrate changes :- `python manage.py migrate`
- Run the website :- 
``` 
python manage.py runserver 
# if you want to run on specific port (for e.g. 6000 port)
python manage.py runserver 0.0.0.0/6000
```

## Run using Docker

```
docker pull nikhil2611/fithub:latest
docker run -p 8000 -d nikhil2611/fithub
```


