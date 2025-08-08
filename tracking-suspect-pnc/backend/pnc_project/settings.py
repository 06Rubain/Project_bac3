import os # Assurez-vous que 'os' est importé en haut du fichier

# ...

# AJOUTEZ CES APPLICATIONS À LA LISTE INSTALLED_APPS
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Applications tierces
    'rest_framework',
    'corsheaders',
    'pgvector',

    # Nos applications
    'api',
]

# AJOUTEZ LE MIDDLEWARE CORS (juste avant CommonMiddleware)
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    # ...
    'corsheaders.middleware.CorsMiddleware', # Ajouter cette ligne
    'django.middleware.common.CommonMiddleware',
    # ...
]

# DÉFINISSEZ LES ORIGINES AUTORISÉES (pour que React puisse communiquer avec l'API)
# Pour le développement, nous pouvons être permissifs.
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000", # L'adresse par défaut de React
    "http://127.0.0.1:3000",
]


# MODIFIEZ LA CONFIGURATION DE LA BASE DE DONNÉES
# Remplacez la configuration SQLite existante par celle-ci
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('POSTGRES_NAME'),
        'USER': os.environ.get('POSTGRES_USER'),
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD'),
        'HOST': os.environ.get('POSTGRES_HOST'),
        'PORT': '5432',
    }
}

# ... (le reste du fichier)