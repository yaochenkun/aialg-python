import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import constant.server_consts as server_consts
import json
from alg.tensorflow.demo_model import DemoModel
from base_alg_service_impl import BaseAlgServiceImpl


class NlpAlgServiceImpl(BaseAlgServiceImpl):
    
    def __init__(self, port):
        super(NlpAlgServiceImpl, self).__init__(port, server_consts.NLP_ALG_SERVER_NAME)
        # BaseAlgServiceImpl.__init__(self, port, server_consts.NLP_ALG_SERVER_NAME)
        self._demo_model = DemoModel()

    # compute the result according to origin 
    def predict(self, input_value):

        print "start predicate, the origin value is ", input_value
        result = self._demo_model.predict(input_value)
        print "the result is ", result
        return json.dumps({'result': str(result)})

    def hello(self, key):

        print self._server_name, "server on port", self._port, ":'hello' method has been called"
        return self._server_name + " server: hello " + str(key)

    def bye(self):

        print self._server_name, "server on port", self._port, ":'bye' method has been called"
        return self._server_name + " server: goodbye~"
