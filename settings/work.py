from backend_imatpro_system.settings import *


env_work = environ.Env(
    # set casting, default value
    DEBUG=(bool, True)
)

environ.Env.read_env(os.path.join(BASE_DIR, 'config/app/.env.config.app.work'), overwrite=True)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env_work('DEBUG')

ALLOWED_HOSTS = env_work("DJANGO_ALLOWED_HOSTS").split(" ")

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': env_work('POSTGRESQL_NAME'),
        'USER': env_work('POSTGRESQL_USER'),
        'PASSWORD': env_work('POSTGRESQL_PASS'),
        'HOST': env_work('POSTGRESQL_HOST'),
        'PORT': env_work('POSTGRESQL_PORT'),
    }
}

