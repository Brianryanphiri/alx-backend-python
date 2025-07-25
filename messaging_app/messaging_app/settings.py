from datetime import timedelta

INSTALLED_APPS = [
    # Default Django apps required for auth and admin
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',   # required for auth models
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Third-party apps
    'rest_framework',
    'rest_framework_simplejwt',

    # Your apps here
    # 'messaging_app.chats',
]

DEBUG = True  # Set True for local development

ALLOWED_HOSTS = ['*']  # Allow all hosts (good for dev, restrict in production)

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=30),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'AUTH_HEADER_TYPES': ('Bearer',),
}
