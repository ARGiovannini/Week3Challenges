import problems_one
import problems_two
import problems_three

# to_reverse = [1, 2, 3, 4, 5, 6]
# result = problems_one.reverse_list(to_reverse)
# print(result)

# list_of_numbers = [1, 2, 3, 4, 5, 6, 7, 8]
# min_number = 4
# result = problems_one.list_value_checker(list_of_numbers, min_number)
# print(result)

# list_of_names = ["Harry", "Larry", "Curly", "Mo"]
# another_list_of_names = ["Sue", "Larry", "Craig", "Mo"]
# result = problems_one.list_value_comparison(list_of_names, another_list_of_names)
# print(f"{result} are in both lists")

# person = {
#     "name": "Timmy Thomas",
#     "age": 5,
#     "interests": {
#         "favorite_book": "Where The Sidewalk Ends",
#         "favorite_movie": "Star Wars",
#         "favorite_color": "Red"
#     }
# }
# fav_color = problems_one.get_value_of_favorite_color(person)
# print(f"{person['name']}'s favorite color is {fav_color}")

# address = {
# 	"street": "123 Sesame Street",
# 	"city": "Some Town",
# 	"state": "Some State",
# 	"zip_code": 12345
# }
# problems_one.dictionary_printer(address)

# list_of_numbers = [1, 2, 4, 1, 5, 2, 1, 5, 6, 7, 8, 3, 8, 9, 10, 10, 12, 1, 11]
# dictionary_of_numbers = problems_one.list_numbers_to_dictionary(list_of_numbers)
# print(dictionary_of_numbers)

# tuple_example = (1, 2 , 3, 4)
# output = problems_two.the_tuplizer(tuple_example)
# print(output)

# batting_averages = (.123, .301, .290, .313, .106)
# problems_two.highest_batting_average(batting_averages)

# string = input("Give me a word that uses all the vowels: ")
# problems_two.check_for_vowels(string)

# list_to_square = [1, 2, 3, 4, 5, 6, 7]
# tuple_squares = problems_two.make_tuple_squares(list_to_square)
# print(tuple_squares)

# tuple_input = (1, 3, 5, 7, 9, 1, 2)
# tuple_return = problems_two.tuple_value_mover(tuple_input)
# print(tuple_return)

# list_of_tuples = [("Barry Benson", 608123456), ("Bob Belcher", 8088675309), ("Marty McFly", 7198883333), ("Stone Cold Steve Austin", 987654321), ("Jackie Daytona", 3512531122)]
# result = problems_two.tuple_list_dictionary_converter(list_of_tuples)
# print(result)

# number_to_check = input("Give me a positive integer. Lets find out if it is happy: ")
# problems_three.happy_number_checker(number_to_check)

# problems_three.print_prime_numbers()

fibonacci_start = int(input("Input a number to make a fibonacci sequence with: "))
length_of_sequence = int(input("How long would you like your sequence to be? "))
problems_three.fibonacci(fibonacci_start, length_of_sequence)