import problems_one
import problems_two

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

string = input("Give me a word that uses all the vowels: ")
problems_two.check_for_vowels(string)