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
                    response = float(input(question))

                    if response > 0:
                        return response
                    else:
                        print(error)

                except ValueError:
                    print(error)

# Main ruotine

recipe_name = not_blank("what is the recipe name: ")
print ("you are making {}". format(recipe_name,not_blank))

recipe_serving = num_check("what the amount you will be wanting?")
print ("The serving size you will be getting is {}". format(recipe_serving,num_check))