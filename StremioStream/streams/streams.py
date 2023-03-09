

import requests
from threading import Thread
import os
from StremioStream.constants import TGARCHIVEAPI_URL
from time import time
class Streams:
    def __init__(self,type,fullId):
        from StremioStream.constants import TGARCHIVEAPI_DOWNLOAD_URL
        self.base_stream=TGARCHIVEAPI_DOWNLOAD_URL+'/{}'
        self.id=fullId
        self.results=[]
        self.type='movie'
    def getStreamDetails(self):
        pass
    def parseStreams(self,id):
        print(id)
        if id[:2]=='ss':
            META_URL=TGARCHIVEAPI_URL+'/file?id={}'
            res=requests.get(META_URL.format(id.split('ss')[-1]))
            r=res.json().get('document')
            s={'behaviorHints':{'notWebReady':True},'name':f'StremioStream {int(r["size"])>>20 or ""}MB','title':r.get('name',''),'url':f"{self.base_stream.format(str(id.split('ss')[-1]))}"}
            self.results.append(s)
        elif id[:2]=='tt':
            if ':' in id:
                self.type='series'
                self.season=id.split(':')[1]
                self.episode=id.split(':')[2]
            cinemeta=f"https://v3-cinemeta.strem.io/meta/movie/{id.split(':')[0]}.json"
            cin_res=requests.get(cinemeta).json().get('meta')
            
            self.name=cin_res.get('name','').replace(':','').replace("'",'')
            self.year=cin_res.get('year','')
            query=f"{self.name} + {self.year}" if self.type=='movie' else f"{self.name} S{self.season}E{self.episode}"
            TGARCHIVEAPI_URL_FOR_SEARCH=TGARCHIVEAPI_URL+f'/search?name={query.replace(" ","%20")}&page=1'
            res=requests.get(TGARCHIVEAPI_URL_FOR_SEARCH,headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}).json()
            r=res.get('documents')
            print(TGARCHIVEAPI_URL_FOR_SEARCH)
            for i in r:
                s={'behaviorHints':{'notWebReady':True },'name':f'StremioStream {int(i["size"])>>20 or ""}MB','title':i.get('name',''),'url':f"{self.base_stream.format(str(i.get('_id')))}"}
                self.results.append(s)
            query=f"{self.name} + {self.year}" if self.type=='movie' else f"{self.name} S0{self.season}E0{self.episode}"
            TGARCHIVEAPI_URL_FOR_SEARCH=TGARCHIVEAPI_URL+f'/search?name={query.replace(" ","%20")}&page=1'
            res=requests.get(TGARCHIVEAPI_URL_FOR_SEARCH,headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}).json()
            r=res.get('documents')
            print(TGARCHIVEAPI_URL_FOR_SEARCH)
            for i in r:
                s={'behaviorHints':{'notWebReady':True },'name':f'StremioStream {int(i.get("size","500"))>>20 or ""}MB','title':i.get('name',''),'url':f"{self.base_stream.format(str(i.get('_id')))}"}
                self.results.append(s)
        elif id[:2]=='ST':
            query=f"{id.split('ST')[-1]}"
            TGARCHIVEAPI_URL_FOR_SEARCH=TGARCHIVEAPI_URL+f'/search?name={query.replace(" ","%20")}&page=1'
            res=requests.get(TGARCHIVEAPI_URL_FOR_SEARCH,headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}).json()
            r=res.get('documents')
            print(TGARCHIVEAPI_URL_FOR_SEARCH)
            for i in r:
                s={'behaviorHints':{'notWebReady':True },'name':f'StremioStream {int(i["size"])>>20 or ""}MB','title':i.get('name',''),'url':f"{self.base_stream.format(str(i.get('_id')))}"}
                self.results.append(s)
            

    def get_streams(self):
        self.parseStreams(self.id)
        # self.results.sort(key=lambda x:int(x.get('title').replace('backup','10000').replace('default','100000').replace('0p','')),reverse=True)
        print(self.results)
        self.results.sort(key=lambda x:x.get('name'),reverse=True)
        return self.results


