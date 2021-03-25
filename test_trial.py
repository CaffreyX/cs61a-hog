from dice import six_sided, four_sided, make_test_dice
def roll_dice(num_rolls, dice=six_sided):
    """Simulate rolling the DICE exactly NUM_ROLLS > 0 times. Return the sum of
    the outcomes unless any of the outcomes is 1. In that case, return 1.

    num_rolls:  The number of dice rolls that will be made.
    dice:       A function that simulates a single dice roll outcome.
    >>> roll_dice(3,dice=make_test_dice(2,3,4))
    9
    """
    # These assert statements ensure that num_rolls is a positive integer.
    assert type(num_rolls) == int, 'num_rolls must be an integer.'
    assert num_rolls > 0, 'Must roll at least once.'
    # BEGIN PROBLEM 1
    "*** YOUR CODE HERE ***"
    num = 0
    total = 0
    One = False
    while num < num_rolls:
         score = dice()
         print(score)
         total += score
         num += 1
         if score == 1:
            One = True
    if One == True:
        return 1
    else:
        return total
def make_averaged(original_function, trials_count=1000):
    """Return a function that returns the average value of ORIGINAL_FUNCTION
    when called.

    To implement this function, you will have to use *args syntax, a new Python
    feature introduced in this project.  See the project description.

    >>> dice = make_test_dice(4, 1, 5)
    >>> averaged_dice = make_averaged(roll_dice, 1000)
    >>> averaged_dice(1, dice)
    3.0
    """
    # BEGIN PROBLEM 8
    "*** YOUR CODE HERE ***"
    def new_func(*args):
        total,count = 0,0
        while count < trials_count:
            total += original_function(*args)
            count += 1
        return total / trials_count
    return new_func