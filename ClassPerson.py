class Person():
    def __init__(self, first_name, last_name, second_name, birthday):
        self.first_name = first_name
        self.last_name = last_name
        self.second_name = second_name
        self.birthday = birthday


class Student(Person):
    def __init__(self, first_name, last_name, second_name, birthday, facultet, list_score, teacher):
        super().__init__(first_name, last_name, second_name, birthday)
        self.facultet = facultet
        self.list_score = list_score
        self.teacher = teacher

    def get_scores(self):
        print(
            f"Студент: {self.last_name} {self.first_name} {self.second_name} учится у {self.teacher}, лист оценок: {self.list_score}")

    def set_score(self, score):
        self.list_score.append(score)

    def average_score(self):
        print(round(sum(self.list_score) / len(self.list_score), 1))


class Teacher(Person):
    def __init__(self, first_name, last_name, second_name, birthday, subject, salary, q_of_students):
        super().__init__(first_name, last_name, second_name, birthday)
        self.subject = subject
        self.salary = salary
        self.q_of_students = q_of_students

    def get_scores(self):
        print(
            f"Преподаватель: {self.last_name} {self.first_name} {self.second_name} по предмету {self.subject}, зарплата: {self.salary}, кол-во студентов {self.q_of_students}")


student1 = Student("Иван", "Петров", "Павлович", "2001",
                   'Факультет1', [4, 5, 4, 5, 3], 'Петров С.М.')
student2 = Student("Алина", "Сичень", "Викторовна", "2002",
                   'Факультет1', [5, 5, 4, 4, 5], 'Петров С.М.')
student3 = Student("Алексей", "Садовский", "Сергеевич", "2003",
                   'Факультет2', [3, 5, 4, 4, 5], 'Петров С.М.')

teacher_one = Teacher('Сергей', 'Петров', 'Михайлович',
                      '1980', 'Математика', 10000, 50)
teacher_two = Teacher('Василий', 'Котыгорох', 'Семенович',
                      '1982', 'Химия', 10000, 30)
print(student1.list_score)
student1.set_score(1)
print(student1.list_score)
student1.average_score()
