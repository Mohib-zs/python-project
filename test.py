import os
import logging

greetings = "Hello there"           #Global Variable


def formula_calculations(a,b):             #def to define function, values in paranthesis are parameters
    formula_1       = "whole square formula"      #Local Variable 1
    formula_2       = "square formula"            # Local Variable 2
    whole_sqaure    = f"{greetings}, This is an example of {formula_1}\n{(a+b)*(a+b)}"
    sqaure          = f"{greetings}, This is an example of {formula_2}\n{(a*a)-(b*b)}"
    # condition_check = a > 0 and b > 0
    # print(type(condition_check))                    #type function is used to see data type of command/function being executed
    # print(a > 0 and b > 0)

    if a < 0 or b < 0:
        return "Please enter positive integers"
    elif a == 0 and b == 0:                             # '=' is used for assigning values while '==' is used for checking equality of values
        return "Please enter a value greater than 0 for atleast one input"
    else:
        return  f"{whole_sqaure}\n{sqaure}"


# input_1 = input("Enter the first integer value\n")            #limiting the input to only an integer, could also int(input_1) in the next line, such is called casting
# input_2 = input("Enter the second integer value\n")   


def validate_and_print(input_1, input_2):
    if input_1.isdigit() and input_2.isdigit():
        input_1_data    = int(input_1)
        input_2_data    = int(input_2)
        my_calculations = formula_calculations(input_1_data, input_2_data)
        print(my_calculations)
    else:
        print("You've entered an invalid value type")


my_list = ["Monday", "Tuesday", "Wednesday"]
my_set  = {"Monday", "Tuesday", "Wednesday"}
my_dictionary = {"Monday": 1, "Tuesday": 2, "Wednesday": 3, "Friday": "Holy"}

print(my_list)
my_list.append("Thursday")
print(my_list[3])
my_list.remove("Tuesday")

for element in my_set:
    print(element)
my_set.add("Friday")
print(my_set)
my_set.remove("Wednesday")

print(my_dictionary)
print(my_dictionary["Tuesday"])

print(os.name)
logger = logging.getLogger("MAIN")
logger.error("Error happened in the app")
