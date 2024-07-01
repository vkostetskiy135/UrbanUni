
#Не получалось наследовать напрямую, все время вылетали ошибки
# import datetime
#
#
# class SuperDate(datetime.datetime):
#     def __init__(self, year, month,  day, hour, *args, **kwargs):
#         super().__init__(year, month,  day, hour, 0, 0, 0 *args, **kwargs)
#
#     def get_season(self):
#         seasons = {'Winter': [12, 1, 2], 'Spring': [3, 4, 5], 'Summer': [6, 7, 8], 'Autumn': [9, 10, 11]}
#         for s in seasons:
#             if self.month in seasons[s]:
#                 return s
#
#     def get_time_of_day(self):
#         times_of_day = {'Morning': [_ for _ in range(6, 12)],
#                         'Day': [_ for _ in range(12, 18)],
#                         'Evening': [_ for _ in range(18, 24)],
#                         'Night': [_ for _ in range(6)]}
#         for t in times_of_day:
#             if self.hour in times_of_day[t]:
#                 return t
#
#
# a = SuperDate(2024, 2, 22, 12)
# print(a.get_season())
# print(a.get_time_of_day())

#Поэтому придумал вот такой способ.
import datetime

class SuperDate:
    def __init__(self, year, month, day, hour):
        self.date = datetime.datetime(year, month, day, hour)

    def get_season(self):
        seasons = {'Winter': [12, 1, 2], 'Spring': [3, 4, 5], 'Summer': [6, 7, 8], 'Autumn': [9, 10, 11]}
        for season, months in seasons.items():
            if self.date.month in months:
                return season

    def get_time_of_day(self):
        times_of_day = {'Morning': range(6, 12),
                        'Day': range(12, 18),
                        'Evening': range(18, 24),
                        'Night': range(0, 6)}
        for time_of_day, hours in times_of_day.items():
            if self.date.hour in hours:
                return time_of_day

a = SuperDate(2024, 2, 22, 12)
print(a.get_season())
print(a.get_time_of_day())

