#!/usr/bin/env python
# -*- coding: utf-8 -*-


class BaseAlgServiceImpl(object):
    """所有thrift接口的父类
    保存的接口监听的端口号和服务名称
    """
    def __init__(self, port, server_name):
        self._port = port
        self._server_name = server_name
