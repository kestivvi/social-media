# Showcase
social-media to szkolny projekt wykonany w celach edukacyjnych. Jest to prosta, prymitywna, ale funkcjonalna aplikacja typu social media. Użytkownicy mogą tworzyć konta i logować się. Mogą tworzyć posty, komentować je oraz lajkować. Użytkownik ma prawo do modyfikacji i usunięcia swoich postów i komentarzy oraz oczywiście może odlajkować poprzedmio polubiony post.

Aplikacja została napisana z pomocą frameworka django. 

https://github.com/kestivvi/social-media/assets/40665452/f3875640-9b6c-4dea-8f9b-f73009cc43a2



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
