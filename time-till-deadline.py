from datetime import datetime

user_input = input("Enter your goal with a deadline separated by colon\n")
input_list = user_input.split(':')

goal     = input_list[0]
deadline = input_list[1]

deadline_date   = datetime.strptime(deadline, "%d.%m.%Y")
today_date      = datetime.today()
result_date     = deadline_date - today_date

print(f"Your time to {goal} is {int(result_date.total_seconds() /60 /60)} hours")
