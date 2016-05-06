#coding:utf8
#file is used to test the speed of split a paper
import codecs
import nltk
import threading
#单词拼写检查
import enchant

import re


anthor = 'tanghan'

Stemming = nltk.PorterStemmer()
spellcheck = enchant.Dict("en_US")
FEATHER_WORDS = []
for x in xrange(26):
    FEATHER_WORDS.append([])
COUNTER = []

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
            if len(res[x]) >= 4 and spellcheck.check(res[x]) and res[x].isalpha():
                res[x] = res[x].lower()
                vocau[getPos(res[x][0])].append(res[x])
    return vocau

def filter(vocau, stoplist, contents):
    count = 0
    for x in xrange(len(vocau)):
        if not vocau[x] == [] and not stoplist[x] == []:
            pos = getPos(vocau[x][0][0])
            print 'pos', pos
            count += 1
            t = threading.Thread(target=diff, args=(contents, vocau[x], stoplist[x], pos))
            t.start()
    print 'count:',count
    ts = threading.Thread(target=listenJ, args=(count,))
    ts.start()

def listenJ(count):
    while len(COUNTER) != count:
        print 'COUNTER',
        pass
    print 'END'
    del COUNTER[:]

def diff(contents, words, stopwords, pos):
    for x in xrange(len(words)):
        words[x] = words[x].strip()
        if stopwords.count(words[x]) == 0:
            contents[pos].append(words[x])
    COUNTER.append(1)
    print 'thread end'

def stemmer(wordlist):
    for x in xrange(len(wordlist)):
        for y in xrange(len(wordlist[x])):
            wordlist[x][y] = Stemming.stem(wordlist[x][y])

#first filter
Words = WordExtra('test.txt')
StopList = WordExtra('StopList.txt')
filter(Words, StopList, FEATHER_WORDS)

#stemming
FEATHER_STEM_WORDS = []
for x in xrange(26):
    FEATHER_STEM_WORDS.append([])
stemmer(Words)
print 'Second'
filter(Words, StopList, FEATHER_STEM_WORDS)
print Words