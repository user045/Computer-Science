# Tuples

# Tuples are  an ordered immutable sequence. They look like ordered tuples in
# math (1, 5, 7, 11); ('a','x','c')

# Create an empty tuple
point = ()

# The comma distinguishes a tuple
point = (2) # the integer 2
point = (2, 3) # the tuple containing a single element 2
print(point)

# Concatenate Tuples
point = point + (3,)
print(point)
point = point + (-1, 4)
print(point)

#Tuple Unpacking
(x, y, z, w) = point = (2, 3, -1, 4)
print(f"x: {x}, y: {y}, z: {z}, w: {w}")

# Things the interpreter gets mad about
# x, y = point - Not enough variables (places) to store items in the tuple. 

# The proper way to ignore items in a tuple
(x, y, _, _) = point    # Use an underscore for the items you want to ignore
print(f"x: {x}, y: {y}")

# We can index it
print(point[2])

# Tuples are immutable, so we cannot change the value of an item in a tuple
# point[2] = 5 # This will raise an error

# Exchange Values
# Suppose we want to exchange the values in two variables
s = 5
t = 8

# With tuples
print(f"Before Swap - s: {s}, t: {t}")
(s, t) = (t, s)
print(f"After Swap - s: {s}, t: {t}")

# Without tuples - using a temporary variable
temp = s
s = t
t = temp

# Returning multiple items out of a function
my_scores = [88, 95, 70, 62, 99, 24, 74, 85]

def find_min_max(scores):
    '''
    Purpose: Find the minimum and maximum scores in a list of scores
    Parameters: scores - the numerical list we want the max / min of; list
    Return Values: max, min; float /int
    '''
    minimum = scores[0]
    maximum = scores[0]
    for item in scores:
        if item < minimum:
            minimum = item
        if item > maximum:
            maximum = item
    return (minimum, maximum)

min, max = find_min_max(my_scores)
print(f"minimum: {min}, maximum: {max}")

# Here's an Exercise for you

my_rocks = [('talc', 1), ('lead', 1.5), ('copper',3), ('nickel',4), ('silicon', 6.5), ('emerald', 7.5), ('boron', 9.5), ('diamond', 10)]

# The first element of the tuple is the mineral and the second is the rating of the mineral
# Soft - rating of 1-3
# Medium - rating of 3.1-5
# Hard - rating of 5.1-8
# Very Hard - rating of 8.1 - 10

def hardness(rocks):
    '''
    Purpose: to take a list of (mineral, hardness) and make a dictionary of hardness categories
    Parameters: rocks is a list of tuples of minerals and hardness ratings 
    Return Value: dictionary where the hardness categories are the keys and the values ae a list of minerals for that category.

    Example:
        hardness(my_rocks)
        {'soft': ['talc', 'lead', 'copper'], 'medium': ['nickel'], 'hard': ['silicon', 'emerald'], 'very hard': ['boron', 'diamond']}
    '''

    # Advantages of Tuples
    # Tuples use less space than lists
    # You can't change tuples by mistake
    # You can use tuples as dictionary keys
    # Function arguments are passed as tuples
    # Return more than one item out of function using a tuple