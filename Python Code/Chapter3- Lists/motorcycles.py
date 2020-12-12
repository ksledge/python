motorcycles = []
#Build the List
motorcycles.append('honda')
motorcycles.append('suzuki')
motorcycles.append('yamaha')

#Insert items into the List
motorcycles.insert(0,'indian')
motorcycles.insert(3,'ducati')

#Pop Items from compiled list
first_owned = motorcycles.pop(0)
last_owned = motorcycles.pop()

#Remove Items from the List
motorcycles.remove('suzuki')

too_expensive = 'ducati'

#Print The List
print(motorcycles)

#Function to print statements built from the list
print(f"The first motorcycle I owned was an {first_owned.title()}.")
print(f"The last motorcycle I owned was a {last_owned.title()}.")
print(f"\nA {too_expensive.title()} is too expensive for me.")