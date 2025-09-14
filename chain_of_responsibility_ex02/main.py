from event import Event
from window import Window
from dialog import Dialog

my_window = Window()
my_dialog = Dialog(parent=my_window)

event = Event("ok")
my_dialog.handle(event)

event = Event("cancel")
my_dialog.handle(event)

event = Event("send")
my_dialog.handle(event)

event = Event("close")
my_dialog.handle(event)

event = Event("solve")
my_dialog.handle(event)