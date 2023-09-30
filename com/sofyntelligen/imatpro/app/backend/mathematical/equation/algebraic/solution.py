
def solution_equation(equation_expression):
    count = 0
    list_operation = []
    for item in equation_expression.get_argument_expression():
        if valid_operator(item):
            list_operation.append(count)
        count += 1
    return division(equation_expression, list_operation)


def subtraction(equation_expression, list_operation):
    try:
        equation_expression.simplify(
            equation_expression.get_argument_expression().index('-'),
            equation_expression.get_argument_expression().index('-'),
            '0')
        return subtraction(equation_expression, list_operation)
    except ValueError as error:
        return equation_expression


def addition(equation_expression, list_operation):
    try:
        equation_expression.simplify(
            equation_expression.get_argument_expression().index('+'),
            equation_expression.get_argument_expression().index('+'),
            '0')
        return addition(equation_expression, list_operation)
    except ValueError as error:
        return subtraction(equation_expression, list_operation)


def multiplication(equation_expression, list_operation):
    try:
        equation_expression.simplify(
            equation_expression.get_argument_expression().index('times'),
            equation_expression.get_argument_expression().index('times'),
            '0')
        return multiplication(equation_expression, list_operation)
    except ValueError as error:
        return addition(equation_expression, list_operation)


def division(equation_expression, list_operation):
    try:
        values = get_value(equation_expression, list_operation, 'div')
        result = int(values[2]) / int(values[3])
        print(values)
        print(result)
        equation_expression.simplify(values[0], values[1], result)
        return division(equation_expression, list_operation)
    except ValueError as error:
        return multiplication(equation_expression, list_operation)


def valid_operator(item):
    return item == 'div' or item == 'times' or item == '+' or item == '-'


def get_value(equation_expression, list_operation, operator):
    try:
        position_operation = equation_expression.get_argument_expression().index(operator)
        position_character = list_operation.index(position_operation)
        start = list_operation[position_character - 1] + 1
        stop = list_operation[position_character + 1] - 1
        return start, stop, ''.join(equation_expression.get_argument_expression()[start:position_operation]), \
            ''.join(equation_expression.get_argument_expression()[position_operation + 1:stop + 1])
    except ValueError as error:
        raise ValueError(operator)