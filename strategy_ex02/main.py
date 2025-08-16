from transport_chooser import TransportChooser
from strategies import *


destination = (50, 50)

chooser = TransportChooser(destination, strategy=Plane())
chooser.use_strategy()


chooser1 = TransportChooser(destination)
chooser1.use_strategy()