# Default Values
'''When you use default values, any parameter with a default value needs to be listed
   after all the parameters that don’t have default values. This allows Python to continue
   interpreting positional arguments correctly.
'''
def pet_info( pet_name, animal_type= 'dog', ):
    """ Display info about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

# Print out function call results with default value field.
pet_info(pet_name= 'harry')

# To bypass the default value field with a more specific animal type.
pet_info(pet_name= 'harry', animal_type='hamster')