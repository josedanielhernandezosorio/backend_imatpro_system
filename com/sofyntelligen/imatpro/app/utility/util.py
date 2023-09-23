
def get_representation_equation(list_code):
    view_latex = ''
    for code in list_code:
        view_latex += code['character']['view_latex'] + ' '

    return view_latex
