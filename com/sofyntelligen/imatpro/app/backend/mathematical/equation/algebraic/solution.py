from decimal import Decimal


def solution_equation(equation_expression):
    return division(equation_expression)


def subtraction(equation_expression):
    try:
        values = get_value(equation_expression, '-')
        result = Decimal(values[2]) - Decimal(values[3])
        equation_expression.simplify(values[0], values[1], list(str(result)))
        return subtraction(equation_expression)
    except ValueError as error:
        return equation_expression


def addition(equation_expression):
    try:
        values = get_value(equation_expression, '+')
        result = Decimal(values[2]) + Decimal(values[3])
        equation_expression.simplify(values[0], values[1], list(str(result)))
        return addition(equation_expression)
    except ValueError as error:
        return subtraction(equation_expression)


def multiplication(equation_expression):
    try:
        values = get_value(equation_expression, 'times')
        result = Decimal(values[2]) * Decimal(values[3])
        equation_expression.simplify(values[0], values[1], list(str(result)))
        return multiplication(equation_expression)
    except ValueError as error:
        return addition(equation_expression)


def division(equation_expression):
    try:
        values = get_value(equation_expression, 'div')
        result = Decimal(values[2]) / Decimal(values[3])
        equation_expression.simplify(values[0], values[1], list(str(result)))
        return division(equation_expression)
    except ValueError as error:
        return multiplication(equation_expression)


def valid_operator(item):
    return item == 'div' or item == 'times' or item == '+' or item == '-'


def get_value(equation_expression, operator):
    try:
        list_operation = get_list_operation(equation_expression)
        position_operation = equation_expression.get_argument_expression().index(operator)
        position_character = list_operation.index(position_operation)
        start = 0 if position_character == 0 else list_operation[position_character - 1] + 1
        stop = equation_expression.get_argument_expression().__len__() if list_operation.index(position_operation) + 1 == list_operation.__len__() else list_operation[position_character + 1] - 1
        return start, stop, ''.join(equation_expression.get_argument_expression()[start:position_operation]), \
            ''.join(equation_expression.get_argument_expression()[position_operation + 1:stop + 1])
    except ValueError as error:
        raise ValueError(operator)


def get_list_operation(equation_expression):
    count = 0
    list_operation = []
    for item in equation_expression.get_argument_expression():
        if valid_operator(item):
            list_operation.append(count)
        count += 1
    return list_operation

