def count_calls():
    global calls
    calls += 1


def string_info(string: str):
    count_calls()
    result = (len(string), string.upper(), string.lower())
    return result


def is_contains(string: str, list_to_search: list):
    count_calls()
    for word in list_to_search:
        if string.lower() == word.lower():
            return True
    return False

calls = 0

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)