import sys

if __name__ == '__main__':

    sys.path.append(r'/home/windylee/PyProj/ai-alg')

    import constant.EnvConsts as envConsts
    from ServerConfigLoader import loadServerConfigAndStart
    # load server's config and start servers
    loadServerConfigAndStart(envConsts.NLP_ALG_SERVER_NAME,
                             envConsts.SERVER_IP,
                             envConsts.NLP_ALG_SERVER_PORT_RANGE,
                             envConsts.NLP_ALG_SERVICE_INTER_MODULE_NAME,
                             envConsts.NLP_ALG_SERVICE_INTER_CLASS_NAME,
                             envConsts.NLP_ALG_SERVICE_IMPL_MODULE_NAME,
                             envConsts.NLP_ALG_SERVICE_IMPL_CLASS_NAME)

    # hold on the parent process
    sys.exit(1)




