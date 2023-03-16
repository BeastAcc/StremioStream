from StremioStream.constants import TGARCHIVEAPI_URL
TGARCHIVEAPI_URL_FOR_INDEX=TGARCHIVEAPI_URL+'/index?page={}'
TGARCHIVEAPI_URL_FOR_SEARCH=TGARCHIVEAPI_URL+'/search?name={}&page={}'
import requests
import json
from StremioStream.models.catalog_meta import  CatalogMeta
def getCategories():
        return [
            {
                'name': 'Trending',
                'endpoint': ''
            },
        ]
def getCatalog(genreFull='',search=''):
    page=1
    perPage=20 if genreFull else 60
    data=genreFull if genreFull else search
    data_query=data.replace('%20',' ')
    calatog_items=[]
    if 'skip' in data:
            data_query=data.split('&')[0]
            page+=int(data.split('skip=')[1])//perPage
    if genreFull:
            url=TGARCHIVEAPI_URL_FOR_INDEX.format(page)
    else:
            url=TGARCHIVEAPI_URL_FOR_SEARCH.format(data_query,page)     
    res=requests.get(url,headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'})
    if len(json.loads(res.content)['documents'])>0 and not genreFull:
           calatog_items=[CatalogMeta(description=data_query,name='All Results',id='ST'+str(data_query)).toMeta()]
    calatog_items.extend([CatalogMeta.fromJson(data=i).toMeta() for i in json.loads(res.content)['documents'] if 'video' in i.get('mime_type')])
    return calatog_items
