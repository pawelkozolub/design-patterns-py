from receiver import Receiver
from command import Command
from caller import Caller

tool = Receiver()
cmd1 = Command(tool)
cmd2 = Command(tool)
caller = Caller()

caller.store_command(cmd1, "do something 1")
caller.store_command(cmd2, "do something 2")

caller.execute_commands()

caller.show_commands()
caller.show_history()