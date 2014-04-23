import Crawler
import Parse
from bs4 import BeautifulSoup

def singleTest(path):
    File = open(path, 'rb')
    soup = BeautifulSoup(File)
    pr = Parse.Parse()
    paper = pr.getPaperInfo(soup)
    print(paper.pub)


def testALl():
    file = open('log\\err.log', 'rb')
    pr = Parse.Parse()
    for line in file:
        path = line.decode('utf-8').split('\t')[1]
        print(path)
        f = open(path, 'rb')
        soup = BeautifulSoup(f)
        paper = pr.getPaperInfo(soup)


path = 'HTLM_Data\\0\\dl.acm.org#citation.cfm$id=1074423&preflayout=flat.html'
#singleTest(path)

testALl()
