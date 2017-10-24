class SpeechAlgServiceImpl:
    def __init__(self):
        self.log = {}

    def hello(self, key):
        return "speech: hello " + str(key)

    def bye(self):
        return "speech: goodbye~"