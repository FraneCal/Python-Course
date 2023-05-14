# A program that asks a user to enter an OIB - Personal identification number (min. 11 numbers),
# and then checks it as described on the following page:
# https://regos.hr/app/uploads/2018/07/KONTROLA-OIB-a.pdf


def OIB_control():
    global first_number, next_number
    # Get the user input and validate it
    while True:
        user_input = input('Enter an OIB you want to check: ')
        # If the values is different from 11 print out the message and continue the while loop
        if len(user_input) != 11:
            print('Input must be 11 digits long')
            continue

        # Check if the input only contains numbers
        try:
            int(user_input)
        # If the input contains any string that is not a number print out the message and continue
        # the while loop
        except ValueError:
            print('Input must consist only of numbers')
            continue

        # If the input is alright, break the while loop
        break

    # Convert the input to a list of integers
    input_list = [int(number) for number in user_input]
    remainder = []

    for index, number in enumerate(input_list[:10]):
        if index == 0:
            first_number = (number + 10) % 10
            # If the remainder is 0, overwrite it with value 10
            if first_number == 0:
                first_number = 10
            first_number = (first_number * 2) % 11

        else:
            if index == 1:
                next_number = (number + first_number) % 10
            else:
                next_number = (number + next_number) % 10
            # If the remainder is 0, overwrite it with value 10
            if next_number == 0:
                next_number = 10
            next_number = (next_number * 2) % 11
            remainder.append(next_number)

    if remainder[-1] == 1:
        #If the last remainder is 1, overwrite it with value 0
        control_number = 0
    else:
        #If the remainder is any other value do the following
        control_number = 11 - remainder[-1]

    #If the control number is the same as the last number in the input list OIB is valid
    if control_number == input_list[-1]:
        print('OIB is valid.')
    else:
        print('OIB is not valid.')


OIB_control()
