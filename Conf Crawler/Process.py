import sys
import SQLConn
import SQLConnCra
import os
import Crawler
import Parse
from bs4 import BeautifulSoup
             
def Init(pr, sql):
     pr.sql = sql

def processConfMain(confId):
     content  = cr.crawlPaperMain(confId)
     soup = BeautifulSoup(content)
     arr_paperId = pr.parseMainPage(soup)
     return arr_paperId

def outPut_sql(paper):
     qa_sql = SQLConnCra.QASQL()
     if(qa_sql.checkPaper(paper.id) == False):
          qa_sql.InsertPaper(paper)

def processPaper(paperId):
     content = cr.crawlPaperMain(paperId)
     soup = BeautifulSoup(content)
     paper = pr.getPaperInfo(soup)
     paper.id = paperId
     outPut_sql(paper)

if(len(sys.argv) != 2):
     print('arg err')
     exit()

cr = Crawler.Crawler()
pr = Parse.Parse()

sql = SQLConn.QASQL()
sqlcra = SQLConnCra.MysqlUti()

Init(pr, sqlcra)
arr_conf = sql.getConf(sys.argv[1])
#arr_conf = sql.getConf("SIGIR")
for item in arr_conf:
     confId = item[0]
     print(confId)

     arr_paperId = processConfMain(confId)

     for paperId in arr_paperId:
          print(paperId)
         
          try:
               pr.testPaper(paperId)
               processPaper(paperId)
               sqlcra.updatePaper(paperId, 1)
          except:
               sqlcra.insertErr('Paper Err', paperId, cr.lastPath)
               sqlcra.updatePaper(paperId, -1)



