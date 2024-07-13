import datetime


class SuperDate(datetime.datetime):

    def get_season(self):
        seasons = {'Winter': [12, 1, 2], 'Spring': [3, 4, 5], 'Summer': [6, 7, 8], 'Autumn': [9, 10, 11]}
        for s in seasons:
            if self.month in seasons[s]:
                return s

    def get_time_of_day(self):
        times_of_day = {'Morning': [_ for _ in range(6, 12)],
                        'Day': [_ for _ in range(12, 18)],
                        'Evening': [_ for _ in range(18, 24)],
                        'Night': [_ for _ in range(6)]}
        for t in times_of_day:
            if self.hour in times_of_day[t]:
                return t


a = SuperDate( 2024, 2, 22, 12)
print(a.get_season())
print(a.get_time_of_day())


