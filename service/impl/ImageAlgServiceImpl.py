class ImageAlgServiceImpl:
    def __init__(self):
        self.log = {}

    def hello(self, key):
        return "image: hello " + str(key)

    def bye(self):
        return "image: goodbye~"