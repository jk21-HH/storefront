# Storefront

A Django REST Framework backend for an e-commerce storefront, providing APIs for products, collections, carts, and tagging.

## Apps

- **store** — core e-commerce models: products, collections, carts, customers, orders (filtering, search, ordering, and pagination supported)
- **tags** — generic tagging for store objects
- **store_custom** — custom extensions to the store app
- **likes** — like/favorite functionality
- **playground** — scratch app for experimentation

## Requirements

- Python 3.14
- PostgreSQL (via `psycopg2-binary`)

## Setup

```bash
pipenv install
cp storefront/settings.example.py storefront/settings.py  # if present
cp .env.example .env
```

Update `.env` / `settings.py` with your database credentials, then run:

```bash
pipenv run python manage.py migrate
pipenv run python manage.py createsuperuser
pipenv run python manage.py runserver
```

## Tech Stack

- Django
- Django REST Framework
- drf-nested-routers
- django-filter
- django-debug-toolbar

## Admin

Django admin is available at `/admin/` for managing store, tags, and store_custom data.
