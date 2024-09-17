# import functions
from functions import validate_and_execute, user_input_message          #best way
from functions import *         #better because no need to use module name with code for usage
import test as t                # refernce test as t now in code

while True:
    user_input = input(user_input_message)
    if user_input == "exit":
        print("Exiting the program. Goodbye!")
        break                                       # Exit the loop if the user enters 'exit'
    days_and_unit = user_input.split(":")
    print(days_and_unit)
    days_and_unit_dictionary = {"days": days_and_unit[0], "unit": days_and_unit[1]}
    validate_and_execute()
    print(days_and_unit_dictionary)
    print(type(days_and_unit_dictionary))
    validate_and_execute()
