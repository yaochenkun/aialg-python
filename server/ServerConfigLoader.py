import threading
import multiprocessing
from time import sleep

from thrift.protocol import TBinaryProtocol
from thrift.server import TServer
from thrift.transport import TSocket
from thrift.transport import TTransport


# start thrift server on port
def startServerHandle(serverName,
                      serverIP,
                      port,
                      serviceInterModuleName,
                      serviceInterClassName,
                      serviceImplModuleName,
                      serviceImplClassName):

    # dynamic generate service impl and inter class
    AlgServiceImplClass = getattr(__import__(serviceImplModuleName, globals(), locals(), [serviceImplClassName]), serviceImplClassName)
    AlgServiceProcessorClass = getattr(__import__(serviceInterModuleName, globals(), locals(), [serviceInterClassName]), serviceInterClassName)

    # instantiation class object
    algServiceProcessor = AlgServiceProcessorClass(AlgServiceImplClass(port))

    transport = TSocket.TServerSocket(serverIP, port)
    tfactory = TTransport.TBufferedTransportFactory()
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()

    server = TServer.TThreadPoolServer(algServiceProcessor, transport, tfactory, pfactory)

    print 'Starting the', serverName,'server on IP', serverIP, 'port', port
    server.serve()


def loadServerConfigAndStart(serverName,
                             serverIP,
                             serverPortRange,
                             serviceInterModuleName,
                             serviceInterClassName,
                             serviceImplModuleName,
                             serviceImplClassName):

    # get port range
    portRange = serverPortRange.split('-');
    portBegin = int(portRange[0])
    portEnd = int(portRange[1])

    # start servers
    for port in range(portBegin, portEnd + 1):
        # lauchServerThread = threading.Thread(target=startServerHandle, args=(serverName,
        #                                                                      serverIP,
        #                                                                      port,
        #                                                                      serviceInterModuleName,
        #                                                                      serviceInterClassName,
        #                                                                      serviceImplModuleName,
        #                                                                      serviceImplClassName))

        # lauchServerThread.setDaemon(True)
        # lauchServerThread.start()

        lauchServerProcess = multiprocessing.Process(target=startServerHandle, args=(
                                                                             serverName,
                                                                             serverIP,
                                                                             port,
                                                                             serviceInterModuleName,
                                                                             serviceInterClassName,
                                                                             serviceImplModuleName,
                                                                             serviceImplClassName))
        lauchServerProcess.start()
        sleep(0.2)  # delay starting to avoid console-print exception
