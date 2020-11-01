'''
Created by Sebastian Deluca
CHECK MAIN.PY for desc.

ADDITIONS:
2X2 DETERMINANT CALCULATOR


FIXES NEEDED:


'''

from fractions import Fraction
from math import *


def addition(vals):  # Add all the value in the list
    sum = 0  # Set base for sum
    for num in vals:
        sum += num  # Create a sum
    return sum


def subtraction(vals):  # Subtract all the values in a list
    difference = vals[0]  # Set base for diff.
    for num in vals[1:]:
        difference -= num
    return difference


def division(num_one, num_two):  # Divide two numbers
    try:
        if '/' in num_one:
            frac = num_one.split('/')
            num_one = int(frac[0]) / int(frac[1])
        if '/' in num_two:
            frac = num_two.split('/')
            num_two = int(frac[0]) / int(frac[1])
    except TypeError:
        pass
    quotient = num_one / num_two
    values = quotient.as_integer_ratio()
    if len(str(values[0])) > 9 and len(str(values[1])) > 9:
        fraction_ver = Fraction(num_one,num_two)
    else:
        fraction_ver = str(values[0]) + '/' + str(values[1])
    statement = str(quotient) + ' or ' + str(fraction_ver)
    return statement


def multiplication(num_one, num_two):  # Multiply two numbers
    product = num_one * num_two
    if type(product) == float:
        product = Fraction(product)
    return product


def square_root(value):  # Determine the square root of a number
    sq_root = sqrt(value)
    check = str(sq_root).split('.')
    if 0 == check[0][0]:
        sq_root = int(sq_root)
    else:
        sq_root = Fraction(sq_root)
    return sq_root


def quadratic(equation):  # Determine the x values
    values = equation.split(' ')
    abc = []
    for i in values:
        abc.append(int(i))
    a = int(abc[0])
    b = int(abc[1])
    c = int(abc[2])
    try:
        formula_plus = ((b * -1) + (sqrt((b ** 2) - 4 * (a * c)))) / (2 * a)
        formula_minus = ((b * -1) - (sqrt((b ** 2) - 4 * (a * c)))) / (2 * a)
        statement = ('x = ' + str(formula_plus) + ', x = ' + str(formula_minus))
    except ValueError:  # Square Root is negative
        statement = 'Your square-root value is negative. Program Cannot Calculate.'
    return statement


def matrix_inverter(matrix):  # Inverts 2x2 Matrixes
    values = matrix.split(' ')
    new_matrix = []
    new_matrix.append(values[3])
    new_matrix.append(int(values[1]) * -1)
    new_matrix.append(int(values[2]) * -1)
    new_matrix.append(values[0])
    print('The inverted matrix is: ')
    counter = 0
    print('[', end=' ')
    for i in new_matrix:

        if counter == 2:
            print(']')
            print('[', end=' ')
        print(i, end=' ')
        counter += 1
    print(']')


def determinant_calculator(matrix):  # Calculate the determinant
    matrix_numbers = matrix.split(' ')
    all_vals = []
    for i in matrix_numbers:
        try:
            new = int(i)
        except ValueError:
            new = i
        all_vals.append(new)
    top_row = []
    middle_row = []
    bottom_row = []
    top_left_det = []
    top_mid_det = []
    top_right_det = []
    counter = 0
    for num in all_vals:
        if counter < 3:
            top_row.append(num)
        elif 2 < counter < 6:
            middle_row.append(num)
        else:
            bottom_row.append(num)
        counter += 1
    placement = 0

    for value in top_row:  # Create the inner determinant matrices
        if placement == 0:
            mid_copy = middle_row.copy()
            bot_copy = bottom_row.copy()
            past_indices = []
            for numbers in middle_row:
                if mid_copy.index(numbers) in past_indices:
                    place = mid_copy.index(numbers)
                    del mid_copy[place]
                    mid_copy.insert(place, '999999999999999999')

                if mid_copy.index(numbers) == placement:
                    del mid_copy[mid_copy.index(numbers)]
                    mid_copy.insert(placement, '99999999999999')
                else:
                    past_indices.append(mid_copy.index(numbers))
                    top_left_det.append(numbers)

            past_indices = []
            for numbers in bottom_row:
                if bot_copy.index(numbers) in past_indices:
                    place = bot_copy.index(numbers)
                    del bot_copy[place]
                    bot_copy.insert(place, '99999999999')
                if bot_copy.index(numbers) == placement:

                    del bot_copy[bot_copy.index(numbers)]
                    bot_copy.insert(placement, '9999999999999')
                else:
                    past_indices.append(bot_copy.index(numbers))
                    top_left_det.append(numbers)

        elif placement == 1:
            mid_copy = middle_row.copy()
            bot_copy = bottom_row.copy()
            past_indices = []
            for numbers in middle_row:
                if mid_copy.index(numbers) in past_indices:
                    place = mid_copy.index(numbers)
                    del mid_copy[place]
                    mid_copy.insert(place, '999999999999999999')

                if mid_copy.index(numbers) == placement:
                    del mid_copy[mid_copy.index(numbers)]
                    mid_copy.insert(placement, '99999999999999')
                else:
                    past_indices.append(mid_copy.index(numbers))
                    top_mid_det.append(numbers)

            past_indices = []
            for numbers in bottom_row:
                if bot_copy.index(numbers) in past_indices:
                    place = bot_copy.index(numbers)
                    del bot_copy[place]
                    bot_copy.insert(place, '99999999999')
                if bot_copy.index(numbers) == placement:

                    del bot_copy[bot_copy.index(numbers)]
                    bot_copy.insert(placement, '9999999999999')
                else:
                    past_indices.append(bot_copy.index(numbers))
                    top_mid_det.append(numbers)

        elif placement == 2:
            mid_copy = middle_row.copy()
            bot_copy = bottom_row.copy()
            past_indices = []
            for numbers in middle_row:
                if mid_copy.index(numbers) in past_indices:
                    place = mid_copy.index(numbers)
                    del mid_copy[place]
                    mid_copy.insert(place, '999999999999999999')

                if mid_copy.index(numbers) == placement:
                    del mid_copy[mid_copy.index(numbers)]
                    mid_copy.insert(placement, '99999999999999')
                else:
                    past_indices.append(mid_copy.index(numbers))
                    top_right_det.append(numbers)

            past_indices = []
            for numbers in bottom_row:
                if bot_copy.index(numbers) in past_indices:
                    place = bot_copy.index(numbers)
                    del bot_copy[place]
                    bot_copy.insert(place, '99999999999')
                if bot_copy.index(numbers) == placement:

                    del bot_copy[bot_copy.index(numbers)]
                    bot_copy.insert(placement, '9999999999999')
                else:
                    past_indices.append(bot_copy.index(numbers))
                    top_right_det.append(numbers)
        placement += 1

    try:
        statement = ((top_row[0] * ((top_left_det[0] * top_left_det[3]) - (top_left_det[1] * top_left_det[2]))) - \
                     (top_row[1] * ((top_mid_det[0] * top_mid_det[3]) - (top_mid_det[1] * top_mid_det[2]))) + \
                     (top_row[2] * ((top_right_det[0] * top_right_det[3]) - (top_right_det[1] * top_right_det[2]))))
    except TypeError:
        top_statement = ''
        if top_row[0] == 0 or top_row[0] == '0':
            top_statement = '0'
        else:
            if type(top_row[0]) == str:
                top_statement += top_row[0] + '('
            else:
                if top_row[0] > 1:
                    top_statement += str(top_row[0]) + '('
                else:
                    top_statement += '('
            if (type(top_left_det[0]) == str or type(top_left_det[3]) == str) and (type(top_left_det[1]) == str or type(top_left_det[2]) == str):
                if top_row[0] == '1' or top_row[0] == 1:
                    top_statement = '('+ (str(top_left_det[0]) + str(top_left_det[3])) +(' - ' + str(top_left_det[1]) + str(top_left_det[2]))+ ')'
                else:
                    top_statement = (str(top_row[0]) + '('+ (str(top_left_det[0]) + str(top_left_det[3])) +(' - ' + str(top_left_det[1]) + str(top_left_det[2]))+ ')')
                both = True
            else:
                both = False
            if both == True:
                pass
            elif (type(top_left_det[0]) == str or type(top_left_det[3]) == str) and both == False:
                top_statement += (str(top_left_det[0]) + str(top_left_det[3]) + ' - ')
            else:
                top_statement += str((top_left_det[0] * top_left_det[3]))
            if both == True:
                pass
            elif (type(top_left_det[1]) == str or type(top_left_det[2]) == str) and both == False:
                top_statement += (' - ' + str(top_left_det[1]) + str(top_left_det[2]))
            else:
                top_statement += str(top_left_det[1] * top_left_det[2])
            top_statement += ')'

        ###MID STATE
        mid_statement = ''
        if top_row[1] == 0 or top_row[1] == '0':
            mid_statement = '0'
        else:
            if type(top_row[1]) == str:
                mid_statement += top_row[1] + '('
            else:
                if top_row[1] > 1:
                    mid_statement += str(top_row[1]) + '('
                else:
                    mid_statement += '('
            if (type(top_mid_det[0]) == str or type(top_mid_det[3]) == str) and (type(top_mid_det[1]) == str or type(top_mid_det[2]) == str):
                if top_row[1] == '1' or top_row[1] == 1:
                    mid_statement = '(' + (str(top_mid_det[0]) + str(top_mid_det[3])) + (' - ' + str(top_mid_det[1]) + str(top_mid_det[2]))
                else:
                    mid_statement = (str(top_row[1]) + '(' + (str(top_mid_det[0]) + str(top_mid_det[3])) + (' - ' + str(top_mid_det[1]) + str(top_mid_det[2])))
                both = True
            else:
                both = False
            if both == True:
                pass
            elif (type(top_mid_det[0]) == str or type(top_mid_det[3]) == str) and both == False:
                mid_statement += (str(top_mid_det[0]) + str(top_mid_det[3]) + ' + ')
            else:
                mid_statement += str((top_mid_det[0] * top_mid_det[3]))
            if both == True:
                pass
            elif (type(top_mid_det[1]) == str or type(top_mid_det[2]) == str) and both == False:
                mid_statement += (' - ' + str(top_mid_det[1]) + str(top_mid_det[2]))
            else:
                mid_statement += str(top_mid_det[1] * top_mid_det[2])
            mid_statement += ')'

        ###BOT STATE
        bot_statement = ''
        if type(top_row[2]) == str:
            bot_statement += top_row[2] + '('
        else:
            if top_row[2] > 1:
                bot_statement += str(top_row[2]) + '('
            else:
                bot_statement += '('
        if (type(top_right_det[0]) == str or type(top_right_det[3]) == str) and (type(top_right_det[1]) == str or type(top_right_det[2]) == str):
            bot_statement = (str(top_row[2]) + '(' + (str(top_right_det[0]) + str(top_right_det[3])) + (' - ' + str(top_right_det[1]) + str(top_right_det[2])))
            both = True
        else:
            both = False
        if both == True:
            pass
        elif (type(top_right_det[0]) == str or type(top_right_det[3]) == str) and both == False:
            bot_statement += (str(top_right_det[0]) + str(top_right_det[3]) + ' + ')
        else:
            bot_statement += str((top_right_det[0] * top_right_det[3]))
        if both == True:
            pass
        elif (type(top_right_det[1]) == str or type(top_right_det[2]) == str) and both == False:
            bot_statement += (' - ' + str(top_right_det[1]) + str(top_right_det[2]))
        else:
            bot_statement += str(top_right_det[1] * top_right_det[2])
        bot_statement += ')'
    

    print((top_statement + ' - ' + mid_statement + ' + ' + bot_statement).center(150, ' '))
    print(('Unfortunately, I currently cannot simplify further. Hopefully, this helped you!').center(150, ' '))


def derivative_finder(equation):  # Find the derivative
    values = equation.split(' ')
    derivative = []
    for i in values:
        if 'x' in i:
            placement = i.index('x')
            try:
                value = int(i[placement + 1:])

            except ValueError:
                value = ''
            if value == '':  # No placement
                final = int(i[:placement])
                if final >= 0:
                    final = ' + ' + str(final)
                else:
                    final = ' - ' + str(final)
                derivative.append(final)
            else:
                final = (int(i[:placement]) * value)
                adding = value - 1
                if adding == 1:  # To keep derivative form
                    adding = ''
                statement = str(final) + 'x' + str(adding)
                derivative.append(statement)
    print('The derivative of ' + str(equation) + ' is: ')
    for x in derivative:
        print(x, end = '')
    print('')