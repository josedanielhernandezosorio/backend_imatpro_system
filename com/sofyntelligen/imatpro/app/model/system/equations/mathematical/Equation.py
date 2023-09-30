from com.sofyntelligen.imatpro.app.utility.util import get_representation_equation


class EquationExpression:

    expression = None
    data = None

    def __init__(self, data):
        self.data = data
        self.expression = get_representation_equation(self.data['list_code'])
        self.__argument_expression = self.expression.split()
        self.__list_expression_solution = []

    def simplify(self, start, stop, values):
        count = 0
        argument_expression = []
        for item in self.__argument_expression:
            if not (start <= count <= stop):
                argument_expression.append(item)
            count += 1
        self.__argument_expression = argument_expression
        self.__argument_expression.insert(start, values)
        self.__list_expression_solution.append(self.__argument_expression)

    def get_argument_expression(self):
        return self.__argument_expression

    def set_argument_expression(self, argument_expression):
        self.__argument_expression = argument_expression

    def __str__(self):
        return 'EquationExpression(' + \
            f'expression={self.expression}' + \
            f',__argument_expression={self.__argument_expression.__str__()}' + \
            f',__list_expression_solution={self.__list_expression_solution.__str__()}' + \
            f',data={self.data})'


