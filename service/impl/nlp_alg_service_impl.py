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
from base_alg_service_impl import BaseAlgServiceImpl
from deepnlp import segmenter

class NlpAlgServiceImpl(BaseAlgServiceImpl):
    
    def __init__(self, port):
        super(NlpAlgServiceImpl, self).__init__(port, server_consts.NLP_ALG_SERVER_NAME)
        # BaseAlgServiceImpl.__init__(self, port, server_consts.NLP_ALG_SERVER_NAME)
        self._demo_model = DemoModel()

    # compute the result according to origin 
    def predict(self, origin):

        logging.info('start predicate, the origin value is %s' % origin)
        result = self._demo_model.predict(origin)
        logging.info('the result is %s'%result)
        return json.dumps({'result': str(result)})

    def hello(self, text):

        logging.info('start predicate, the origin value is %s' % text)
        segList = segmenter.seg(text)
        text_seg = " ".join(segList)
        logging.info('the result is %s' % text_seg)

        return json.dumps({'result': text_seg})

    def bye(self):

        return json.dumps({'result': '今天天气真好~'})