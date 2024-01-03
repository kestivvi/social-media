# Po klonowaniu wykonujemy w folderze nadrzędnym komendy:

- Przygotowanie środowiska

```python
python -m venv venv_name
venv_name/Scripts/activate
pip install -r requirements.txt
python social-media/manage.py collectstatic
python social-media/manage.py makemigrations
python social-media/manage.py migrate
```

- Uruchomienie serwera

```python
python social-media/manage.py runserver
```
