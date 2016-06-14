#coding:utf8
#time:2016.05.07
#file is used to established a website to get imgs
import StringIO
import os
from PIL import Image

from tornado import web, ioloop, escape

class UploadFileHandler(web.RequestHandler):
    def get(self):
        # items = ['image/bg.jpg', 'image/bg1.jpg', 'image/bg2.jpg']
        # self.render('FileUpload.html', items=items)
        self.write('''
            <html>
              <head><title>Upload File</title></head>
              <body>
                <form action='file' enctype="multipart/form-data" method='post'>
                <input type='file' name='file'/><br/>
                <input type='submit' value='submit'/>
                </form>
              </body>
            </html>
            ''')

    def post(self):
        upload_path = os.path.dirname(__file__)+'\\' + 'static\\userimage'  #文件的暂存路径
        if not os.path.exists(upload_path):
            os.mkdir(upload_path)
        file_metas = self.request.files['file']    #提取表单中‘name’为‘file’的文件元数据
        print file_metas
        for meta in file_metas:
            filename=meta['filename']
            print filename
            filepath = upload_path + '\\' + filename
            print filepath
            with open(filepath, 'wb') as up:      #有些文件需要已二进制的形式存储，实际中可以更改
                up.write(meta['body'])
            self.defwithimage(filepath)
            self.write('finished!')

    def defwithimage(self, imgpath):
        img = Image.open(imgpath)
        img.show()
