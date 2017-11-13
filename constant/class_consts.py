import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

# nlp
NLP_ALG_SERVICE_INTER_CLASS_NAME = 'Processor'
NLP_ALG_SERVICE_IMPL_CLASS_NAME = 'NlpAlgServiceImpl'

# image
IMAGE_ALG_SERVICE_INTER_CLASS_NAME = 'Processor'
IMAGE_ALG_SERVICE_IMPL_CLASS_NAME = 'ImageAlgServiceImpl'

# speech
SPEECH_ALG_SERVICE_INTER_CLASS_NAME = 'Processor'
SPEECH_ALG_SERVICE_IMPL_CLASS_NAME = 'SpeechAlgServiceImpl'

# video
VIDEO_ALG_SERVICE_INTER_CLASS_NAME = 'Processor'
VIDEO_ALG_SERVICE_IMPL_CLASS_NAME = 'VideoAlgServiceImpl'