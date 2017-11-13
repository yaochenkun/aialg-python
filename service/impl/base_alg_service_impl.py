import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

class BaseAlgServiceImpl(object):
    def __init__(self, port, server_name):
        self._port = port
        self._server_name = server_name
