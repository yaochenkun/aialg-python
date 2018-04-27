#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import server.nlp_alg_server_laucher as nlp_laucher
import server.image_alg_server_laucher as img_laucher

if __name__ == '__main__':
    logging.basicConfig(
        format='%(asctime)s %(levelname)-8s: %(message)s', level=logging.INFO)

    logging.info('this is a information')
    # nlp_laucher.load_nlp_server()
    img_laucher.load_image_server()
    
