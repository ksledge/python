##############################################################
# Funtion that will accept an arbitrary number of arguments  #
#                                                            #   
##############################################################
def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print("\nMaking a " + str(size) + "'" + " pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping.title())
