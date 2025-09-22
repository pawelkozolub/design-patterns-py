from car import Car

car1 = Car("Model 3", "gasoline")
car2 = Car("Model 6", "diesel")
car3 = Car("Model 4", "electric")

visitor1 = "Adam"
visitor2 = "Jeff"
visitor3 = "Anna"
visitor4 = "Scot"

print(visitor1)
car1.take_a_look(visitor1)
car1.request_additional_information()
car1.test_drive(visitor1)

print(visitor2)
car1.take_a_look(visitor2)
car2.take_a_look(visitor2)
car3.take_a_look(visitor2)

print(visitor3)
car2.take_a_look(visitor3)
car1.take_a_look(visitor3)
car3.take_a_look(visitor3)
car2.test_drive(visitor3)
car2.test_drive(visitor3)

print(visitor4)
car3.take_a_look(visitor4)
car3.request_additional_information()