grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}


def avg_scores_for_students(grades_list, students_set):
    """
    Собирает на ходу словарь. В качестве ключа берет имя студента из отсортированного списка,
    а в качестве значения подставляет средний балл из списка оценок
    """
    result = {}
    for i, student in enumerate(sorted(students_set)):
        result[student] = round(sum(grades_list[i]) / len(grades_list[i]), 2)
    return result


print(avg_scores_for_students(grades, students))
