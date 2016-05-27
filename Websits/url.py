#coding:utf8
__author__ = 'tanghan'

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from handlers import UploadFileHandler

url = [
    (r'/file', UploadFileHandler),
]