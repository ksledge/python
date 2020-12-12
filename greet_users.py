def greet_users(names):
    """ Function to greet list of users."""
# Loop of names in the list that prints out hello message.    
    for name in names:
        message = "Hello, " + name.title() + "!"
        print(message)

# Define list called usernames and pass that list to the function.
usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)