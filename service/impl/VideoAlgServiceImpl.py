class VideoAlgServiceImpl:
    def __init__(self):
        self.log = {}

    def hello(self, key):
        return "video: hello " + str(key)

    def bye(self):
        return "video: goodbye~"