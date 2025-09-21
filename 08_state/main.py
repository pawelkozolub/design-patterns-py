from phone import *

normal_state = NormalState()
plane_state = PlaneState()
silent_state = SilentState()
vibration_state = VibrationState()

phone = Phone()
phone.ring()

phone.set_state(plane_state)
phone.ring()

phone.set_state(silent_state)
phone.ring()

phone.set_state(vibration_state)
phone.ring()

phone.set_state(normal_state)
phone.ring()