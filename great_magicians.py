def show_magicians(magician_names):
    """ Function to print names of magicians."""
    for magician in magicians:
        print(magician.title())

def make_great(magician_names):
    """Print out "The Great" in front of magician name."""
    great_magicians = []
    while magicians:
        magician = magicians.pop()
        great_magician = magician + ' the Great'
        great_magicians.append(great_magician)
    
    for great_magician in great_magicians:
        magicians.append(great_magician)


magicians = ['merlin', 'peter', 'paul', 'dave']
show_magicians(magicians)

print("\n")
make_great(magicians)
show_magicians(magicians)
g