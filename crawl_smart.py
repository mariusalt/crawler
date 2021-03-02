import time
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import csv
import itertools

class CrawledArticle():
    def __init__(self, phone, talk, web, video):
        self.phone = phone
        self.talk = talk
        self.web = web
        self.video = video

class ArticleFetcher():
    def fetch(self):
        url = "https://www.gsmarena.com/battery-test.php3"

        while url != "":
            print(url)
            time.sleep(1)
            r = requests.get(url)
            soup = BeautifulSoup(r.text, "lxml")
  #          soup = BeautifulSoup(resp.text,"html5lib")
 #           mytable=doc.find_all('table',{‘class’:’keywords persist-area ’})
            My_table = soup.find('tbody')
            alltd=[]
 #           phone=[]
  #          end_rate=[]
   #         talk=[]
    #        web=[]
     #       video=[]
            for tag in My_table.find_all('td'):
                alltd.append(tag.contents)
            end_rate=alltd[1::6]
            talk=alltd[2::6]
            web=alltd[3::6]
            video=alltd[4::6]
            cus_rat=alltd[5::6]
            phone=[]
            for p in My_table.find_all('a'):
                phone.append(p.contents)
            del phone[1::2]

                
            cate=[phone,end_rate,talk,web,video,cus_rat]
            for cat in cate:
                for n,l in enumerate(cat):
                    for val in l:
                        subtree=BeautifulSoup(str(val),"lxml")
                        s = subtree.text
                        s = str(val)
                        s = s.replace('\n',' ')
                        s = s.strip()
                        cat[n]=s

            

#Writing to file.
            
            for n,i in enumerate(phone):
                newstr = i.replace("<a href=", "")
                newstr = newstr.replace('.php">', "--")
                newstr = newstr.replace("</a>", "")
                phone[n]=newstr

            for n,i in enumerate(talk):
                newstr = i.replace(":", ".")
                newstr = newstr.strip('h')
                talk[n]=newstr
 #               i[n]=newstr
            for n,i in enumerate(web):
                newstr = i.replace(":", ".")
                newstr = newstr.strip('h')
                web[n]=newstr

            for n,i in enumerate(video):
                newstr = i.replace(":", ".")
                newstr = newstr.strip('h')
                video[n]=newstr
                
            all=[]
            for i in range(len(phone)):
                l=[]
                for cat in cate:
                    l.append(cat[i])
                all.append(l)
    

            with open('guestFile2.csv', 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(('Phone','Talk_time' ,'Web_time','Video_time'))
                writer.writerows(zip(phone,talk,web,video))
            break


fetcher = ArticleFetcher()
fetcher.fetch()
 
#with open('crawler_out.csv','w',newline='') as csvfile:
 #   articlewriter = csv.writer(csvfile, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
#
 #   for article in fetcher.fetch():
  #      articlewriter.writerow([article.phone, article.talk, article.web, article.video])

#