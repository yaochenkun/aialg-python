import tensorflow as tf
import abc

class BaseModel(object):

    def __init__(self, model_path):
        self.define_variables()
        self.restore_variables(model_path)

    # define model's variables
    @abc.abstractmethod
    def define_variables(self):
        return

    # resotre variables from model file
    def restore_variables(self, model_path):
        self._model_path = model_path
        self._session = tf.Session()
        self._saver = tf.train.Saver()
        self._saver.restore(self._session, self._model_path)

    # abstract train method waited to be override by SubModel
    @abc.abstractmethod
    def train(self):
        return

    # abstract predict method waited to be override by SubModel
    @abc.abstractmethod
    def predict(self, x_value):
        return
