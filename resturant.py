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

bbq_palace = Resturant( "The BBQ Palace" , "barbeque")
bbq_palace.describe_resturant()
bbq_palace.open_resturant()

pizza_king = Resturant("The Pizza King", "pizza")
pizza_king.describe_resturant()
pizza_king.open_resturant()

chinese_kitchen = Resturant("The Chinese Kitchen", "chinese")
chinese_kitchen.describe_resturant()
chinese_kitchen.open_resturant()




