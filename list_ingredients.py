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

# Replace line below with component 3 in due course
scale_factor = eval(input("scale Factor "))

# Set up empty ingredients list
ingredients = []

# Loop to ask user to enter an ingredient
stop = ""
while stop != "xxx":

    amount = num_check("what is the amount for the ingredients? ")

    # stop loopin if exit code is typed and there are more
    # than 2 ingredients
    if amount == "xxx" and len(ingredients) >  1:
        break

    elif amount == "xxx" and len (ingredients) <2:
        print("you need at least two ingredients in the list.  "
              "please add more ingredients. ")
    # If exit code is not entered, add ingredient to list
    else:
        # Ask user for ingredient (via not blank function)
        get_ingredients = not_blank("please type in an ingredient name ")
        amount = float(amount) * scale_factor

        # Remove decimal point for whole numbers
        if amount % 1 == 0:
            amount = int(amount)
        elif amount * 10 % 1 == 0:
            amount = "{:.1f}".format(amount)
        else:
            amount = "{:.2f}".format(amount)

        ingredients.append("{} units {}".format(amount, get_ingredients))

# Output list
for items in ingredients:
