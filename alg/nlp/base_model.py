#!/usr/bin/env python
# -*- coding: utf-8 -*-

import abc
import tensorflow as tf


class BaseModel(object):
    def __init__(self, model_path):
        self.define_variables()
        self.restore_variables(model_path)

    @abc.abstractmethod
    def define_variables(self):
        """define model's variables
        """
        return

    def restore_variables(self, model_path):
        """resotre variables from model file
        """
        self._model_path = model_path
        self._session = tf.Session()
        self._saver = tf.train.Saver()
        self._saver.restore(self._session, self._model_path)

    @abc.abstractmethod
    def train(self):
        """abstract train method waited to be override by SubModel
        """
        return

    @abc.abstractmethod
    def predict(self, x_value):
        """abstract predict method waited to be override by SubModel
        """
        return
