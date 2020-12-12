# Modifying a list without using functions.
unprinted_designs = ['robot', 'iphone case', 'robot pendant', 'barbie']
completed_models = []

while unprinted_designs:
    current_design = unprinted_designs.pop()
    print("Printing model: " + current_design)
    completed_models.append(current_design)

# Display all the completed models.
print("\nThe following modes have been printed: ")
for completed_model in completed_models:
    print(completed_model)

