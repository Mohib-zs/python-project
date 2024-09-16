greetings = "Hello there"           #Global Variable


def formula_calculations(a,b):                      #def to define function, values in paranthesis are parameters
    formula_1       = "whole square formula"        #Local Variable 1
    formula_2       = "square formula"              # Local Variable 2
    whole_sqaure    = f"{greetings}, This is an example of {formula_1}\n{(a+b)*(a+b)}"
    sqaure          = f"{greetings}, This is an example of {formula_2}\n{(a*a)-(b*b)}"
    # condition_check = a > 0 and b > 0
    # print(type(condition_check))                    #type function is used to see data type of command/function being executed
    # print(a > 0 and b > 0)

    if a < 0 or b < 0:
        return "Please enter positive integers"
    elif a == 0 and b == 0:                                                 # '=' is used for assigning values while '==' is used for checking equality of values
        return "Please enter a value greater than 0 for atleast one input"
    else:
        return  f"{whole_sqaure}\n{sqaure}"


def get_input(prompt):
    user_input = input(prompt)
    list_input = user_input.split(':')
    dictionary_input = {"input 1": list_input[0], "input 2": list_input[1]}
    if user_input.lower() == "exit":
        return "exit"
    try:
        return [int(i) for i in set(list_input)]
    except ValueError:
        print("Invalid input.")
        return []


while True:
    input_list = get_input("Enter a list of atleast two integers separated by commas, or type 'exit' to quit\n")             #limiting the input to only an integer, could also int(input_1) in the next line, such is called casting
    print(type(set(input_list)))
    print(type(input_list))
    print(set(input_list))
    print(input_list)

    if input_list == "exit":
        print("Exiting the program.")
        break

    len(input_list) >= 2                        # input list length must be equal or greater than 2
    for i in range(0, len(input_list) - 1, 2):  # 0 is the starting index range, len(input_list) is the ending index range with -1 if user inputs odd length input list, the last input would get skipped, 2 means taking pairs/steps of two elements at a time
        a = input_list[i]
        b = input_list[i+1]
        my_calculations = formula_calculations(a, b)
        print(my_calculations)


