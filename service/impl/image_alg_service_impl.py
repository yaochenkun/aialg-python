#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import logging

from constant import server_consts
from service.impl.base_alg_service_impl import BaseAlgServiceImpl


class ImageAlgServiceImpl(BaseAlgServiceImpl):
    """图像处理的thrift接口
    """

    def __init__(self, port):
        BaseAlgServiceImpl.__init__(self, port,
                                    server_consts.IMAGE_ALG_SERVER_NAME)
        # instance image models here
        # ex: self.__demo_model = DemoModel()

    def hello(self, key):
        """hello
        """
        logging.info('%s server on port %s : "hello" method has been called',
                     self._server_name, self._port)
        return self._server_name + " server: hello " + str(key)

    def bye(self):
        """bye
        """
        logging.info('%a server on port %s "bye" method has been called',
                     self._server_name, self._port)
        return self._server_name + " server: goodbye~"
