import constant.EnvConsts as envConsts
from ServerConfigLoader import loadServerConfigAndStart
import sys

if __name__ == '__main__':

    # load server's config and start servers
    loadServerConfigAndStart(envConsts.VIDEO_ALG_SERVER_NAME,
                             envConsts.SERVER_IP,
                             envConsts.VIDEO_ALG_SERVER_PORT_RANGE,
                             envConsts.VIDEO_ALG_SERVICE_INTER_MODULE_NAME,
                             envConsts.VIDEO_ALG_SERVICE_INTER_CLASS_NAME,
                             envConsts.VIDEO_ALG_SERVICE_IMPL_MODULE_NAME,
                             envConsts.VIDEO_ALG_SERVICE_IMPL_CLASS_NAME)

    # hold on the parent process
    sys.exit(1)




