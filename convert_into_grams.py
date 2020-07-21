import csv

#open file 
groceries = open('recipe_list.csv')

#read data
csv_groceries = csv.reader(groceries)

#create a dictionary 
food_dictionary = {}

# Add the data from the list into the dictionary

for row in csv_grceries:
  food_dictionary[row[0]] = row[1]

print(food_dictionary)

keep_going = ""
while keep_going == "":
  amount = eval(input("how much? "))
  amount = float(amount)

# get ingredient 
ingredient = input ("ingredient: ")

if ingredient in food_dictionary:
  mult_by = food_dictionary.get(ingredient)
  amount = amount * float(mult_by) / 250
  peint ("amount in g {} ".format(amount))
else:
  print("{} is unchanged".format (amount) 
  
  



  
