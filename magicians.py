def show_magicians(magician_names):
    """ Function to print names of magicians."""
    for magician in magicians:
        print(magician.title())
magicians = ['merlin', 'peter', 'paul', 'dave']
show_magicians(magicians)