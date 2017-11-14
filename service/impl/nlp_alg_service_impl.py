#coding=utf-8
from __future__ import unicode_literals

import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

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

        print "start predicate, the origin value is ", origin
        result = self._demo_model.predict(origin)
        print "the result is ", result
        return json.dumps({'result': str(result)})

    def hello(self, text):

        print "start predicate, the origin value is ", text
        segList = segmenter.seg(text)
        text_seg = " ".join(segList)
        print "the result is ", text_seg

        return json.dumps({'result': text_seg.encode('utf-8')})

    def bye(self):

        return json.dumps({'result': '今天天气真好~'})