# Problem 1

"""
Write a function that takes in a Tuple of 4 values
This function should unpack the Tuple into 4 variables,
Then create two NEW tuples, with two variable values in each
Finally, create another new Tuple, with the other two Tuples nested inside of it
Return this final nested Tuple

Example Input: (1,2,3,4)
Example Output: ((1,2)(3,4))
"""


def the_tuplizer(initial_tuple):
    var_1, var_2, var_3, var_4 = initial_tuple
    new_tuple_1 = (var_1, var_2)
    new_tuple_2 = (var_3, var_4)
    final_tuple = (new_tuple_1, new_tuple_2)
    return final_tuple

# Problem 2


"""
Write a function that takes in a Tuple of Batting Averages
Convert to a List, sort highest to lowest, and return the highest value

Example Input: (.123, .301, .290, .313, .106)
Example Output: .313
"""


def highest_batting_average(batting_tuple):
    batting_list = list(batting_tuple)
    batting_list.sort()
    return batting_list[-1]


# Problem 3

"""
Write a function that takes in a string
The function should determine if every vowel is present in that string
If so, print "Congratulations, you passed the Vowel Test"
Otherwise print "Wrong! Try another string!"
HINT: A set of all vowels {'a','e','i','o','u'} will be helpful for this task!

Example Input: "Eunoia"
Example Output: "Congratulations, you passed the Vowel Test"

Example Input: "devCodeCamp"
Example Output: "Wrong! Try another string!"
"""


def check_for_vowels(input_string):
    input_string = input_string.lower()
    set_of_vowels = {"a", "e", "i", "o", "u"}
    count = 0
    for vowel in set_of_vowels:
        if vowel in input_string:
            count += 1
    if count == 5:
            print("Congratulations, you passed the Vowel Test")
    else:
        print("Wrong! Try another string!")


# Problem 4


"""
Write a function that takes in a list of numbers
The function should return a list of tuples,
where the FIRST value is the original number,
and the SECOND is the square of the original number


Example Input: [2,3,4]
Example Output: [(2,4),(3,9),(4,16)]

Example Input: [5,10]
Example Output: [(5,25),(10,100)]
"""


def make_tuple_squares(list_of_numbers):
    list_of_tuples = []
    for num in list_of_numbers:
        value = num * num
        tuple = (num, value)
        list_of_tuples.append(tuple)
    return list_of_tuples

# Problem 5


"""
Write a function that takes in a Tuple
Your function should remove the value from the END of the Tuple, and place it in the middle, then return that tuple
HINT: You will need to convert the Tuple to a different data structure to achieve this!

Example Input: (1, 3, 5, 7, 9, 1, 2)
Example Output: (1, 3, 5, 2, 7, 9, 1)
"""


def tuple_value_mover(tuple_to_shift):
    tuple_as_list = list(tuple_to_shift)
    variable_to_move = tuple_as_list.pop(-1)
    tuple_as_list.insert(int(len(tuple_as_list)/2), variable_to_move)
    shifted_tuple = tuple(tuple_as_list)
    return shifted_tuple
    



# Problem 6

"""
Write a function that takes in a list of Tuples
These Tuples will consist of a contact name (string) and a phone number (integer)
Convert this List of Tuples into a Dictionary, where the contact name is the key, and the phone number is the value
Return the dictionary

Example Input: [("Barry Benson", 608123456), ("Bob Belcher", 8088675309), ("Marty McFly", 7198883333), ("Stone Cold Steve Austin", 987654321), ("Jackie Daytona", 3512531122)]
Example Output: {'Barry Benson': 608123456, 'Bob Belcher': 8088675309, 'Marty McFly': 7198883333, 'Stone Cold Steve Austin': 987654321, 'Jackie Daytona': 3512531122}
"""


def tuple_list_dictionary_converter(list_of_tuples):
    new_dictionary = {}
    for tuple in list_of_tuples:
        new_dictionary[tuple[0]] = tuple[1]
    return new_dictionary
