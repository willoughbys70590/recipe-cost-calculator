# Not blank funtion
def not_blank(question):
    error = "your recipe name has numbers in it."

    valid = False
    while not valid:
        has_errors = ""
        response = input(question)

        # look at each character in string and if its a number, complain
        for letter in response:
            if letter.isdigit():
                has_errors = "yes"
                break

        if response == "":
            continue
        elif has_errors != "":
            print(error)
            continue
        else:
            return response

# Number checking (number must be more than 0)
def num_check(question):

            error = "please enter a number that is more than zero"

            valid = False
            while not valid:
                try:
                    response = int(input(question))

                    if response > 0:
                        return response
                    else:
                        print(error)

                except ValueError:
                    print(error)

                if ingredient_amount == "xxx" and len(get_ingredients) > 1:
                    break

                elif ingredient_amount == "xxx" and len(get_ingredients) < 2:
                    print("you need at least two ingredients in the list.  "
                          "please add more ingredients. ")
# Assume all ingredients are in grams!!

get_ingredients = input,not_blank("Ingredient Name:")
ingredient_price = float (input("ingredient price: $"))
ingredient_amount = float(input ("ingredient amount bought: "))
recipe_amount = float (input("recipe amount needed:"))

cost_to_make = ingredient_price / ingredient_amount * recipe_amount 
print ("cost to make:") 
print("{:.2f}".format(cost_to_make))

get_ingredients = input,not_blank("Ingredient Name:")
ingredient_price = float (input("ingredient price: $"))
ingredient_amount = float(input ("ingredient amount bought: "))
recipe_amount = float (input("recipe amount needed:"))
cost_to_make = ingredient_price / ingredient_amount * recipe_amount 
print ("cost to make:") 
print("{:.2f}".format(cost_to_make))
expense_list = ['pasta',3.80], ['butter',0.92], ['garlic',0.14 ], ['plain flour',0.04 ], ['whole milk', 1.43], ['cream', 2.35], ['parmesan cheese', 3.07], ['salt', 0.02], ['pepper', 0.18], ['chicken', 23] 

total =0

#add costs 
for item in expense_list:
  total += item[1]

average = total / len(expense_list)
print(average)
#output 
print(get_ingredients,cost_to_make)