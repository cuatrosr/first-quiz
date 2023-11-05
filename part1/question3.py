################################################################################
#     ____                          __     _                          _____
#    / __ \  __  __  ___    _____  / /_   (_)  ____    ____          |__  /
#   / / / / / / / / / _ \  / ___/ / __/  / /  / __ \  / __ \          /_ <
#  / /_/ / / /_/ / /  __/ (__  ) / /_   / /  / /_/ / / / / /        ___/ /
#  \___\_\ \__,_/  \___/ /____/  \__/  /_/   \____/ /_/ /_/        /____/
#
#  Question 3
################################################################################
#
# Instructions:
# Make a Python class for a magical oven that can combine ingredients at
# different temperatures to craft special materials.
#
# The oven class should have the methods:
# - add(item) to add an oven to be combined
# - freeze() to freeze the ingredients
# - boil() to boil the ingredients
# - wait() to combine the ingredients with no change in temperature
# - get_output() to get the result
#
# You will need to change the `make_oven()` function to return a new instance
# of your oven.
#
# The `alchemy_combine()` function will use your oven. You can see the expected
# formulas and their outputs in the test file, `question3_test.py`.


class Oven:
    def __init__(self):
        self.recipe = [
            (["lead", "mercury"], {"boil": "gold", "freeze": None, "wait": None}),
            (["water", "air"], {"boil": None, "freeze": "snow", "wait": None}),
            (["cheese", "dough", "tomato"], {"boil": "pizza", "freeze": None, "wait": None})
        ]
        self.ingredients = []
        self.temperature = 0

    def add(self, item):
        self.ingredients.append(item)

    def freeze(self):
        self.temperature = -10

    def boil(self):
        self.temperature = 110

    def wait(self):
        pass

    def get_output(self):
        temperature = "boil" if self.temperature >= 100 else ("freeze" if self.temperature < 0 else "wait")
        return next(act[temperature] for ing, act in self.recipe if set(ing) == set(self.ingredients))


# This function should return an oven instance!
def make_oven():
    return Oven()


def alchemy_combine(oven, ingredients, temperature):
    for item in ingredients:
        oven.add(item)

    if temperature < 0:
        oven.freeze()
    elif temperature >= 100:
        oven.boil()
    else:
        oven.wait()

    return oven.get_output()
