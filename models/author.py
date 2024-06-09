class Author:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, value):
        if isinstance(value, int):
            self._id = value
        else:
            raise ValueError("ID must be a type of integer")
    
    @property
    def name(self):
        return self._name 
    
    @name.setter
    def name(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._name = value
        else: 
            raise ValueError("Name must be a non-empty string")
        
    def __repr__(self):
        return f'<Author {self.name}>'
