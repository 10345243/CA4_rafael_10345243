
from car import Car, ElectricCar, PetrolCar, DieselCar, HybridCar, Dealership

dealership = Dealership()
dealership.create_current_stock()

proceed = 'y'
while proceed == 'y':
    dealership.process_rental()
    proceed = raw_input('continue on this module? Y/N ').lower()
  
proceed = 'y'
while proceed == 'y':
    dealership.process_returnCar()
    proceed = raw_input('continue? Y/N').lower()

print 'Thank you'