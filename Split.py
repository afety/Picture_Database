#coding:utf8
#file is used to test the speed of split a paper
anthor = 'tanghan'

def start(filename):
    vocau = []
    with open(filename,'r') as paper_in:
        temp = ''
        while True:
            temp = paper_in.readline()
            if not temp:
                break
            val = ''
            for pos in xrange(len(temp)):
                if temp[pos] == ' ' or pos == len(temp)-1:
                    if val != '':
                        vocau.append(val+temp[pos])
                        val = ''
                else:
                    val += temp[pos]
    print vocau

start('test')