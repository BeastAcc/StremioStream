import json
class Episode:
    def __init__(self,id,name,thumbnail,description,released,number,anilist_id):
        self.id=f"{anilist_id}__{id}"
        self.name=name
        self.thumbnail=thumbnail
        self.description=description
        self.released=released
        self.number=number
    def fromJson(data,anilist_id):
        parsed=data
        return Episode(id=parsed.get("id",''),
                       name=parsed.get("title",''),
                       thumbnail=parsed.get("image",''),
                       description=parsed.get('description',''),
                       released=parsed.get('airDate',''),
                       number=parsed.get('number',1),
                       anilist_id=anilist_id)
    def __str__(self):
        return f"{self.id}, {self.name}"
    def toMeta(self):
        return  {
		'id': self.id,
		'name':f'{self.number}. {self.name}',
		'thumbnail':self.thumbnail,
		'description':self.description,
        'number':self.number or '0',
        'released':self.released
	}