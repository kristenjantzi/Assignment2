"""
Counter app
"""


while True:
    try:
        first_value = int(input("Please enter a starting value: ") or 0)
        if not first_value:
            print("You didn't enter a value. The default value is 0.")
        if first_value >= 0:
            print(f"You have entered a starting value of: {first_value}")
            break
    except ValueError:
        print("You didn't enter a valid number.")


while True:
    try:
        end_value = int(input("Please enter an end value: "))
        if not end_value:
            print("You must enter a value greater than 0!")
        if end_value >= 1:
            print(f"You have entered an end value of: {end_value}")
            break
    except ValueError:
        print("You didn't enter a valid number.")


while True:
    try:
        step_value = int(input("Please enter a value to step by: ") or 1)
        if not step_value:
            print("You didn't enter a value. The default value is 1.")
        if step_value >= 1:
            print(f"You have entered a step value of: {step_value}")
            break
    except ValueError:
        print("You didn't enter a valid number.")


print("Your numbers are: ")
counter_app = first_value
while counter_app <= end_value:
    print(counter_app)
    counter_app += step_value
