from django.db import models


class EquationFilterManager(models.Manager):

    def get_equation_all(self, type_representation='PRINCIPAL'):
        return self.filter(type_representation=type_representation)

    def get_type_equation(self, type_equations, type_representation='PRINCIPAL'):
        return self.filter(type_representation=type_representation).filter(type_equations=type_equations)

    def get_grade_school(self, grade_school, type_representation='PRINCIPAL'):
        return self.filter(type_representation=type_representation).filter(grade_school=grade_school)

    def get_solution_id(self, solution_id):
        return self.filter(solution_id=solution_id)

    # TODO: document enpoint filters
    def filters(self, object_type_equations, object_grade_school, type_equations, grade_school, type_representation):

        if type_representation == 'ALL':
            return self.all()
        if None != type_equations:
            if None != type_representation:
                return self.get_type_equation(object_type_equations.values_list('id', flat=True).get(value=type_equations), type_representation=type_representation)
            else:
                return self.get_type_equation(object_type_equations.values_list('id', flat=True).get(value=type_equations))
        else:
            if None != grade_school:
                if None != type_representation:
                    return self.get_grade_school(object_grade_school.values_list('id', flat=True).get(value=grade_school), type_representation=type_representation)
                else:
                    return self.get_grade_school(object_grade_school.values_list('id', flat=True).get(value=grade_school))
            else:
                if None != type_representation:
                    return self.get_equation_all(type_representation=type_representation)
                else:
                    return self.get_equation_all()

    def solution(self, solution_id):
        if None != solution_id:
            return self.filter(solution_id=solution_id)
        else:
            return self.all()



