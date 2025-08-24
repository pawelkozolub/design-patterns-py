import copy
from memento import Memento


class ToDo:
    def __init__(self):
        self.todos = []
        self.memento = Memento()

    def add_goal(self, goal):
        self.todos.append(goal)
        self.memento.save_state(copy.deepcopy(self.todos))

    def show_goals(self, show_ended=True):
        for i, goal in enumerate(self.todos):
            if not show_ended and goal.startswith('!'):
                continue
            print(i, goal)

    def end_goal(self, num):
        self.todos[num] = '!' + self.todos[num]
        self.memento.save_state(copy.deepcopy(self.todos))

    def undo(self):
        self.memento.undo()
        self.todos = self.memento.read_state()

    def redo(self):
        self.memento.redo()
        self.todos = self.memento.read_state()