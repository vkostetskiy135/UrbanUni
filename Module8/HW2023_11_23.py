class ForbiddenSymbol(Exception):
    pass


class Numberism(Exception):
    pass


def exception_wrapper(func):
    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except Numberism:
            print('Numbers are not welcome!')
        except ForbiddenSymbol:
            print('Special characters are not welcome!')
        else:
            print('Hallelujah to the letters!')
    return wrapper


@exception_wrapper
def test(example):
    if example.isalnum():
        if not example.isalpha():
            raise Numberism()
    else:
        raise ForbiddenSymbol()




example1 = 'asdAD3'
example2 = 'asdAD!'
example3 = 'asdasd'
test(example1)
test(example2)
test(example3)
