'''
This program, as well as _Functions.py was created by Sebastian Deluca.
It is meant to ease some more difficult aspects of mathematics, such as
quadratic equations, 3x3 Matrix determinants, and whatnot. This program
will be added onto once I A. Learn more mathematics, and B. Learn how to
fix errors that may be present.
BEGIN - [2020.10.29]
'''

import SuperCalc_Functions as calc
import time

def w_s(times):
    for x in range(times):
        print('')

def wait_input():
    input('Press Enter to Continue')

def help_menu():  # A help menu to guide the user
    help_loop = True
    while help_loop:
        w_s(25)
        print(('What do you want help with?').center(150, ' '))
        print(('1. What can this do?').center(150, ' '))
        print(('2. Quadratic Equations').center(150, ' '))
        print(('3. Input').center(150, ' '))
        print(('4. Known Errors').center(150, ' '))
        print(('B/Q. Return to Main Menu').center(150, ' '))
        user_input = input('#: ')  # Get user input
        if user_input == '1':
            w_s(1)
            print(('The SuperCalculator, as I egotistically named it, is capable of doing basic mathematics, like addition,\n'
                  'subtraction, multiplication, and division. It can also calculate derivatives, inverses of 2x2 matrices, the\n'
                  'determinants of 3x3 matrices, and perform the quadratic formula, among other things. Each type of function\n'
                  'will tell you how to format your input. If the input is incorrect, the output will be. So enter them properly.').center(150, ' '))
            w_s(1)
            print(('Each menu tells you how to navigate it, so you shouldn\'t need much help beyond that.').center(150, ' '))
            wait_input()

        elif user_input == '2':
            w_s(24)
            print('')
            print(('If your Quadratic Equation output claims there was an error, it\'s because your square root is a negative. I currently do not remember how to calculate that.').center(150, ' '))
            print('It\'ll be fixed eventually!')
            wait_input()

        elif user_input == '3':
            w_s(25)
            print(('For every advanced calculation, separate your values by spaces. For example, for the derivative, enter \n'
                  '2x2 17x -5 to signify (2x^2 + 17x - 5). This format makes it easier to code for. For matrices, just \n'
                  'separate the values by spaces. \nThe matrix\n[1,2]\n[3,4]\n would be entered into the program as \' 1 2 3 4 \' \n'
                  'again, to simplify the recognition of values. This is re-iterated in each function.').center(150, ' '))
            wait_input()

        elif user_input == '4':
            w_s(25)
            print(('Here are Version 0.0.2\'s Known Errors:\n 1. Fraction Division will most likely produce incorrect ' +
                   'values. \nThis is due to how computers interpret repeating values.\n 2. The Quadratic Equation code' +
                    ' will tell you there is an input error if your Sq.Root is negative.').center(150,' '))
            wait_input()

        elif user_input.upper() == 'B' or user_input.upper() == 'Q':
            w_s(1)
            print('Returning to main menu.')
            help_loop = False
            w_s(25)
            main()

def main():
    run_loop = True
    while run_loop:
        w_s(25)
        print(('The Super-Calculator -- Coded by Sebastian Deluca').center(150,' '))
        print(('Build 0.0.2').center(150, ' '))
        w_s(1)
        print(('-Options-').center(150, ' '))
        print(('1/A: Addition').center(150, ' '))
        print(('2/S: Subtraction').center(150, ' '))
        print(('3/D: Divison').center(150, ' '))
        print(('4/M: Multiplication').center(150, ' '))
        print(('5/SR: Square-Rooting').center(150, ' '))
        print(('6/Q: Quadratic Equation').center(150, ' '))
        print(('7/I: 2x2 Matrix Inversion').center(150, ' '))
        print(('8/DT: 3x3 Matrix Determinant').center(150, ' '))
        print(('9/DR: Derivative').center(150, ' '))
        w_s(1)
        print(('10/H: Help').center(150, ' '))
        print(('11/QQ: Quit').center(150, ' '))
        w_s(1)
        user_input = input('#: ')  # Get choice
        if user_input == '1' or user_input.upper() == 'A':  # Addition
            add_loop = True
            while add_loop:
                w_s(1)
                print(('Enter your values with no spaces. (i.e \'2+2\')').center(150,' '))
                w_s(1)
                values = input().split('+')
                try:
                    mapping = map(int, values)
                    user_values = list(mapping)
                    sum = calc.addition(user_values)
                    print(sum)
                    w_s(1)
                    print('Would you like to continue addition? Enter \'Q\' to go back to the Main Menu.')
                    user_input = input()
                    if user_input.upper() != 'Q':
                        add_loop = True
                    else:
                        add_loop = False

                except ValueError:
                    w_s(1)
                    print('Your Input is invalid.')
                    time.sleep(1)

        elif user_input == '2' or user_input.upper() == 'S':
            sub_loop = True
            while sub_loop:
                w_s(1)
                print(('Enter your values with no spaces. (i.e \'2-2\')').center(150, ' '))
                w_s(1)
                values = input().split('-')
                try:
                    mapping = map(int, values)
                    user_values = list(mapping)
                    difference = calc.subtraction(user_values)
                    print(difference)
                    w_s(1)
                    print('Would you like to continue subtraction? Enter \'Q\' to go back to the Main Menu.')
                    user_input = input()
                    if user_input.upper() != 'Q':
                        sub_loop = True
                    else:
                        sub_loop = False

                except ValueError:
                    w_s(1)
                    print('Your Input is invalid.')
                    time.sleep(1)
                    
        elif user_input == '3' or user_input.upper() == 'D':
            div_loop = True
            while div_loop:
                w_s(1)
                print(('Please enter two values, separated by space. (i.e \' 4 2\')').center(150, ' '))
                try:
                    values = input().split(' ')
                    quotient = calc.division(int(values[0]), int(values[1]))
                    print(values[0] + ' / ' + values[1] + ' = ' + str(quotient))
                    w_s(1)
                    print('Would you like to continue division? Enter \'Q\' to go back to the Main Menu.')
                    user_input = input()
                    if user_input.upper() != 'Q':
                        div_loop = True
                    else:
                        div_loop = False
                except:
                    print('You have entered an invalid input.')
                    time.sleep(1)

        elif user_input == '4' or user_input.upper() == 'M':
            mult_loop = True
            while mult_loop:
                w_s(1)
                print(('Please enter two values, separated by space. (i.e \' 4 2\')').center(150, ' '))
                try:
                    values = input().split(' ')
                    product = calc.multiplication(int(values[0]), int(values[1]))
                    print(values[0] + ' x ' + values[1] + ' = ' + str(product))
                    w_s(1)
                    print('Would you like to continue multiplication? Enter \'Q\' to go back to the Main Menu.')
                    user_input = input()
                    if user_input.upper() != 'Q':
                        mult_loop = True
                    else:
                        mult_loop = False
                except:
                    print('You have entered an invalid input.')
                    time.sleep(1)

        elif user_input == '5' or user_input.upper() == 'SR':
            pass
        elif user_input == '6' or user_input.upper() == 'Q':
            pass
        elif user_input == '7' or user_input.upper() == 'I':
            pass
        elif user_input == '8' or user_input.upper() == 'DT':
            pass
        elif user_input == '10' or user_input.upper() == 'H':
            help_menu()
        elif user_input == '11' or user_input.upper() == 'QQ':
            w_s(1)
            print('Goodbye!')
            run_loop = False
        else:
            w_s(1)
            print('Input Invalid. Try Again.')
            time.sleep(1)

main()