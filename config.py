import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'nekii-klyuch-na-vsyakii-sluchai'
    CACHE_TYPE = 'memcached'
    CACHE_DEFAULT_TIMEOUT = 300
    CACHE_MEMCACHED_SERVERS = os.environ.get('MEMCACHED_SERVERS') or ['127.0.0.1:12512',]