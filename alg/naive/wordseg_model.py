#coding=utf-8
from __future__ import unicode_literals

import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
reload(sys)
sys.setdefaultencoding('utf8')

from alg.naive.base_model import BaseModel
from deepnlp import segmenter

class WordsegModel(BaseModel):

    def predict(self, text):
        return segmenter.seg(text)