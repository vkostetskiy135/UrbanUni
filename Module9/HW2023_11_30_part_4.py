def all_variants(some_str):
    for i in range(1, len(some_str) + 1):
        for y in range(len(some_str)):
            if y + i > len(some_str):
                break
            yield some_str[y:y + i]


for _ in all_variants('abc'):
    print(_)