class Resturant():
    '''Class to define a resturant'''
    def __init__(self, name, cuisine_type):
        self.name = name.title()
        self.cuisine_type = cuisine_type
        self.number_served = 20
    
    def describe_resturant(self):
        msg = self.name.title() + " serves wonderful " + self.cuisine_type + "." 
        print('\n' + msg)

    def open_resturant(self):
        msg = self.name.title() + " is open. Come on in!"
        print( msg )

    def resturant(self):
        msg = "Number of customers served: " + str(self.number_served)
        print(msg)
    
    def set_number_served(self, number_served):
        """Method to set number of customers served."""
        self.number_served = number_served
    
    def increment_number_served(self, increment):
        """Method to increment number of customers served."""
        self.number_served += increment
        

bbq_palace = Resturant( "The BBQ Palace" , "barbeque")
bbq_palace.describe_resturant()
bbq_palace.open_resturant()
#bbq_palace.resturant()
bbq_palace.set_number_served(300)
print(f"Number served: {bbq_palace.number_served}")
bbq_palace.increment_number_served(300)
print(f"Number served today: {bbq_palace.number_served}")


#pizza_king = Resturant("The Pizza King", "pizza")
#pizza_king.describe_resturant()
#pizza_king.open_resturant()

#chinese_kitchen = Resturant("The Chinese Kitchen", "chinese")
#chinese_kitchen.describe_resturant()
#chinese_kitchen.open_resturant()