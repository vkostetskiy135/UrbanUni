class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed
        self.time = 0

    def run(self):
        self.distance += self.speed * 2
        self.time += 1

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):

        #Функция, которая в конце цикла, подкорректирует занятые участниками места, если потребуется
        #Добавил в класс Runner аттрибут объекта time и метод run так же увеличивает счетчик time.
        #В дальнейшем сравниваем именно время
        def correction_func(finishers_dict):
            all_places = [n for n in range(1, len(finishers_dict) + 1)]
            sorted_participants = sorted(finishers_dict.values(), key=lambda x: x.time, reverse=False)
            str_participapants = [str(participant) for participant in sorted_participants]
            return dict(zip(all_places, str_participapants))

        #Но вообще, мы знаем скорость каждого участника и тратить вычислительные мощности на проведение соревнований
        #совсем не нужно. Функция ниже могла бы заменить весь остальной код в методе start.

        # def results_without_competition():
        #     all_places = [n for n in range(1, len(self.participants) + 1)]
        #     sorted_participants = sorted(self.participants, key=lambda x: x.speed, reverse=True)
        #     return dict(zip(all_places, [str(participant) for participant in sorted_participants]))

        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return correction_func(finishers)


if __name__ == '__main__':

    runner1 = Runner('Vasya')
    runner2 = Runner('Kolya', 7)
    runner3 = Runner('Krypton', 8)
    runner4 = Runner('Megatron', 4)

    tour1 = Tournament(100, runner1, runner2, runner3, runner4)
    tour_result = tour1.start()
    print(tour_result)

