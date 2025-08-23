from memento import Memento


my_memento = Memento()
my_memento.save_state("state 1")
my_memento.save_state("state 2")
my_memento.save_state("state 3")
my_memento.save_state("state 4")
my_memento.save_state("state 5")

print(my_memento.read_state())      # state 5

my_memento.undo()
my_memento.undo()
print(my_memento.read_state())      # state 3

my_memento.save_state("state 6")
print(my_memento.read_state())      # state 6

my_memento.redo()
print(my_memento.read_state())      # state 6

my_memento.undo()
print(my_memento.read_state())      # state 3

my_memento.redo()
print(my_memento.read_state())      # state 6