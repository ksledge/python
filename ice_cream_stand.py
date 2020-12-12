class Resturant():
    '''Class to define a resturant'''
    def __init__(self, name, cuisine_type):
        self.name = name.title()
        self.cuisine_type = cuisine_type
    
    def describe_resturant(self):
        msg = self.name.title() + " serves wonderful " + self.cuisine_type + "." 
        print('\n' + msg)

    def open_resturant(self):
        msg = self.name.title() + " is open. Come on in!"
        print( msg )
class IceCreamStand(Resturant):
    """ Class to define an Ice Cream Stand."""
    def __init__(self, name, cuisine_type= 'ice cream'):
        """Then initialize attributes specific to an ice cream stand."""        
        super().__init__(name, cuisine_type)
        self.flavors = []

    def show_flavors(self):
        """Display the flavors available."""
        print("\nWe have the following flavors available:")
        for flavor in self.flavors:
            print("- " + flavor.title())
            
jumbo = IceCreamStand('Jumbo Cones')
jumbo.flavors = ['vanilla', 'chocolate', 'black cherry', 'walnut', 'rocky road', 'pina colada']

jumbo.describe_resturant()
jumbo.show_flavors()


#bbq_palace = Resturant( "The BBQ Palace" , "barbeque")
#bbq_palace.describe_resturant()
#bbq_palace.open_resturant()

#pizza_king = Resturant("The Pizza King", "pizza")
#pizza_king.describe_resturant()
#pizza_king.open_resturant()

#chinese_kitchen = Resturant("The Chinese Kitchen", "chinese")
#chinese_kitchen.describe_resturant()
#chinese_kitchen.open_resturant()
