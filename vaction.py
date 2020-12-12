responses = {}

# Set a flag to indicate that polling is active.
polling_active = True

while polling_active:
    # Prompt for the name and response.
    name = input("\nWhat is your name? ")
    response= input("Which vacation spot would you like to visit someday? ")

    # Store response in the dictionary.
    responses[name] = response

    # Find out if anyone else is going to take the poll.
    repeat = input("Would you like to let another person respond? (Y / N ) ")
    if repeat == 'N':
        polling_active = False
    if repeat == 'n':
        polling_active = False

# Polling is complete. Print out the results.
print("\n--- Poll Results ---")
for name, response in responses.items():
    print( name + " would like to visit " + response + ".")