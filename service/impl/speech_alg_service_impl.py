import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import constant.server_consts as server_consts
from base_alg_service_impl import BaseAlgServiceImpl

class SpeechAlgServiceImpl(BaseAlgServiceImpl):
    def __init__(self, port):
        BaseAlgServiceImpl.__init__(self, port, server_consts.SPEECH_ALG_SERVER_NAME)
        # instance speech models here
        # ex: self.__demo_model = DemoModel()

    def hello(self, key):
        print self._server_name, "server on port", self._port, ":'hello' method has been called"
        return self._server_name + " server: hello " + str(key)

    def bye(self):
        print self._server_name, "server on port", self._port, ":'bye' method has been called"
        return self._server_name + " server: goodbye~"

