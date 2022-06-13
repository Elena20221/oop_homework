class Student:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.average_rating = float()

    def __str__(self):
        grades_count = 0
        _courses_in_progress_string = ', '.join(self.courses_in_progress)
        _finished_courses_string = ', '.join(self.finished_courses)
        for k in self.grades:
            grades_count += len(self.grades[k])
        self.average_rating = sum(map(sum, self.grades.values()))/grades_count
        res = f'Имя: {self.name}\n'\
              f'Фамилия: {self.surname}\n'\
              f'Средняя оценка за домашнее задание:{self.average_rating}\n'\
              f'Курсы в процессе обучения: {_courses_in_progress_string}\n'\
              f'Завершенные курсы: {_finished_courses_string}'
        return res

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('not ')
            return
        return self.average_rating <  other.average_rating


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.average_rating = float()

    def __str__(self):
        grades_count = 0
        for k in self.grades:
            grades_count += len(self.grades[k])
        self.average_rating = sum(map(sum, self.grades.values())) / grades_count
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_rating}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Такое сравнение некорректно ')
            return
        return self.average_rating <  other.average_rating

class Reviewer(Mentor):
    def __int__(self,name, surname,):
        super().__init__(name, surname)


    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res


lecturer_1 = Lecturer('Ivan','Ivanov')
lecturer_1.courses_attached +=['Python']

lecturer_2 = Lecturer('Pety','Petrov')
lecturer_2.courses_attached +=['Java']

reviwer_1 =Reviewer('Some','Buddy')
reviwer_1.courses_attached +=['Python']
reviwer_1.courses_attached +=['Java']

reviwer_2 =Reviewer('Sergey','Serov')
reviwer_2.courses_attached +=['Python']
reviwer_2.courses_attached +=['Java']

student_1 = Student('Kir','Moon')
student_1.courses_in_progress +=['Python']
student_1.finished_courses +=['Введение в программирование.']

student_2 = Student('Roy', 'Eman')
student_2.courses_in_progress +=['Java']
student_2.finished_courses +=['Введение в программирование.']

student_1.rate_hw(lecturer_1, 'Python',10)
student_1.rate_hw(lecturer_1, 'Python',10)

student_1.rate_hw(lecturer_2, 'Java',5.5)
student_1.rate_hw(lecturer_2, 'Java',7)

student_2.rate_hw(lecturer_1, 'Python',8.8)
student_2.rate_hw(lecturer_1, 'Python',9)

student_2.rate_hw(lecturer_2, 'Java',10)
student_2.rate_hw(lecturer_2, 'Java',9.5)

reviwer_1.rate_hw(student_1,'Python',8)
reviwer_1.rate_hw(student_1,'Python',10)

reviwer_2.rate_hw(student_2,'Java',8.5)
reviwer_2.rate_hw(student_2,'Java',10)


print(f'Перечень проверяющих:\n\n{reviwer_1}\n\n{reviwer_2}')
print()
print(f'Перечень студентов:\n\n{student_1}\n\n{student_2}')
print()
print(f'Перечень лектров:\n\n{lecturer_1}\n\n{lecturer_2}')
print()
print(f'Результат сравнения студентов (по средним оценкам за ДЗ): '
      f'{student_1.name} {student_1.surname} < {student_2.name} {student_2.surname} = {student_1 > student_2}')
print()
print(f'Результат сравнения лекторов (по средним оценкам за лекции): '
      f'{lecturer_1.name} {lecturer_1.surname} < {lecturer_2.name} {lecturer_2.surname} = {lecturer_1 > lecturer_2}')
print()
student_list = [student_1,student_2]
lecturer_list = [lecturer_1,lecturer_2]


def student_rating(student_list,course_name):
    sum_all = 0
    count_all = 0
    for stud in student_list:
        if stud.courses_in_progress == [course_name]:
           sum_all += stud.average_rating
           count_all += 1
    average_for_all = sum_all/count_all
    return average_for_all


def lecturer_rating(lecturer_list, course_name):
    sum_all = 0
    count_all = 0
    for lecturer  in lecturer_list:
        if lecturer.courses_attached == [course_name]:
           sum_all += lecturer.average_rating
           count_all += 1
    average_for_all = sum_all / count_all
    return average_for_all


print(f"Средняя оценка для всех студентов по курсу {'Python'}:{student_rating(student_list,'Python')}")
print(f"Средняя оценка для всех студентов по курсу {'Java'}:{student_rating(student_list,'Java')}")
print()
print(f"Средняя оценка для всех лекторов по курсу {'Python'}: {lecturer_rating(lecturer_list,'Python')}")
print(f"Средняя оценка для всех лекторов по курсу {'Java'}: {lecturer_rating(lecturer_list,'Java')}")
