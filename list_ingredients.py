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

# Get ingredients list
# Assume all ingredients are in grams!!

# for each ingredient
get_ingredients = input,not_blank ("Ingredient Name: ")
ingredient_price = float (input("ingredient price: $"))
ingredient_amount = float(input ("ingredient amount bought: "))
recipe_amount = float(input("recipe amount needed:"))
cost = ingredient_price / ingredient_amount * recipe_amount
print("cost to make:")
print("{:.2f}".format(cost))

# while loop
questions = []

ingredients = ""
while ingredients != "xxx":
    ingredients = input("ingredient name:")
    if ingredients == "xxx":
            break

    price = input("ingredient price:$ ")
    amount = float(input("ingredient amount bought: "))
    recipe_amount = float(input("recipe amount needed:"))
    cost_to_make = ingredient_price / ingredient_amount * recipe_amount
    print("cost to make:")
    print("{:.2f}".format(cost_to_make))

    questions.append("{} ".format(ingredients, cost_to_make))
    print(questions)


