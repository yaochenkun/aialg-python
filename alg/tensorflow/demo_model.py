import sys
import os.path
# sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import threading
from time import sleep
from constant import model_consts
import tensorflow as tf
import logging
from base_model import BaseModel


class DemoModel(BaseModel):

    def __init__(self):
        
        super(DemoModel, self).__init__(model_consts.NLP_ALG_DEMO_MODEL_PATH)

    def define_variables(self):
        # constant define
        self._W = tf.Variable([.3], dtype=tf.float32, name='weight')
        self._b = tf.Variable([-.3], dtype=tf.float32, name='bias')
        # variable define
        self._x = tf.placeholder(tf.float32)
        self._predict = self._W * self._x + self._b

    # params should be local while not member
    def train(self):

        W = tf.Variable([.3], dtype=tf.float32, name='weight')
        b = tf.Variable([-.3], dtype=tf.float32, name='bias')
        x = tf.placeholder(tf.float32)
        linear_model = W * x + b
        y = tf.placeholder(tf.float32)
        loss = tf.reduce_sum(tf.square(linear_model - y))

        optimizer = tf.train.GradientDescentOptimizer(0.01)
        train = optimizer.minimize(loss)

        x_train = [1, 2, 3, 4]
        y_train = [0, -1, -2, -3]
        init = tf.global_variables_initializer()

        saver = tf.train.Saver()
        with tf.Session() as sess:
            sess.run(init)
            for i in range(1000):
                sess.run(train, {x: x_train, y: y_train})
            curr_w, curr_b, curr_loss = sess.run([W, b, loss], {x: x_train, y: y_train})
            logging.info("W: %s b: %s loss: %s" % (curr_w, curr_b, curr_loss))
            logging.info(sess.run(linear_model, {x: 3}))
            save_path = saver.save(sess, self._model_path)

    def predict(self, x_value):

        # simulate 2s' computing of tensorflow
        # sleep(2)
        return self._session.run(self._predict, {self._x: x_value})
