import constant.EnvConsts as envConsts


class VideoAlgServiceImpl:
    def __init__(self, port):
        self.log = {}
        self.port = port
        self.serverName = envConsts.VIDEO_ALG_SERVER_NAME

    def hello(self, key):
        print self.serverName, "server on port", self.port, ":'hello' method has been called"
        return self.serverName + " server: hello " + str(key)

    def bye(self):
        print self.serverName, "server on port", self.port, ":'bye' method has been called"
        return self.serverName + " server: goodbye~"
