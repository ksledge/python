# Keyword Arguments
''' When you use keyword arguments, be sure to use the exact names of the parameters in
    the function’s definition.
'''
def pet_info(animal_type, pet_name):
    """ Display info about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

pet_info(animal_type= 'hamster', pet_name= 'harry')

