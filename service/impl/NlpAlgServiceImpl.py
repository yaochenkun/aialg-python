import constant.EnvConsts as envConsts
import alg.tensorflow.TensorFlowDemo as tfd
import json


class NlpAlgServiceImpl:
    def __init__(self, port):
        self.log = {}
        self.port = port
        self.serverName = envConsts.NLP_ALG_SERVER_NAME
        self.demoModel = tfd.demoModel()

    # compute the result according to origin 
    def predict(self, origin):
        print "start predicate, the origin value is ", origin
        result = self.demoModel.demoPredict(origin)
        print "the result is ", result
        return json.dumps({'result': str(result)})

    def hello(self, key):
        print self.serverName, "server on port", self.port, ":'hello' method has been called"
        return self.serverName + " server: hello " + str(key)

    def bye(self):
        print self.serverName, "server on port", self.port, ":'bye' method has been called"
        return self.serverName + " server: goodbye~"
