#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from deepnlp import segmenter
from deepnlp import pos_tagger


class NaiveModel(object):
    """包含了分词，词性标注，命名实体识别功能
    """

    def __init__(self):
        self._pos_tragger = pos_tagger.load_model('zh')

    def segment(self, text):
        """提供分词功能
        参数text为要分词的句子
        返回包含分词结果的list
        """
        words = segmenter.seg(text)
        return words

    def pos(self, text):
        """提供词性标注功能
        参数text为要进行词性标注的句子
        返回值为dict，key为分词结果，value为没个词的词性
        """
        words = segmenter.seg(text)
        tagging = self._pos_tragger.predict(words)
        return tagging