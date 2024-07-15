import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.max_colwidth', None)


def write_holiday_cities(first_letter):
    data = pd.read_csv('StudentsHoliday/travel-notes.csv')

    want_to_visit = set()
    already_been_to = set()

    for _, row in data.iterrows():
        if row.iloc[0].startswith(first_letter.upper()):
            visited_cities = set(row.iloc[1].split(';'))
            to_visit_cities = set(row.iloc[2].split(';'))

            already_been_to.update(visited_cities)
            want_to_visit.update(to_visit_cities)

    not_visited_yet = want_to_visit - already_been_to

    first_city_to_visit = sorted(not_visited_yet)[0] if not_visited_yet else None

    result_data = {
        "Уже были": ','.join(sorted(already_been_to)),
        "Хотят посетить": ','.join(sorted(want_to_visit)),
        "Еще не были": ','.join(sorted(not_visited_yet)),
        "Первый город для посещения": first_city_to_visit
    }

    result_df = pd.DataFrame([result_data])

    result_df.to_csv('StudentsHoliday/holiday.csv', index=False)


def print_holiday():
    holidata = pd.read_csv('StudentsHoliday/holiday.csv')
    for column in holidata.columns:
        print(f'{column}: {holidata[column].values[0]}')


write_holiday_cities('r')
print_holiday()
