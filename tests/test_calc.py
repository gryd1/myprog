def add(x, y):
    try:
        z = x + y
        if z == '':
            return 'Error'
        return str(z)
    except:
        return 'Error'


def test_add_1():
    assert add(-15, 14) == '-1'
    print(add(-15, 14))


def test_add_2():
    assert add(20, 24) == '44'
    print(add(20, 24))


def test_add_3():
    assert add(-15, 15) == '0'
    print(add(-15, 15))


def test_add_4():
    assert add(-15.3, 14.8) == '-0.5'
    print(add(-15.3, 14.8))


def test_add_5():
    assert add(x='', y='') == 'Error'
    print(add(x='', y=''))


def minus(x, y):
    try:
        z = x - y
        return str(z)
    except:
        return 'Error'


def test_minus_1():
    assert minus(-30.4, 5.6) == '-36.0'
    print(minus(-30.4, 5.6))


def test_minus_2():
    assert minus(-30, -35) == '5'
    print(minus(-30, -35))


def test_minus_3():
    assert minus(30, 30) == '0'
    print(minus(30, 30))


def test_minus_4():
    assert minus(-30, 5) == '-35'
    print(minus(-30, 5))


def test_minus_5():
    assert minus(x='', y='') == 'Error'
    print(minus(x='', y=''))


def multiplication(x, y):
    try:
        z = x * y
        return str(z)
    except:
        return 'Error'


def test_multi_1():
    assert multiplication(60, 0) == '0'
    print(multiplication(60, 0))


def test_multi_2():
    assert multiplication(60, -1.5) == '-90.0'
    print(multiplication(60, -1.5))


def test_multi_3():
    assert multiplication(60, 1.5) == '90.0'
    print(multiplication(60, 1.5))


def test_multi_4():
    print(multiplication(x='', y=''))


def division(x, y):
    try:
        if y != 0:
            z = x / y
            return str(z)
        else:
            return 'Error'
    except:
        return 'enter two parameters'


def test_divi_1():
    assert division(0, 1.5) == '0.0'
    print(division(0, 1.5))


def test_divi_2():
    assert division(-60, 1.5) == '-40.0'
    print(division(-60, 1.5))


def test_divi_3():
    assert division(60, 1.5) == '40.0'
    print(division(60, 1.5))


def test_divi_4():
    assert division(5, 0) == 'Error'
    print(division(5, 0))


def test_divi_5():
    assert division(x='', y='') == 'enter two parameters'
    print(division(x='', y=''))


def substraction(index, lens, string):
    try:
        if index > 0:
            index = index - 1
            if lens > 0:
                lens = lens + index
                result = list(string)
                slices = result[index:lens]
                mystring = ''.join(slices)
            else:
                return 'Error lens'
            return mystring
        else:
            return 'Error index'
    except:
        return 'Where three parameters'


def test_substraction_1():
    assert substraction(1, 2, 'hello world') == 'he'
    print(substraction(1, 2, 'hello world'))


def test_substraction_2():
    assert substraction(0, 2, 'hello world') == 'Error index'
    print(substraction(0, 2, 'hello world'))


def test_substraction_3():
    assert substraction(1, 0, 'hello world') == 'Error lens'
    print(substraction(1, 0, 'hello world'))


def test_substraction_4():
    assert substraction(index='', lens=2, string='hello world') == 'Where three parameters'
    print(substraction(index='', lens=2, string='hello world'))


def test_substraction_5():
    assert substraction(1, 20, 'hello world') == 'hello world'
    print(substraction(1, 20, 'hello world'))


def upper(string):
    try:
        if string != '':
            result = string.upper()
            return result
        else:
            return 'abort(422)'
    except:
        return 'abort(422)'


def test_upper_1():
    print(upper('hello world'))


def test_upper_2():
    assert upper(string='') == 'abort(422)'
    print('abort(422)')


def test_upper_3():
    print(upper('HeLlo123 WORLD'))


def lower(string):
    try:
        if string != '':
            result = string.lower()
            return result
        else:
            return 'abort(422)'
    except:
        return 'abort(422)'


def test_lower_1():
    print(lower('HELLO WORLD'))


def test_lower_2():
    assert lower(string='') == 'abort(422)'
    print('abort(422)')


def test_lower_3():
    print(lower('HeLlo123 WORLD'))
