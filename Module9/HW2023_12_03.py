def is_prime(func):
    def wrapper(*args, **kwargs):
        func_result = func(*args, **kwargs)
        dividable_by = []
        for i in range(2, func_result):
            if func_result % i == 0:
                dividable_by.append(i)
        if not dividable_by:
            print('Простое')
        else:
            print('Сложное')
        return func_result
    return wrapper


@is_prime
def sum_three(a, b, c):
    return a + b + c

print(sum_three(2, 3, 6))

print(sum_three(4, 5, 6))