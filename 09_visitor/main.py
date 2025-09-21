from animals import Dog, Cat
from operations import Sound

def accept_visitor(visitor):
    visitor.execute_method()

dog = Dog()
dog_sound = Sound("dog")
dog.accept_visitor = accept_visitor
dog.accept_visitor(dog_sound)


cat = Cat()
cat_sound = Sound("cat")
cat.accept_visitor = accept_visitor
cat.accept_visitor(cat_sound)