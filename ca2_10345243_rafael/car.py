# Define a class for my car

class Car(object):
    # implement the car object.
    
    def __init__(self):
        self.__colour = ''
        self.__make = ''
        self.__mileage = 0
        self.engineSize = ''

    def getColour(self):
        return self.__colour

    def getMake(self):
        return self.__make

    def getMileage(self):
        return self.__mileage

    def setColour(self, colour):
        self.__colour = colour

    def setMake(self, make):
        self.__make = make

    def setMileage(self, mileage):
        self.__mileage = mileage

    def paint(self, colour):
        self.__colour = colour
        return self.__colour

    def move(self, distance):
        self.__mileage = self.__mileage + distance
        return self.__mileage
#creating types of cars
        
class ElectricCar(Car):
    
    def __init__(self):
        Car.__init__(self)
        self.__numberFuelCells = 1

    def getNumberFuelCells(self):
        return self.__numberFuelCells

    def setNumberFuelCells(self, value):
        self.__numberFuelCells = value

class PetrolCar(Car):

    def __init__(self):
        Car.__init__(self)
        self.__numberCylinders = 1

    def getNumberCylinders(self):
        return self.__numberCylinders

    def setNumberCylinders(self, value):
        self.__numberCylinders = value

class DieselCar(Car):

    def __init__(self):
        Car.__init__(self)
        self.__numberCylinders = 1

    def getNumberCylinders(self):
        return self.__numberCylinders

    def setNumberCylinders(self, value):
        self.__numberCylinders = value

class HybridCar(Car):

    def __init__(self):
        Car.__init__(self)
        self.__numberCylinders = 1
        self.__numberFuelCells = 1
        
    def getNumberCylinders(self):
        return self.__numberCylinders

    def setNumberCylinders(self, value):
        self.__numberCylinders = value
    
    def getNumberFuelCells(self):
        return self.__numberFuelCells

    def setNumberFuelCells(self, value):
        self.__numberFuelCells = value

#creating a car rental        
class Dealership(object):

    def __init__(self):
        self.electric_cars = []
        self.petrol_cars = []
        self.diesel_cars = []
        self.hybrid_cars = [] 

    def create_current_stock(self):
        for i in range(1,5):
           self.electric_cars.append(self.electric_cars)
        for i in range(1,21):
           self.petrol_cars.append(self.petrol_cars)
        for i in range(1,9):
           self.diesel_cars.append(self.diesel_cars)
        for i in range(1,9):
           self.hybrid_cars.append(self.hybrid_cars)        
        
    def stock_count(self):
        print 'Petrol cars in stock ' + str(len(self.petrol_cars))
        print 'Electric cars in stock ' + str(len(self.electric_cars))
        print 'Diesel cars in stock ' + str(len(self.diesel_cars))
        print 'Hidrid cars in stock ' + str(len(self.hybrid_cars))
        
        
        
    def rent(self, car_list, amount):
        if len(car_list) < amount:
            print 'Not enough cars in stock'
            return
        total = 0
        while total < amount:
           car_list.pop()
           total = total + 1
           
    def returnCar(self, car_list, amount, list_type):
        if list_type == 'p' and len(car_list) + amount > 20:
            print 'You can not return over limit'
            return
        elif list_type in ['d', 'h'] and len(car_list) + amount > 8:
            print 'You can not return over limit'
        elif list_type == 'e' and len(car_list) + amount > 4:
            print 'You can not return over limit' 
        total = 0
        while total < amount:
           car_list.append(amount)
           total = total + 1
		   
		  

    def process_rental(self):
        print "hello welcome to Augier Car Rental"
        answer = raw_input('would you like to RENT a car? Y/N ').lower()
        if answer == 'y':
            print "What type would you like?" 
            print "Type 'P' for pretrol, 'D' for diesel, 'E' for eletric, or 'h' for hybrid"
            answer = raw_input().lower()
            amount = int(raw_input('how many cars would you like to RENT? '))
            if answer == 'p':
                self.rent(self.petrol_cars, amount)
            elif answer == 'd':
                self.rent(self.diesel_cars, amount)
            elif answer == 'e':
                self.rent(self.eletric_cars, amount)
            elif answer == 'h':    
                    self.rent(self.hybrid_cars, amount)
            else:
                print 'Sorry not a valid choise'
        
        self.stock_count()
        
    def process_returnCar(self):
        print "hello welcome to Augier Car Rental"
        answer = raw_input('would you like to RETURN a car? Y/N ').lower()
        if answer == 'y':
            print "What type would you like?" 
            print "Type 'P' for pretrol, 'D' for diesel, 'E' for eletric, or 'h' for hybrid"
            answer = raw_input().lower()
            amount = int(raw_input('how many cars would you like to RETURN? '))
            if answer == 'p':
                self.returnCar(self.petrol_cars, amount, 'p')
            elif answer == 'd':
                self.returnCar(self.diesel_cars, amount, 'd')
            elif answer == 'e':
                self.returnCar(self.eletric_cars, amount, 'e')
            elif answer == 'h':    
                    self.returnCar(self.hybrid_cars, amount, 'h')
            else:
                print 'Sorry not a valid choise'
        
        self.stock_count()
        