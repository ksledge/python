class Car():
    """A Simple attempt to represent a car."""
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 15000
    
    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's milage."""
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        """Set the odometer reading to the given value.
           Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
           self.odometer_reading = mileage
        else:
           print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles
class Battery():
    """ A simple attempt to model a batter for an electic car."""
    def __init__(self, battery_size=60):
        """Initilize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def get_range(self):
        """Print a statement about the range the battery provides."""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)

#    def upgrade_battery(self):
#        """Check battery size and set capacity to 85."""
#        if self.battery_size == 60:
#            self.battery_size = 85
#            print("Upgraded the battery to 85 kWh.")
#        else:
#            print("The battery is already upgraded.")

    
             

class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""
    def __init__(self, make, model, year):
        """Initialize attributes of the parent class.
           Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery = Battery()
    

print("Make an electric car, and check the battery:")
my_tesla = ElectricCar('tesla', 'model s', 2016)
#print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
#my_tesla.battery.get_range()
print("\nUpgrade the battery, and check it again:")
my_tesla.battery.upgrade_battery()
my_tesla.battery.describe_battery()

print("\nTry upgrading the battery a second time:")
my_tesla.battery.upgrade_battery()
my_tesla.battery.describe_battery()

