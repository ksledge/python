def sandwich_items(*items):
    """ Function that will print out the items on a sandwich."""
    print("I'll make you a great sandwich: ")
    for item in items:
        print("  ...adding " + item + " to your sandwich.")
    print("Your sandwich is ready!\n")

sandwich_items('roast beef', 'cheddar cheese', 'lettuce', 'honey dijon')
sandwich_items('turkey', 'apple slices', 'honey mustard')
sandwich_items('peanut butter', 'strawberry jam')
