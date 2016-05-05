#coding:utf8
#file is used to test the speed of split a paper
import codecs
import threading
import re
from porterStemming import PorterStemmer

anthor = 'tanghan'

FEATHER_WORDS = []
Stemming = PorterStemmer()

def getPos(char):
    if ord(char) < 97 or ord(char) > 122:
        return -1
    return ord(char) - 97

def WordExtra_reg(filename):
    vocau = []
    for i in xrange(26):
        vocau.append([])
    with codecs.open(filename, 'r', 'utf-8') as filein:
        text = ''
        for line in filein.readlines():
            text += line[:len(line)-1]+" "
        pattern = re.compile("\\w+")
        res = pattern.findall(text)
        for x in xrange(len(res)):
            if len(res[x]) >= 4:
                val = Stemming.stem(res[x], 0, len(res[x]) - 1)
                vocau[getPos(val[0])].append(val)
    return vocau

def WordExtra(filename):
    vocau = []
    for i in xrange(26):
        vocau.append([])
    with codecs.open(filename, 'r', 'utf-8') as paper_in:
        temp = ''
        while True:
            temp = paper_in.readline()
            if not temp:
                break
            val = ''
            for pos in xrange(len(temp)):
                if temp[pos] == ' ' or temp == '\n':
                    if val == '':
                        pass
                    else:
                        p = getPos(val[0])
                        val = Stemming.stem(val, 0, len(val)-1)
                        vocau[p].append(val)
                        val = ''
                else:
                    if val == '\'' or val.isdigit() or val == '\\':
                        val = ''
                    val += temp[pos].lower()
    print 40,vocau
    return vocau

def filter(vocau, stoplist):
    for x in xrange(len(vocau)):
        t = threading.Thread(target=diff, args=(vocau[x], stoplist[x], x))
        t.start()
    while not len(FEATHER_WORDS)==26: pass
    print 48, FEATHER_WORDS


def diff(words, stopwords, pos):
    if words == [] or stopwords == []:
        pass
    else:
        result = []
        for x in xrange(len(words)):
            for y in xrange(len(stopwords)):
                if not words[x] == stopwords[y] and not result.count(words[x]):
                    print 'append:',words[x]
                    result.append(words[x])

    FEATHER_WORDS.insert(pos, result)


Words = WordExtra_reg('test.txt')
StopList = WordExtra_reg('StopList.txt')
filter(Words, StopList)
