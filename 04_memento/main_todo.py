from todo import ToDo


my_list = ToDo()

my_list.add_goal("Do homework")
my_list.add_goal("Go for shopping")
my_list.add_goal("Go to pharmacy")

my_list.show_goals()
print("-----------")

my_list.end_goal(0)
my_list.show_goals(show_ended=False)
print("-----------")

my_list.undo()
my_list.show_goals(show_ended=False)
print("-----------")

my_list.redo()
my_list.show_goals(show_ended=False)