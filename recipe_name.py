# get the recipe name and make sure not blank 

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

# Main ruotine 

recipe_name = input("what is the recipe name: ")

print ("you are making {}". format(recipe_name))

recipe_serving = input("what the amount you will be wanting?")

print (" The amount you will be getting is {}". format(recip_ serving))