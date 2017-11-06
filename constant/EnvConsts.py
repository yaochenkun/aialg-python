# 9000: Nlp Haproxy 9001-9009: Nlp Servers
# 9010: Image Haproxy 9011-9019: Image Servers
# 9020: Speech Haproxy 9021-9029: Speech Servers
# 9030: Video Haproxy 9031-9039: Video Servers

SERVER_IP = '10.108.112.50'

NLP_ALG_SERVER_NAME = 'NLP'
NLP_ALG_SERVICE_INTER_MODULE_NAME = 'service.inter.NlpAlgService'
NLP_ALG_SERVICE_INTER_CLASS_NAME = 'Processor'
NLP_ALG_SERVICE_IMPL_MODULE_NAME = 'service.impl.NlpAlgServiceImpl'
NLP_ALG_SERVICE_IMPL_CLASS_NAME = 'NlpAlgServiceImpl'
NLP_ALG_SERVER_PORT_RANGE = '9001-9009'
NLP_ALG_DEMO_MODEL_PATH = '/home/windylee/PyProj/ai-alg/model/demo_model.ckpt'

IMAGE_ALG_SERVER_NAME = 'IMAGE'
IMAGE_ALG_SERVICE_INTER_MODULE_NAME = 'service.inter.ImageAlgService'
IMAGE_ALG_SERVICE_INTER_CLASS_NAME = 'Processor'
IMAGE_ALG_SERVICE_IMPL_MODULE_NAME = 'service.impl.ImageAlgServiceImpl'
IMAGE_ALG_SERVICE_IMPL_CLASS_NAME = 'ImageAlgServiceImpl'
IMAGE_ALG_SERVER_PORT_RANGE = '9011-9019'

SPEECH_ALG_SERVER_NAME = 'SPEECH'
SPEECH_ALG_SERVICE_INTER_MODULE_NAME = 'service.inter.SpeechAlgService'
SPEECH_ALG_SERVICE_INTER_CLASS_NAME = 'Processor'
SPEECH_ALG_SERVICE_IMPL_MODULE_NAME = 'service.impl.SpeechAlgServiceImpl'
SPEECH_ALG_SERVICE_IMPL_CLASS_NAME = 'SpeechAlgServiceImpl'
SPEECH_ALG_SERVER_PORT_RANGE = '9021-9029'

VIDEO_ALG_SERVER_NAME = 'VIDEO'
VIDEO_ALG_SERVICE_INTER_MODULE_NAME = 'service.inter.VideoAlgService'
VIDEO_ALG_SERVICE_INTER_CLASS_NAME = 'Processor'
VIDEO_ALG_SERVICE_IMPL_MODULE_NAME = 'service.impl.VideoAlgServiceImpl'
VIDEO_ALG_SERVICE_IMPL_CLASS_NAME = 'VideoAlgServiceImpl'
VIDEO_ALG_SERVER_PORT_RANGE = '9031-9039'
