import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

if __name__ == '__main__':

    # sys.path.append(r'/home/windylee/PyProj/ai-alg')
    #
    # import constant.env_consts as envConsts
    # from common_server_laucher import loadServerConfigAndStart

    # load server's config and start servers
    sys.path.append('..')
    import constant.env_consts as env_consts
    import constant.server_consts as server_consts
    import constant.module_consts as module_consts
    import constant.class_consts as class_consts
    from common_server_laucher import load_server_config_and_start
    load_server_config_and_start(server_consts.NLP_ALG_SERVER_NAME,
                                 env_consts.SERVER_IP,
                                 env_consts.NLP_ALG_SERVER_PORT_RANGE,
                                 module_consts.NLP_ALG_SERVICE_INTER_MODULE_NAME,
                                 class_consts.NLP_ALG_SERVICE_INTER_CLASS_NAME,
                                 module_consts.NLP_ALG_SERVICE_IMPL_MODULE_NAME,
                                 class_consts.NLP_ALG_SERVICE_IMPL_CLASS_NAME)

    # hold on the parent process
    sys.exit(1)




