data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]


def count_whatever_inside(data):
    main_queue = [data]
    sum_ = 0
    while main_queue:
        cur_data = main_queue.pop(0)
        if isinstance(cur_data, str):
            sum_ += len(cur_data)
        elif isinstance(cur_data, int):
            sum_ += cur_data
        elif isinstance(cur_data, dict):
            for k, v in cur_data.items():
                main_queue.append([k, v])
        else:
            for i in cur_data:
                main_queue.append(i)
    return sum_


print(count_whatever_inside(data_structure))




