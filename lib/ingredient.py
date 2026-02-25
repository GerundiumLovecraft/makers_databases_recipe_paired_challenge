class Ingredient:

    def __init__(self, id, name, spiciness):
        self.id = id
        self.name = name
        self.spiciness = spiciness
        
    def __eq__(self, another_ingredient):
        return self.__dict__ == another_ingredient.__dict__
        
    def __repr__(self):
        return f"{self.name} (Spiciness level: {self.spiciness})"