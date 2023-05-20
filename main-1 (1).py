'''Basic Calulator by Micah Pierre-Louis'''

def calculator():
    while True: # loop indefinitely until user quits the program
        user_option = str(input('***Basic Calculator***\n\nThis calculator performs the four basic arithmetic operations.\n\nChoose an operation, or press q to quit: \n(A)dd\n(S)ubtract\n(M)ultiply\n(D)ivide\n(Q)uit\n')) # prompting user to choose an operation
        options = ['a', 's', 'm', 'd', 'q'] # valid options for user to choose from
        
        if user_option.lower() == 'q': # break the loop if user enters 'q'
            break
        
        user_num1 = int(input('Enter the first number:\t')) # prompting user to enter first number
        user_num2 = int(input('Enter the second number:\t')) # prompting user to enter second number

        if user_option.lower() == 'a': # addition branch
            print(f'{user_num1} + {user_num2} is {user_num1 + user_num2}')

        elif user_option.lower() == 's': # subtraction branch
            print(f'{user_num1} - {user_num2} is {user_num1 - user_num2}')

        elif user_option.lower() == 'm': # multiplication branch
            print(f'{user_num1} * {user_num2} is {user_num1 * user_num2}')

        elif user_option.lower() == 'd': # division branch
            if user_num2 == 0: # the user may not divide by zero 
                print('Error: Dividing by Zero')
            else:
                print(f'{user_num1} / {user_num2} is {user_num1 / user_num2:.2f}')
                
        elif user_option not in options: # the user may not input a key other than the ones in the options list
            print('Invalid input, try again.')
            continue # continue the loop       
    
calculator() # intializes the calculator

