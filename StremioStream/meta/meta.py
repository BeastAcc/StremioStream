
import requests
from StremioStream.models.episode import Episode
from StremioStream.constants import TGARCHIVEAPI_URL
META_URL=TGARCHIVEAPI_URL+'/file?id={}'
def mk_item(item,id):
        meta = dict()
        meta['id'] =id
        meta['type'] = 'movie'
        meta['name'] = item.get('name','')
        meta['description']=f'Name: {item["name"]} \n Size: {int(item["size"])>>20}MB.'
        return meta
#TODO:Check meta if no episode exist,do something else insread of res.json().get('id') as it stops zoro for lost girls too.
def getMeta(id):

    res=requests.get(META_URL.format(id.replace('ss','')),headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'})
    return mk_item(res.json().get('document'),id)
