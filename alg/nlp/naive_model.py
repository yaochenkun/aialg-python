#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from deepnlp import segmenter
from deepnlp import pos_tagger
from deepnlp import ner_tagger


class NaiveModel(object):
    """包含了分词，词性标注，命名实体识别功能
    """

    def __init__(self):
        self._tokenizer = segmenter.load_model('zh')
        self._pos_tagger = pos_tagger.load_model('zh')
        self._ner_tagger = ner_tagger.load_model('zh')

    def segment(self, text):
        """提供分词功能
        参数text为要分词的句子
        返回包含分词结果的list
        """
        words = self._tokenizer.seg(text)
        return words

    def pos(self, text):
        """提供词性标注功能
        参数text为要进行词性标注的句子
        返回值为dict，key为分词结果，value为每个词的词性
        """
        words = self._tokenizer.seg(text)
        tagging = self._pos_tagger.predict(words)
        return tagging

    def ner(self, text):
        """提供命名实体识别功能
        参数text为要进行命名实体识别的句子
        """
        words = self._tokenizer.seg(text)
        tagging = self._ner_tagger.predict(words)
        return tagging