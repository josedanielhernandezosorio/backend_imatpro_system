
import json
from uuid import uuid4
from com.sofyntelligen.imatpro.app.utility.util import get_view_math


class EquationExpression:

    expression = None

    def __init__(self, data, character):
        self.__data_init = data
        self.__data_character = character
        self.__data_init['order'] = 1
        self.__data_init['solution_id'] = uuid4()
        del self.__data_init['date']
        del self.__data_init['last_update']
        del self.__data_init['character_count']
        self.expression = self.__data_init['view']
        self.__result = self.expression.split()
        self.__result_procedure = [self.__result]
        self.__data = [self.__data_init.__str__()]

        print(self.__result_procedure)

    def simplify(self, start, stop, values):
        count = 0
        argument_expression_init = []
        argument_expression_end = []
        for item in self.__result:
            if not (start <= count <= stop):
                if count <= start:
                    argument_expression_init.append(item)
                if stop <= count:
                    argument_expression_end.append(item)
            count += 1
        self.__result = argument_expression_init
        self.__result.extend(values)
        self.__result.extend(argument_expression_end)
        self.__result_procedure.append(self.__result)
        data = self.__data_init
        data['type_representation'] = 'DEVELOPMENT'
        data['order'] = data['order'] + 1
        data['list_code'] = []
        data['view'] = ' '.join(self.__result)
        mathML2Tex, asciiMath2MathML = get_view_math(data['view'])
        data['latex_math'] = mathML2Tex
        data['math_ml'] = asciiMath2MathML
        self.__data.append(data.__str__())
        print(self.__result_procedure)


    def get_argument_expression(self):
        return self.__result

    def set_argument_expression(self, argument_expression):
        self.__result = argument_expression

    def __str__(self):
        return 'EquationExpression(' + \
            f'expression={self.expression}' + \
            f',__result={self.__result}' + \
            f',__result_procedure={self.__result_procedure}' + \
            f',__data={self.__data})'


