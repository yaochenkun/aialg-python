#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import sys
import logging
import json
from constant import server_consts
from alg.nlp.demo_model import DemoModel
from alg.nlp.naive_model import NaiveModel
from service.impl.base_alg_service_impl import BaseAlgServiceImpl

reload(sys)
sys.setdefaultencoding('utf8')


class NlpAlgServiceImpl(BaseAlgServiceImpl):
    """用于RPC调用的自然语言处理接口
    """

    def __init__(self, port):
        super(NlpAlgServiceImpl,
              self).__init__(port, server_consts.NLP_ALG_SERVER_NAME)
        self.__demo_model = DemoModel()
        self.__naive_model = NaiveModel()

    def predict(self, origin):
        """ compute the result according to origin
        """

        logging.info('start predicate, the origin value is %s', origin)
        result = self.__demo_model.predict(origin)
        logging.info('the result is %s', result)
        return json.dumps({'result': str(result)})

    def word_seg(self, text):
        """ 分词接口
        """
        seg_list = self.__naive_model.segment(text)
        items = []
        byte_from = 0
        for seg in seg_list:
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

        return json.dumps(result, ensure_ascii=False)

    def word_pos(self, text):
        """词性标注接口
        """
        tagging = self.__naive_model.pos(text)
        items = []
        byte_from = 0
        for word, pos in tagging:
            byte_length = len(word)
            byte_offset, byte_from = byte_from, byte_from + byte_length
            element = dict()
            element['byte_length'] = byte_length
            element['byte_offset'] = byte_offset
            element['item'] = word
            element['pos'] = pos

            items.append(element)
        result = dict()
        result['text'] = text
        result['items'] = items
        return json.dumps(result, ensure_ascii=False)
