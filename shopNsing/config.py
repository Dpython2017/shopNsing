import os
CACHES = {
    "default": {
        "BACKEND": "redis_cache.cache.RedisCache",
        "LOCATION": os.environ.get('REDIS_URL'),
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient"
        }
    }
}
# Public API Config
API_KEY = "4b32cb78da40ba12c2fea537c078ded6"
MUSIXMATCH_URL = "https://api.musixmatch.com/ws/1.1/"
