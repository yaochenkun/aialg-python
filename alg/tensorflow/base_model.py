import tensorflow as tf

class BaseModel:

    def __init__(self, model_path):

        self._model_path = model_path
        self._session = tf.Session()
        self._saver = tf.train.Saver()
        self._saver.restore(self._session, self._model_path)

    # abstract train method waited to be override by SubModel
    def train(self):
        pass

    # abstract predict method waited to be override by SubModel
    def predict(self):
        pass
