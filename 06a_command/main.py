from switch import Switch
from flashlight import Flashlight
from flashlight_switcher import FlashlightSwitcher

my_flashlight = Flashlight()
my_switch = Switch()
my_flashlight_switcher = FlashlightSwitcher(my_flashlight, my_switch)

command = "on"
my_flashlight_switcher.toggle(command)

command = "off"
my_flashlight_switcher.toggle(command)

print("------")
print(my_switch.get_history())