# Backend

Aceasta este **partea de backend** a aplicației, construită folosind framework-ul **Django**.

## Cerințe

Pentru a rula aplicația, trebuie să ai instalat:

- **Python** (v3.14.3 sau o versiune mai mare)
- **pip** (v25.3 sau o versiune mai mare)

## Instalare

1. Asigură-te că te afli în directorul `backend`

2. Creează un fișier `.env` și adaugă următoarea linie:

```bash
DJANGO_ALLOWED_HOSTS=[DJANGO_ALLOWED_HOSTS]
```

_Note: Înlocuiește conținutul din parantezele pătrate cu valorile corespunzătoare._

### Optional: rularea fără Docker

1. Creează mediul virtual folosind comanda:

```bash
python -m venv .venv
```

2. Activează mediul virtual folosind comanda:

```bash
source ./.venv/bin/activate
```

3. Instalează dependențele folosind comanda:

```bash
pip install -r requirements.txt
```

4. Crează migrațiile folosind comanda:

```bash
python manage.py makemigrations
```

5. Aplică migrațiile folosind comanda:

```bash
python manage.py migrate
```

6.  Rulează proiectul folosind comanda:

```bash
python manage.py runserver
```
