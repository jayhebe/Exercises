class Person:
    name = "Person"
    
    def __init__(self, name = None):
        self.name = name
        
jeffrey = Person("Jeffery")
print("%s name is %s" % (Person.name, jeffrey.name))

nico = Person()
nico.name = "Nico"
print("%s name is %s" % (Person.name, nico.name))