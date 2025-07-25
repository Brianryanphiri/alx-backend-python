from datetime import timedelta

INSTALLED_APPS = [
    # your existing apps...
    'rest_framework',
    'rest_framework_simplejwt',
]

DEBUG = True  # Set True for local development

ALLOWED_HOSTS = ['*']  # Allow all hosts (good for dev, change for production)

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
