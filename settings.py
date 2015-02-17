import os
import pylibmc

# Memcached
mc_servers = os.environ.get('MEMCACHIER_SERVERS', '').split(',')
mc_user = os.environ.get('MEMCACHIER_USERNAME', '')
mc_pass = os.environ.get('MEMCACHIER_PASSWORD', '')
on_heroku = 'DYNO' in os.environ

if on_heroku:
    memcache = pylibmc.Client(mc_servers, binary=True,
                              username=mc_user,
                              password=mc_pass,
                              behaviors={
                                  'tcp_nodelay': True,
                                  'ketama': True,
                                  'no_block': True,
                              })
else:
    memcache = pylibmc.Client(['localhost:11211'])
