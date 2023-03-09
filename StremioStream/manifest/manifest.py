from StremioStream.catalogs.catalogs import getCategories

MANIFEST={
    "id": "STB.stremio.StremioStream",
    "version": "1.0.0",
    "name": "StremioStream",
    "description": "Plugin to get streams in stremio.",
    "resources": ["stream",{'name': "meta", 'types': ["movie"],'idPrefixes': ['ss','ST']},"catalog"],
    "types": ["movie","series"],
    "catalogs": [
        {
            "id": "StremioStream", "type": "movie", "name": "StremioStream",
            "extra": [
                { "name": "skip", "isRequired": False },
                {'name': 'genre',
                    'isRequired': True,
                    'options':[i.get('name') for i in   getCategories()]
            
        }
    ]},
    {"id": "StremioStreamSearch", "type": "movie", "name": "StremioStreamSearch",
            "extra": [
                {"name": "search", "isRequired": True,},
                { "name": "skip", "isRequired": False },
    ]}
    ]
}