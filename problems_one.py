# Problem 1

"""
Write a function that takes in a List and returns a List with the original list values reversed

Example Input: [1, 2, 3, 4, 5] 
Example Output: [5, 4, 3, 2, 1]
"""


def reverse_list(list):
    counter = len(list)
    reversed_list = []
    while counter > 0:
        reversed_list.append(list[counter - 1])
        counter -= 1
    return reversed_list


# Problem 2

"""
Write a function that has two parameters.
The first parameter will be a list of numbers, the second parameter will be a number.
Iterate over the list & compare each value to the number parameter
If it is greater than the number parameter, add it to a new list
Return the new list

Example Input: [1, 2, 3, 4, 5], 3 
Example Output: [4, 5]
"""


def list_value_checker(list, number):
    new_list = []
    for num in list:
        if num > number:
            new_list.append(num)
    return(new_list)


# Problem 3

"""
Write a function that has two parameters: a list, and another list
Both lists that are passed in should contain the first names of people
Iterate over the lists comparing the values at each index from one list to the other. 
If there is a matching name in both lists, return that name from the function

Example Input: [“Nevin”, “David”, “Mike”], [“Brett”, “Mike”, “Dan"]
Example Output: "Mike"
"""


def list_value_comparison(list_one, list_two):
    matching_names = []
    for name in list_one:
        index = 0
        while index < len(list_two):
            if name == list_two[index]:
                matching_names.append(name)
            index += 1
    return matching_names

    
        


# Problem 4

"""
Write a function that takes in the following dictionary
and returns the value of the key "favorite_color"

person = {
    "name": "Timmy Thomas",
    "age": 5,
    "interests": {
        "favorite_book": "Where The Sidewalk Ends",
        "favorite_movie": "Star Wars",
        "favorite_color": "Red"
    }
}

Expected Output: "Red"
"""


def get_value_of_favorite_color(sample_dictionary):
    return sample_dictionary["interests"]["favorite_color"]

# Problem 5


"""
Problem 5 - Write a function that takes in the following dictionary and prints out every
key and value in a well-formatted print statement

address = {
	"street": "123 Sesame Street",
	"city": "Some Town",
	"state": "Some State",
	"zip_code": 12345
}

Example Output
"street - 123 Sesame Street"
"city - Some Town"
"state - Some State"
"zip_code - 12345"

# BONUS: "clean" the key names so they print in a more readable format:
# Example: "Zip Code - 12345"
"""


def dictionary_printer(dictionary):
    pass


# Problem 6

"""
Write a function that takes in a List of numbers
Return a dictionary where the key is the number
And the value is how frequently it appears in the List


Example Input: [1, 1, 2, 2, 2, 3]
Example Output: {"1": 2, "2": 3, "3": 1}
"""


def list_numbers_to_dictionary(list_of_numbers):
    pass
