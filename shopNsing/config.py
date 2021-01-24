
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient"
        }
    }
}
# Public API Config
API_KEY = "4b32cb78da40ba12c2fea537c078ded6"
MUSIXMATCH_URL = "https://api.musixmatch.com/ws/1.1/"
