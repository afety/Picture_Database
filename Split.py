#coding:utf8
#file is used to test the speed of split a paper
import threading
from porterStemming import PorterStemmer

anthor = 'tanghan'

FEATHER_WORDS = []
Stemming = PorterStemmer()

def getPos(char):
    if ord(char) < 97 or ord(char) > 122:
        return -1
    return ord(char) - 97

def WordExtra(filename):
    vocau = []
    for i in xrange(26):
        vocau.append([])
    with open(filename,'r') as paper_in:
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
                    if val == '\'':
                        val = ''
                    val += temp[pos].lower()
    print vocau
    return vocau

def filter(vocau, stoplist):
    for x in xrange(vocau):
        t = threading.Thread(target=diff, args=(vocau[x], stoplist[x], x))
        t.start()
    while not FEATHER_WORDS: pass
    print FEATHER_WORDS


def diff(words, stopwords,pos):
    for x in xrange(len(words)):
        for y in xrange(len(stopwords)):
            if words[x] == stopwords[y]:
                del words[x]
    FEATHER_WORDS.insert(pos, words)

Words = WordExtra('test.txt')
StopList = WordExtra('StopList.txt')
filter(Words, StopList)
