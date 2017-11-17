#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from constant import env_consts
from constant import server_consts
from constant import module_consts
from constant import class_consts
from server.common_server_laucher import load_server_config_and_start


def load_speech_server():

    # load server's config and start servers
    load_server_config_and_start(
        server_consts.SPEECH_ALG_SERVER_NAME, env_consts.SERVER_IP,
        env_consts.SPEECH_ALG_SERVER_PORT_RANGE,
        module_consts.SPEECH_ALG_SERVICE_INTER_MODULE_NAME,
        class_consts.SPEECH_ALG_SERVICE_INTER_CLASS_NAME,
        module_consts.SPEECH_ALG_SERVICE_IMPL_MODULE_NAME,
        class_consts.SPEECH_ALG_SERVICE_IMPL_CLASS_NAME)

    # hold on the parent process
    sys.exit(1)
