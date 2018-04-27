#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.path.append('..')

from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
import service.inter.image_alg_service as image_alg_service

tSocket = TSocket.TSocket('localhost', 9011)
tTransport = TTransport.TBufferedTransport(tSocket)
protocol = TBinaryProtocol.TBinaryProtocol(tTransport)

client = image_alg_service.Client(protocol)
tTransport.open()

msg = client.face_sim('1', '2')
print(msg)
