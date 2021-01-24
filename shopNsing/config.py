import os
CACHES = {
    "default": {
        "BACKEND": "redis_cache.RedisCache",
        "LOCATION": "{host}:{port}".format(host='ec2-54-224-171-77.compute-1.amazonaws.com',
                                           port='23109'),
    }
}
# Public API Config
API_KEY = "4b32cb78da40ba12c2fea537c078ded6"
MUSIXMATCH_URL = "https://api.musixmatch.com/ws/1.1/"
