#coding:utf-8
__author__ = 'tanghan'

from url import url
from tornado import web
import os

setting = dict(
    template_path='./template',
    static_path='./static',
)

application = web.Application(
    handlers=url,
    **setting
)