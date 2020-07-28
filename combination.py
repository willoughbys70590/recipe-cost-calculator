# Get ingredients list

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

# Main ruotine
recipe_name = not_blank("what is the recipe name: ")
print("you are making {}".format(recipe_name, not_blank))
recipe_serving = num_check("serving size: ")
print("The serving size you will be getting is {}".format(recipe_serving, num_check))
# Assume all ingredients are in grams!!

# for each ingredient
'''
get_ingredients = input,not_blank ("Ingredient Name: ")
ingredient_price = float (input("ingredient price: $"))
ingredient_amount = float(input ("ingredient amount bought: "))
recipe_amount = float(input("recipe amount needed:"))
cost_to_make = ingredient_price / ingredient_amount * recipe_amount
print("cost to make:")
print(get_ingredients,cost_to_make)
print("{:.2f}".format(cost_to_make,get_ingredients))
'''


# while loop
all_ingredients = []

ingredients = ""
while ingredients != "xxx":

    ingredient_details = []

    ingredients = input("ingredient name:")
    if ingredients == "xxx":
            break

    ingredient_price = float(input("ingredient price: $"))
    print ("amount must be in grams")
    ingredient_amount = float(input("ingredient amount bought: "))
    recipe_amount = float(input("recipe amount needed:"))
    cost_to_make = ingredient_price / ingredient_amount * recipe_amount
    print("cost to make:")
    print("{:.2f}".format(cost_to_make,ingredients))

    # add things to each row
    ingredient_details.append(ingredients)
    ingredient_details.append(cost_to_make)

    # add row to larger list
    all_ingredients.append(ingredient_details)

# questions.append(" ".format(ingredients,cost_to_make))

# print(all_ingredients)

# total_cost = cost + cost_to_make
print("****Total cost****")
total = 0
count = 0
for item in all_ingredients:
    total += all_ingredients[count][1]
    print("{} : ${:.2f}".format(all_ingredients[count][0], all_ingredients[count][1]))
    # print(all_ingredients[count][1])
    count +=1
print("{:.2f}".format(total))

per_serve = total / recipe_serving
print("****per serve:**** ")
print("{:.2f}".format(per_serve))
