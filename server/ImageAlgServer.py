from thrift.protocol import TBinaryProtocol
from thrift.server import TServer
from thrift.transport import TSocket
from thrift.transport import TTransport

import constant.EnvConsts as envConsts
import service.inter.ImageAlgService as ImageAlgService
from service.impl.ImageAlgServiceImpl import ImageAlgServiceImpl


if __name__ == '__main__':

    processor = ImageAlgService.Processor(ImageAlgServiceImpl())
    transport = TSocket.TServerSocket(envConsts.IMAGE_ALG_HOST_IP, envConsts.IMAGE_ALG_HOST_PORT)
    tfactory = TTransport.TBufferedTransportFactory()
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()

    server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)

    # You could do one of these for a multithreaded server
    # server = TServer.TThreadedServer(
    #     processor, transport, tfactory, pfactory)
    # server = TServer.TThreadPoolServer(
    #     processor, transport, tfactory, pfactory)

    print('Starting the image server...')
    server.serve()