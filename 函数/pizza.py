# pizza model
def make_pizza(size, color, *toppings):
    print("Making a " + str(size) + "-size  " +
          color + " pizza with following toppings ")
    for topping in toppings:
        print("- " + topping)
