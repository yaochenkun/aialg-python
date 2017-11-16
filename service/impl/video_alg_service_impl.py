#coding=utf-8
from __future__ import unicode_literals

import sys
import os.path
# sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from constant import server_consts
from base_alg_service_impl import BaseAlgServiceImpl


class VideoAlgServiceImpl(BaseAlgServiceImpl):
    def __init__(self, port):
        BaseAlgServiceImpl.__init__(self, port, server_consts.VIDEO_ALG_SERVER_NAME)
        # instance video models here
        # ex: self.__demo_model = DemoModel()

    def hello(self, key):
        logging.info("%s server on port %s:'hello' method has been called" % (self._server_name, self._port))
        return self._server_name + " server: hello " + str(key)

    def bye(self):
        logging.info("%s server on port %s:'bye' method has been called" % (self._server_name, self._port))
        return self._server_name + " server: goodbye~"

