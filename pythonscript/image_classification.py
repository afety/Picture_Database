#coding:utf8
#call matlab function
import os
import matlab.engine

__author__ = 'tanghan'

category={
    "1": "breast",
    "2": "lungCR",
    "3": "lungCT",
    "4": "brain",
    "5": "abdomen",
    "6": "retinal.txt"
}

class classification:
    def __init__(self, imgpath):
        self.__imgpath = imgpath
        self.__eng = matlab.engine.start_matlab()
        self.__origindir = os.getcwd()
        self.__matlabdir = self.__origindir + "\imageclassification"
        self.__eng.addpath(self.__matlabdir)
        print self.__matlabdir

    def getclass(self):
        print self.__imgpath, self.__matlabdir
        classname = self.__getclassname(str(int(self.__eng.NewUseKnn(self.__imgpath, self.__matlabdir))))
        print classname

    def __getclassname(self, classnum):
        return category.get(classnum)

    def quit(self):
        self.__eng.quit()

if __name__ == "__main__":
    test = classification("C:\Users\tanghan\PycharmProjects\Picture_Database\Websits\static\userimage\\bg.jpg")
    test.getclass()
    test.quit()