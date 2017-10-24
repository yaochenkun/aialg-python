class NlpAlgServiceImpl:
    def __init__(self):
        self.log = {}

    def hello(self, key):
        return "nlp: hello " + str(key)

    def bye(self):
        return "nlp: goodbye~"