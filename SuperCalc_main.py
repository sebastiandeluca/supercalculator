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

data_file = 'data\SuperCalc_userInfo'

def w_s(times):
    for x in range(times):
        print('')

def wait_input():
    input('Press Enter to Continue')

def help_menu(mode):  # A help menu to guide the user
    help_loop = True
    while help_loop:
        w_s(25)
        print(('What do you want help with?').center(150, ' '))
        print(('1. What can this do?').center(150, ' '))
        print(('2. Input').center(150, ' '))
        print(('3. Known Errors').center(150, ' '))
        print(('4. Menu Settings').center(150,' '))
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
            w_s(25)
            print(('For every advanced calculation, separate your values by spaces. For example, for the derivative, enter \n'
                  '2x2 17x -5 to signify (2x^2 + 17x - 5). This format makes it easier to code for. For matrices, just \n'
                  'separate the values by spaces. \nThe matrix\n[1,2]\n[3,4]\n would be entered into the program as \' 1 2 3 4 \' \n'
                  'again, to simplify the recognition of values. This is re-iterated in each function.').center(150, ' '))
            wait_input()

        elif user_input == '3':
            w_s(25)
            print(('Here are Version 0.0.2\'s Known Errors:\n 1. Fraction Division will most likely produce incorrect ' +
                   'values. \nThis is due to how computers interpret repeating values.\n2. The Determinant Calculator will misprint values as x0 rather than x + 0.\n But, it\'s only when variables are in the matrix.').center(150,' '))
            wait_input()

        elif user_input == '4':
            w_s(25)
            print(('Your menu mode is currently set to ' + mode.title() + '. Would you like to change it?').center(150, ' '))
            input_loop = True
            while input_loop:
                user_choice = input('Y/N:')
                if user_choice.upper() == 'Y':
                    print('Menu mode has been switched from ' + mode.title(), end=' ')
                    if mode == 'advanced':
                        mode = 'simple'
                        data_change = 'True'
                    elif mode == 'simple':
                        mode = 'advanced'
                        data_change = 'False'
                    print('to ' + mode.title())
                    w_s(1)
                    input_loop = False
                    update_settings(data_change)
                elif user_choice.upper() == 'N':
                    print(('Menu Mode has not been switched.').center(150, ' '))
                    w_s(1)
                    input_loop = False
                else:
                    w_s(1)
                    print(('You have entered an invalid input.').center(150, ' '))
                    time.sleep(1)
            wait_input()

            print(('Your settings have been saved.').center(150, ' '))
        elif user_input.upper() == 'B' or user_input.upper() == 'Q':
            w_s(1)
            print('Returning to main menu.')
            help_loop = False
            w_s(25)
            main(mode)

def main(mode):
    run_loop = True
    while run_loop:
        w_s(25)
        print(('The Super-Calculator -- Coded by Sebastian Deluca').center(150,' '))
        print(('Build 0.0.3').center(150, ' '))
        w_s(1)
        if mode == 'simple':
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
            print(('10/P: Pythagorean Theorem').center(150, ' '))
            w_s(1)
            print(('11/H: Help').center(150, ' '))
            print(('12/QQ: Quit').center(150, ' '))
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
                sq_loop = True
                while sq_loop:
                    w_s(1)
                    print(('Please enter the number you want the find the square root of. i.e \'4\'').center(150, ' '))
                    w_s(1)
                    user_input = input()
                    if user_input.isalpha():
                        w_s(1)
                        print('You have entered an invalid input.')
                        time.sleep(1)
                    else:
                        value = calc.square_root(int(user_input))
                        print('The square root of ' + user_input + ' is ' + str(value))
                        w_s(1)
                        print('Would you like to continue square rooting? Enter \'Q\' to go back to the Main Menu.')
                        user_input = input()
                        if user_input.upper() != 'Q':
                            sq_loop = True
                        else:
                            sq_loop = False

            elif user_input == '6' or user_input.upper() == 'Q':
                quad_loop = True
                while quad_loop:
                    w_s(1)
                    print(('Enter an Equation like so: \'2 2 -2\' is \'(2x^2+2x-2)\'').center(150, ' '))
                    user_input = input()
                    x_vals = calc.quadratic(user_input)
                    if x_vals == False:
                        print(('You have entered an invalid input.').center(150, ' '))
                        time.sleep(1)
                    else:
                        print((x_vals).center(150, ' '))
                        w_s(1)
                        print('Would you like to continue calculating roots? Enter \'Q\' to go back to the Main Menu.')
                        user_input = input()
                        if user_input.upper() != 'Q':
                            quad_loop = True
                        else:
                            quad_loop = False

            elif user_input == '7' or user_input.upper() == 'I':
                invert_loop = True
                while invert_loop:
                    w_s(1)
                    print(('Enter a 2x2 Matrix, like so: \'1 2 3 4\' would be \'[1,2,3,4]\'.').center(150, ' '))
                    print(('This will also give you the determinant, & will ignore extra numbers.').center(150, ' '))
                    user_input = input()
                    for i in user_input.split():

                        if i == '':
                            incorrect_input = True
                            break
                        try:
                            cast = int(i)
                            incorrect_input = False
                        except:
                            incorrect_input = True
                            w_s(1)
                            print(('You have entered an invalid input.').center(150, ' '))
                            time.sleep(1)
                            break
                    if incorrect_input == False:
                        try:
                            calc.matrix_inverter(user_input)
                        except ValueError:
                            print(('You have entered an invalid input.').center(150, ' '))
                        w_s(1)
                        print('Would you like to continue inverting 2x2 matrices? Enter \'Q\' to go back to the Main Menu.')
                        user_input = input()
                        if user_input.upper() != 'Q':
                            invert_loop = True
                        else:
                            invert_loop = False

            elif user_input == '8' or user_input.upper() == 'DT':
                determ_loop = True
                while determ_loop:
                    w_s(1)
                    print(('Enter 9 Integers, spaced apart. (I.e: \'1 2 3...\' is \'[1 2 3 ...]\')').center(150,' '))
                    print(('NOTE: First 3 values are top row, next 3 are middle, last 3 are bottom row.').center(150, ' '))
                    print(('ALSO: Any strings entered will be considered as variables.').center(150, ' '))
                    user_input = input()
                    calc.determinant_calculator(user_input)
                    w_s(1)
                    print('Would you like to continue calculating 3x3 matrix determinants? Enter \'Q\' to go back to the Main Menu.')
                    user_input = input()
                    if user_input.upper() != 'Q':
                        determ_loop = True
                    else:
                        determ_loop = False

            elif user_input == '9' or user_input.upper() == 'DR':  # Finds derivative
                deriv_loop = True
                while deriv_loop:
                    w_s(1)
                    print(('Enter a polynomial: (i.e \'2x2 +3x -2\' is \'2x^2 + 3x - 2\')').center(150, ' '))
                    user_input = input()
                    calc.derivative_finder(user_input)
                    w_s(1)
                    print(
                        'Would you like to continue finding derivatives? Enter \'Q\' to go back to the Main Menu.')
                    user_input = input()
                    if user_input.upper() != 'Q':
                        deriv_loop = True
                    else:
                        deriv_loop = False

            elif user_input == '10' or user_input == 'P':  # Calculates pytagorean
                pytha_loop = True
                while pytha_loop:
                    print(('You need 3 values: a,b, and c').center(150, ' '))
                    print(('For your unknown value, enter \'x\'.').center(150, ' '))
                    user_a = input('a: ')
                    user_b = input('b: ')
                    user_c = input('c: ')
                    calc.pythagorean_theorem(user_a,user_b,user_c)
                    w_s(1)
                    print('Would you like to continue calculating the Pythagorean Theorem? Enter \'Q\' to go back to the Main Menu.')
                    user_input = input()
                    if user_input.upper() != 'Q':
                        pytha_loop = True
                    else:
                        pytha_loop = False

            elif user_input == '11' or user_input.upper() == 'H':
                help_menu(mode)
            elif user_input == '12' or user_input.upper() == 'QQ':
                w_s(1)
                print('Goodbye!')
                run_loop = False
            else:
                w_s(1)
                print('Input Invalid. Try Again.')
                time.sleep(1)

        elif mode == 'advanced':  # User has advanced menu
            print((' - Select an Option -').center(150, ' '))
            print(('Enter \'0\' or \'SMP\' for Simple Arithmetic Options').center(150, ' '))
            w_s(1)
            print(('1/Q: Quadratic Equation').center(150, ' '))
            print(('2/I: 2x2 Matrix Inversion').center(150, ' '))
            print(('3/DT: 3x3 Matrix Determinant').center(150, ' '))
            print(('4/DR: Derivative').center(150, ' '))
            print(('5/P: Pythagorean Theorem').center(150, ' '))
            w_s(1)
            print(('6/H: Help / Options').center(150, ' '))
            print(('7/QQ: Quit').center(150, ' '))
            user_input = input('#: ')
            if user_input == '1' or user_input.upper() == 'Q':
                quad_loop = True
                while quad_loop:
                    w_s(1)
                    print(('Enter an Equation like so: \'2 2 -2\' is \'(2x^2+2x-2)\'').center(150, ' '))
                    user_input = input()
                    x_vals = calc.quadratic(user_input)
                    if x_vals == False:
                        print(('You have entered an invalid input.').center(150, ' '))
                        time.sleep(1)
                    else:
                        print((x_vals).center(150, ' '))
                        w_s(1)
                        print('Would you like to continue calculating roots? Enter \'Q\' to go back to the Main Menu.')
                        user_input = input()
                        if user_input.upper() != 'Q':
                            quad_loop = True
                        else:
                            quad_loop = False

            elif user_input == '2' or user_input.upper() == 'I':
                invert_loop = True
                while invert_loop:
                    w_s(1)
                    print(('Enter a 2x2 Matrix, like so: \'1 2 3 4\' would be \'[1,2,3,4]\'.').center(150, ' '))
                    print(('This will also give you the determinant, & will ignore extra numbers.').center(150, ' '))
                    user_input = input()
                    for i in user_input.split():

                        if i == '':
                            incorrect_input = True
                            break
                        try:
                            cast = int(i)
                            incorrect_input = False
                        except:
                            incorrect_input = True
                            w_s(1)
                            print(('You have entered an invalid input.').center(150, ' '))
                            time.sleep(1)
                            break
                    if incorrect_input == False:
                        try:
                            calc.matrix_inverter(user_input)
                        except ValueError:
                            print(('You have entered an invalid input.').center(150, ' '))
                        w_s(1)
                        print(
                            'Would you like to continue inverting 2x2 matrices? Enter \'Q\' to go back to the Main Menu.')
                        user_input = input()
                        if user_input.upper() != 'Q':
                            invert_loop = True
                        else:
                            invert_loop = False

            elif user_input == '3' or user_input.upper() == 'DT':
                determ_loop = True
                while determ_loop:
                    w_s(1)
                    print(('Enter 9 Integers, spaced apart. (I.e: \'1 2 3...\' is \'[1 2 3 ...]\')').center(150, ' '))
                    print(('NOTE: First 3 values are top row, next 3 are middle, last 3 are bottom row.').center(150, ' '))
                    print(('ALSO: Any strings entered will be considered as variables.').center(150, ' '))
                    user_input = input()
                    calc.determinant_calculator(user_input)
                    w_s(1)
                    print(
                        'Would you like to continue calculating 3x3 matrix determinants? Enter \'Q\' to go back to the Main Menu.')
                    user_input = input()
                    if user_input.upper() != 'Q':
                        determ_loop = True
                    else:
                        determ_loop = False

            elif user_input == '4' or user_input.upper() == 'DR':  # Finds derivative
                deriv_loop = True
                while deriv_loop:
                    w_s(1)
                    print(('Enter a polynomial: (i.e \'2x2 +3x -2\' is \'2x^2 + 3x - 2\')').center(150, ' '))
                    user_input = input()
                    calc.derivative_finder(user_input)
                    w_s(1)
                    print(
                        'Would you like to continue finding derivatives? Enter \'Q\' to go back to the Main Menu.')
                    user_input = input()
                    if user_input.upper() != 'Q':
                        deriv_loop = True
                    else:
                        deriv_loop = False

            elif user_input == '5' or user_input == 'P':  # Calculates pytagorean
                pytha_loop = True
                while pytha_loop:
                    print(('You need 3 values: a,b, and c').center(150, ' '))
                    print(('For your unknown value, enter \'x\'.').center(150, ' '))
                    user_a = input('a: ')
                    user_b = input('b: ')
                    user_c = input('c: ')
                    calc.pythagorean_theorem(user_a, user_b, user_c)
                    w_s(1)
                    print(
                        'Would you like to continue calculating the Pythagorean Theorem? Enter \'Q\' to go back to the Main Menu.')
                    user_input = input()
                    if user_input.upper() != 'Q':
                        pytha_loop = True
                    else:
                        pytha_loop = False

            elif user_input == '6' or user_input.upper() == 'H':
                help_menu(mode)
            elif user_input == '7' or user_input.upper() == 'QQ':
                w_s(1)
                print('Goodbye!')
                run_loop = False

            elif user_input == '0' or user_input.upper() == 'SMP':  # Simple math
                simple_screen = True
                while simple_screen:
                    print(('- Simple Arithmetic Options-').center(150, ' '))
                    w_s(1)
                    print(('1/A: Addition').center(150, ' '))
                    print(('2/S: Subtraction').center(150, ' '))
                    print(('3/D: Divison').center(150, ' '))
                    print(('4/M: Multiplication').center(150, ' '))
                    print(('5/SR: Square-Rooting').center(150, ' '))
                    w_s(1)
                    print(('6/B: Go Back').center(150,' '))
                    user_input = input('#: ')  # Get choice
                    if user_input == '1' or user_input.upper() == 'A':  # Addition
                        add_loop = True
                        while add_loop:
                            w_s(1)
                            print(('Enter your values with no spaces. (i.e \'2+2\')').center(150, ' '))
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
                        sq_loop = True
                        while sq_loop:
                            w_s(1)
                            print(('Please enter the number you want the find the square root of. i.e \'4\'').center(150,
                                                                                                                     ' '))
                            w_s(1)
                            user_input = input()
                            if user_input.isalpha():
                                w_s(1)
                                print('You have entered an invalid input.')
                                time.sleep(1)
                            else:
                                value = calc.square_root(int(user_input))
                                print('The square root of ' + user_input + ' is ' + str(value))
                                w_s(1)
                                print('Would you like to continue square rooting? Enter \'Q\' to go back to the Main Menu.')
                                user_input = input()
                                if user_input.upper() != 'Q':
                                    sq_loop = True
                                else:
                                    sq_loop = False

                    elif user_input == '6' or user_input.upper() == 'B':  # Go back
                        simple_screen = False

            else:
                w_s(1)
                print('Input Invalid. Try Again.')
                time.sleep(1)


def data_check():  # Checks userInfo for settings
    global data_file
    settings = open(data_file, 'r')
    for line in settings:
        if 'first_open' in line[:11]:  # Check if first open
            if 'True' in line[11:]:
                menu_settings()
                data_check()
            else:
                pass
        elif 'simple_menu' in line[:12]:
            if 'True' in line[12:]:
                menu_mode = 'simple'
            elif 'False' in line[12:]:
                menu_mode = 'advanced'
    settings.close()  # Save / Prevent corruption
    return menu_mode


def menu_settings():  # Options
    global data_file
    settings = open(data_file, 'w')
    settings.write('first_open = False\n')
    w_s(1)
    print(('Welcome to the SuperCalculator. Would you prefer a Simple Menu, or an Advanced Menu?').center(150, ' '))
    print(('For Advanced, Enter \'A\'. For Simple, enter anything else.').center(150, ' '))
    user_choice = input()
    if user_choice.upper() == 'A':  # Advanced Menu
        settings.write('simple_menu = False\n')
    else:
        settings.write('simple_menu = True\n')
    w_s(1)
    print(('Your settings have been saved. Your menu mode can be changed from the Options menu at any time.').center(150, ' '))
    settings.close()


def update_settings(newmode):  # Updates the userInfo file
    global data_file
    settings = open(data_file, 'w')
    settings.write('first_open = False\n')
    settings.write('simple_menu = ' + newmode + '\n')
    settings.close()


menu_mode = data_check()
main(menu_mode)
