import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import tensorflow as tf
import abc

class BaseModel(object):

    # abstract predict method waited to be override by SubModel
    @abc.abstractmethod
    def predict(self):
        return
