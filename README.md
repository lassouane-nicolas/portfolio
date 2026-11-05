# Developer Portfolio

Personal developer portfolio built with **Django** and **Wagtail CMS**.

This project showcases my background, technical skills, and development projects. It also demonstrates the implementation of a content-managed website.

## Tech Stack

- Python
- Django
- Wagtail CMS
- SQLite
- HTML / CSS / JavaScript

## Features

- Responsive design
- CMS-managed pages and projects
- Contact form
- SEO and accessibility considerations
- Wagtail administration interface

## Local Setup

### Prerequisites

- Python 3
- Git

### Installation

Clone the repository:

```bash
git clone git@github-personal:lassouane-nicolas/portfolio.git
cd portfolio
```

Create and activate a virtual environment:

```bash
python3 -m venv env
source env/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create the local environment configuration:

```bash
cp .env.example .env
```

Replace the placeholder secret key in `.env` with a securely generated key:

```bash
python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
```

Load environment variables:

```bash
set -a
source .env
set +a
```

Initialize the database:

```bash
python manage.py migrate
```

Create an administrator account:

```bash
python manage.py createsuperuser
```

Start the development server:

```bash
python manage.py runserver
```

Open http://127.0.0.1:8000/ in your browser.

The Wagtail administration interface is available at http://127.0.0.1:8000/admin/.

## Development Notes

- SQLite is used for local development.
- Environment variables are loaded manually from `.env`.
- Sensitive configuration files, local databases, and virtual environments must not be committed.
- Production deployment is not configured yet.

## Project Status

Under development as part of a CMS certification project at Simplon.
