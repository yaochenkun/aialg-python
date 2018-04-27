#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import logging
import json
import sys

from constant import server_consts
from service.impl.base_alg_service_impl import BaseAlgServiceImpl

reload(sys)
sys.setdefaultencoding('utf8')


class ImageAlgServiceImpl(BaseAlgServiceImpl):
    """图像处理的thrift接口
    """

    def __init__(self, port):
        BaseAlgServiceImpl.__init__(self, port,
                                    server_consts.IMAGE_ALG_SERVER_NAME)
        # instance image models here
        # ex: self.__demo_model = DemoModel()

    def face_sim(self, img_base64_1, img_base64_2):
        logging.info("the client visit face_sim")
        return json.dumps({'sim':'80%'})
