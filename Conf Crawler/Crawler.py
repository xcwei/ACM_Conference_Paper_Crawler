import urllib.request
import time
import random
import os
import os.path
import Parse

class Crawler():
    lastPath = ''
    
    def crawlURL(self, url):
        time.sleep(random.randint(1,5))
        headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko'}
        req = urllib.request.Request(url, headers=headers)
        content = urllib.request.urlopen(req).read()
        self.saveUrl(url, content, 'HTML_Data')
        return content

    def saveUrl(self, url, content, root_path):
        url = url.replace('http://','').replace('/','#').replace('?','$')
        d_list = os.listdir(root_path)
        n_dir = len(d_list) - 1
        if(n_dir == -1):
            n_dir = 0
            os.mkdir(root_path + '\\' + str(n_dir))
        dir_path = root_path + '\\' + str(n_dir)
        f_list = os.listdir(dir_path)
        n_file = len(f_list)
        if(n_file > 9999):
            dir_path = root_path + '\\' + str(n_dir + 1)
            os.mkdir(dir_path)

        file_path = dir_path + '\\' + url + '.html'
        file = open(file_path, 'wb')
        file.write(content)
        file.close()
        self.lastPath = file_path

    def crawlPaperMain(self, PaperId):
        url = 'http://dl.acm.org/citation.cfm?id=' + PaperId + '&preflayout=flat'
        return self.crawlURL(url)

