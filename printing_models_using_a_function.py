def print_models(unprinted, completed):
    ''' Function to iterate thru list and print designs.'''
    while unprinted:
        current_design = unprinted.pop()
        print("Printing model: " + current_design)
        completed.append(current_design)

def show_completed(completed):
    """Print all the completed models."""
    print("\nThe following models have been printed: ")
    for complete in completed:
        print(complete)

unprinted = ['iphone case', 'robot pendant', 'dodecahedron']
completed = []

print_models(unprinted [:], completed)
show_completed(completed)

print(unprinted)
print(completed)
