import constant.EnvConsts as envConsts
from ServerConfigLoader import loadServerConfigAndStart
import sys

if __name__ == '__main__':

    # load server's config and start servers
    loadServerConfigAndStart(envConsts.IMAGE_ALG_SERVER_NAME,
                             envConsts.SERVER_IP,
                             envConsts.IMAGE_ALG_SERVER_PORT_RANGE,
                             envConsts.IMAGE_ALG_SERVICE_INTER_MODULE_NAME,
                             envConsts.IMAGE_ALG_SERVICE_INTER_CLASS_NAME,
                             envConsts.IMAGE_ALG_SERVICE_IMPL_MODULE_NAME,
                             envConsts.IMAGE_ALG_SERVICE_IMPL_CLASS_NAME)

    # hold on the parent process
    sys.exit(1)



