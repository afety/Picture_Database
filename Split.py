#coding:utf8
#file is used to test the speed of split a paper
import codecs
import nltk
import threading
#单词拼写检查
import enchant
import re


anthor = 'tanghan'

FEATHER_WORDS = []
Stemming = nltk.PorterStemmer()
spellcheck = enchant.Dict("en_US")
JUDGE = []

def getPos(char):
    if ord(char) < 97 or ord(char) > 122:
        return -1
    return ord(char) - 97

def WordExtra(filename):
    vocau = []
    for i in xrange(26):
        vocau.append([])
    with codecs.open(filename, 'r', 'utf-8') as filein:
        text = ''
        for line in filein.readlines():
            text += line[:len(line)-1]+" "
        res = nltk.word_tokenize(text)
        for x in xrange(len(res)):
            if len(res[x]) >= 4 and spellcheck.check(res[x]):
                res[x] = res[x].lower()
                vocau[getPos(res[x][0])].append(res[x])
    print vocau
    return vocau

def filter(vocau, stoplist):
    for x in xrange(len(vocau)):
        print 'create thread'
        t = threading.Thread(target=diff, args=(vocau[x], stoplist[x], x))
        t.start()
    print 'judge thread'
    t = threading.Thread(target=judge)
    t.start()

def judge():
    while not len(JUDGE) == 26:
        pass
    print FEATHER_WORDS

def diff(words, stopwords, pos):
    print 'thread start'
    result = []
    if words == [] or stopwords == []:
        pass
    else:
        for x in xrange(len(words)):
            count = 0
            for y in xrange(len(stopwords)):
                if words[x] == stopwords[y]:
                    count += 1
            if not count:
                result.append(words[x])

    FEATHER_WORDS.insert(pos, result)
    JUDGE.append(1)

Words = WordExtra('test.txt')
StopList = WordExtra('StopList.txt')
filter(Words, StopList)
