#coding:utf8
from PIL import Image

__author__ = 'tanghan'

def getGray(imgpath):
    return Image.open(imgpath).convert('L')

def otsu_getavegrayvalue(grayimg):
    size = grayimg.size
    total = 0
    for x in xrange(size[0]):
        for y in xrange(size[1]):
            total += grayimg.getpixel((x,y))

    return int(total/(size[0]*size[1]))

def otsu_com(thres, grayimg):
    pixels = grayimg.load()
    #prosprcts
    w0 = 1
    u0 = 0
    n0 = 0
    #background
    w1 = 1
    u1 = 0
    n1 = 0
    for x in xrange(grayimg.size[0]):
        for y in xrange(grayimg.size[1]):
            if pixels[x,y] <= thres:
                n0 += 1
                u0 += pixels[x,y]
            else:
                n1 += 1
                u1 += pixels[x,y]
    w0 = float(n0)/float((grayimg.size[0]*grayimg.size[1]))
    w1 = float(n1)/float((grayimg.size[0]*grayimg.size[1]))
    u0 = u0/n0
    u1 = u1/n1
    return w0*w1*pow((u0-u1),2)

def otsu_threds(grayimg):
    size = grayimg.size
    pixels = grayimg.load()
    min = max = pixels[0,0]
    for x in xrange(size[0]):
        for y in xrange(size[1]):
            if pixels[x,y] < min:
                min = pixels[x,y]
            if pixels > max:
                max = pixels[x,y]
    glist = {}
    g_origin = 0
    pos = 0
    for x in xrange(min, max):
        glist[str(x)] = otsu_com(x, grayimg)

    for key in glist.keys():
        if glist.get(key) > g_origin:
            g_origin = glist.get(key)
            pos = key
    return pos