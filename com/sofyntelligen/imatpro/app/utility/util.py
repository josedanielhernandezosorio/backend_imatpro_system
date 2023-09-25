from py_asciimath.translator.translator import ASCIIMath2MathML, MathML2Tex


def get_representation_equation(list_code):
    latex_math = ''
    for code in list_code:
        latex_math += code['character']['view'] + ' '

    return latex_math


def get_view_math(equation):
    asciiMath2MathML = ASCIIMath2MathML(log=False, inplace=True).translate(equation, displaystyle=True, dtd="mathml2",
                                                                dtd_validation=True, from_file=False, output="string",
                                                                network=True, pprint=False, to_file=None,
                                                                xml_declaration=True, xml_pprint=True,)
    print(asciiMath2MathML)
    mathML2Tex = MathML2Tex().translate(asciiMath2MathML, network=False, from_file=False,)
    print(mathML2Tex)
    return mathML2Tex, asciiMath2MathML
