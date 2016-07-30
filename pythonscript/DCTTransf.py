#coding:utf8
#time: 2016.07.29
# DCT(离散余弦变换)
import hashlib
import imghdr
import math
import os

from PIL import Image

Image_Format = ['rgb', 'gif', 'pbm', 'pgm', 'ppm', 'tiff', 'rast', 'xbm', 'jpeg', 'bmp', 'png']

class phash:
    def __init__(self, imgpath):
        if imghdr.what(imgpath) not in Image_Format:
            print 'phash init error: need image'
            exit(-1)
        self.imgpath = imgpath

    # 获取hashstr值
    def gethashstr(self):
        #放缩为32*32的灰度图像
        grayimg = ((Image.open(self.imgpath)).resize((32, 32))).convert('L')
        #获取像素矩阵
        pixdata = grayimg.load()
        pix = []
        for x in xrange(0, 32):
            temp = []
            for y in xrange(0, 32):
                temp.append(pixdata[x, y])
            pix.append(temp)

        # 计算DCT
        martix = self.DCT(pix, 32)


        newmartix = []
        # 截取前8*8矩阵, 获取平均值
        total = 0
        for x in xrange(len(martix)):
            for y in xrange(len(martix[0])):
                if x < 8 and y < 8 :
                    newmartix.append(martix[x][y])
                    total += martix[x][y]
        average = total/64
        # 组装为序列字符串， 并且计算hashstr值
        str = ''
        for x in xrange(len(newmartix)):
            if newmartix[x] <= average:
                str += '0'
            else:
                str += '1'
        m = hashlib.md5()
        m.update(str)
        return m.hexdigest()

    '''求离散余弦变换的系数矩阵, 返回系数矩阵
       param:
            1.n 矩阵大小
    '''
    def coefficient(self, n):
        coeff = []
        sqrt = 1.0/math.sqrt(n)
        coeff0 = []
        for i in xrange(0, n):
            coeff0.append(sqrt)
        coeff.append(coeff0)
        for i in xrange(1, n):
            temp = []
            for j in xrange(0, n):
                temp.append(math.sqrt(2.0/n)*math.cos(i*math.pi*(j+0.5)/float(n)))
            coeff.append(temp)

        return coeff

    '''矩阵转置'''
    def transposingMatrix(self, matrix, n):
        tMatrix = []
        for i in xrange(0, n):
            temp = []
            for j in xrange(0, n):
                temp.append(0)
            tMatrix.append(temp)

        for i in xrange(0, n):
            for j in xrange(0, n):
                tMatrix[i][j] = matrix[j][i]

        return tMatrix

    '''矩阵相乘'''
    def matrixMultiply(self, matrixA, matrixB, n):
        matrix = []
        for i in xrange(0, n):
            temp = []
            for j in xrange(0, n):
                t = 0.0
                for k in xrange(0, n):
                    t += matrixA[i][k] * matrixB[k][j]
                temp.append(t)
            matrix.append(temp)

        return matrix

    '''离散余弦变换， 返回值为变换后的矩阵数组
       params：
            1.pix 原图像的数据矩阵
            2.n 原图像的大小
    '''
    def DCT(self, pix, n):
        iMatrix = []
        for x in xrange(0, n):
            temp = []
            for y in xrange(0, n):
                temp.append(float(pix[x][y]))
            iMatrix.append(temp)

        # 求系数矩阵
        quotient = self.coefficient(n)
        # 转置系数矩阵
        quotientT = self.transposingMatrix(quotient, n)

        temp = self.matrixMultiply(quotient, iMatrix, n)
        iMatrix = self.matrixMultiply(temp, quotientT, n)

        newpix = []
        for i in xrange(0, n):
            temp = []
            for j in xrange(0, n):
                temp.append(int(iMatrix[i][j]))
            newpix.append(temp)

        return newpix

def gethashstr(imgpath):
    ph = phash(imgpath)
    return ph.gethashstr()