import sys
import os.path
# sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from constant import env_consts
from constant import server_consts
from constant import module_consts
from constant import class_consts
from common_server_laucher import load_server_config_and_start

def load_video_server():

    # load server's config and start servers
    load_server_config_and_start(server_consts.VIDEO_ALG_SERVER_NAME,
                                 env_consts.SERVER_IP,
                                 env_consts.VIDEO_ALG_SERVER_PORT_RANGE,
                                 module_consts.VIDEO_ALG_SERVICE_INTER_MODULE_NAME,
                                 class_consts.VIDEO_ALG_SERVICE_INTER_CLASS_NAME,
                                 module_consts.VIDEO_ALG_SERVICE_IMPL_MODULE_NAME,
                                 class_consts.VIDEO_ALG_SERVICE_IMPL_CLASS_NAME)

    # hold on the parent process
    sys.exit(1)




