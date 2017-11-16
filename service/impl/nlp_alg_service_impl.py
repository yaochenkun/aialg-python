#coding=utf-8
from __future__ import unicode_literals

import sys
import os.path
import logging
# sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

reload(sys)
sys.setdefaultencoding('utf8')

import constant.server_consts as server_consts
import json
from alg.tensorflow.demo_model import DemoModel
from alg.naive.wordseg_model import WordsegModel
from base_alg_service_impl import BaseAlgServiceImpl
from collections import OrderedDict

class NlpAlgServiceImpl(BaseAlgServiceImpl):
    
    def __init__(self, port):
        super(NlpAlgServiceImpl, self).__init__(port, server_consts.NLP_ALG_SERVER_NAME)
        # BaseAlgServiceImpl.__init__(self, port, server_consts.NLP_ALG_SERVER_NAME)
        self.__demo_model = DemoModel()
        self.__wordseg_model = WordsegModel()

    # compute the result according to origin 
    def predict(self, origin):

        logging.info('start predicate, the origin value is %s' % origin)
        result = self._demo_model.predict(origin)
        logging.info('the result is %s'%result)
        return json.dumps({'result': str(result)})

    def hello(self, text):
        
        seg_list = self.__wordseg_model.predict(text)
        items = []
        byte_from = 0
        for i in range(len(seg_list)):
            seg = seg_list[i]

            byte_length = len(seg)
            byte_offset = byte_from
            byte_from = byte_from + byte_length

            element = dict()
            element["byte_length"] = byte_length
            element["byte_offset"] = byte_offset
            element["item"] = seg

            items.append(element)

        result = dict()
        result["text"] = text
        result["items"] = items

        return json.dumps(result)

    def bye(self):

        return json.dumps({'result': '今天天气真好~'})