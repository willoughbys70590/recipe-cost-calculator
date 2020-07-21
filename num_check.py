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
