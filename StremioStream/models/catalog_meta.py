class CatalogMeta:
    def __init__(self,id,name,description):
        self.id=id
        self.name=name
        self.description=description
        self.type='movie'
    def fromJson(data):
        parsed=data
        return CatalogMeta(id='ss'+str(parsed["_id"]),name=parsed["name"],description=f'Name: {parsed["name"]} \n Size: {int(parsed["size"])>>20}MB.')
    def __str__(self):
        return f"{self.id}, {self.name}, {self.poster}"
    def toMeta(self):
        return  {
		'id': self.id,
		'name':self.name,
		'type':self.type,
		'description':self.description
	}