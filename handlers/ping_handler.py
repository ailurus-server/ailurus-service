import logging

from tornado.web import RequestHandler
from tornado.escape import json_decode

from settings import memcache

class PingHandler(RequestHandler):
    EXPIRY = 60  # seconds

    def MemcacheKey(self, ext_ip):
        return 'ip_map_' + ext_ip

    def get(self):
        ext_ip = self.request.remote_ip
        int_ip = memcache.get(self.MemcacheKey(ext_ip))
        self.write({
            'response': 'ok',
            'ip_map_from': ext_ip,
            'ip_map_to': int_ip
        })

    def post(self):
        data = json_decode(self.request.body)
        ext_ip = self.request.remote_ip
        int_ip = data['int_ip']
        memcache.set(self.MemcacheKey(ext_ip), int_ip, time=PingHandler.EXPIRY)
        self.write({
            'response': 'ok',
            'ip_map_from': ext_ip,
            'ip_map_to': int_ip
        })
