import os
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": os.environ.get('REDIS_URL'),
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient"
        }
    }
}
# Public API Config
API_KEY = os.environ.get('API_KEY')
MUSIXMATCH_URL = "https://api.musixmatch.com/ws/1.1/"
