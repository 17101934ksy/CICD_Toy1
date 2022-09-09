import re

def generate_integer(string):
    """ 문자열에서 정수만 추출하는 함수

    Args:
        string (string): 문자열

    Returns:
        _type_: 정수만 가지는 문자열
    """
    integer_compile = re.compile(r'[0-9]')
    string = re.findall(integer_compile, string)

    return ''.join(string)

# def convert_request_form(form):

