import unittest

from car import Car, ElectricCar, PetrolCar, DieselCar, HybridCar, Dealership

# test the car functionality
class TestCar(unittest.TestCase):

    def test_car_mileage(self):
        self.car = Car()
        self.assertEqual(0, self.car.getMileage())
        self.car.move(15)
        self.assertEqual(15, self.car.getMileage())
        self.car.setMileage(45)
        self.assertEqual(45, self.car.getMileage())

    def test_car_make(self):
        self.car = Car()
        self.assertEqual('', self.car.getMake())
        self.car.setMake('Ferrari')
        self.assertEqual('Ferrari', self.car.getMake())

    def test_car_colour(self):
        self.car = Car()
        self.assertEqual('', self.car.getColour())
        self.car.paint('red')
        self.assertEqual('red', self.car.getColour())
        self.car.setColour('yellow')
        self.assertEqual('yellow', self.car.getColour())

    def test_car_engine_size(self):
        self.car = Car()
        self.assertEqual('', self.car.engineSize)
        self.car.engineSize = '2.0tdi'
        self.assertEqual('2.0tdi', self.car.engineSize)

    def test_electric_car_fuel_cells(self):
		electric_car = ElectricCar()
		self.assertEqual(1, electric_car.getNumberFuelCells())
		electric_car.setNumberFuelCells(4)
		self.assertEqual(4, electric_car.getNumberFuelCells())

    def test_diesel_car_fuel_cylinders(self):
		diesel_car = DieselCar()
		self.assertEqual(1, diesel_car.getNumberCylinders())
		diesel_car.setNumberCylinders(4)
		self.assertEqual(4, diesel_car.getNumberCylinders())
    
    def test_petrol_car_cylinders(self):
		petrol_car = PetrolCar()
		self.assertEqual(1, petrol_car.getNumberCylinders())
		petrol_car.setNumberCylinders(4)
		self.assertEqual(4, petrol_car.getNumberCylinders())
       
    def test_hybrid_car_cylinders(self):
		hybrid_car = HybridCar()
		self.assertEqual(1, hybrid_car.getNumberCylinders())
		hybrid_car.setNumberCylinders(4)
		self.assertEqual(4, hybrid_car.getNumberCylinders())
    
    def test_hybrid_car_fuel_cells(self):    
        hybrid_car = HybridCar()
        self.assertEqual(1, hybrid_car.getNumberFuelCells())
        hybrid_car.setNumberFuelCells(4)
        self.assertEqual(4, hybrid_car.getNumberFuelCells())
        
        
    def test_rent(self): 
        dealership = Dealership()
        dealership.create_current_stock()
        self.assertEqual(20, len(dealership.petrol_cars))
        dealership.rent(dealership.petrol_cars, 5)
        self.assertEqual(15, len(dealership.petrol_cars))

        

        
        
   
if __name__ == '__main__':
    unittest.main()
