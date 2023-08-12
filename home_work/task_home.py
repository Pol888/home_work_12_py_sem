import csv
import os
import statistics

class ValidationStudentsName:
    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value:str):
        if value.istitle() and value.isalpha():
            setattr(instance, self.param_name, value)
        else:
            raise ValueError

class Student:
    first_name = ValidationStudentsName()
    last_name = ValidationStudentsName()
    def __init__(self, first_name, last_name, grade_report):
        self.first_name = first_name
        self.last_name = last_name
        self.grade_report = grade_report




    def __str__(self):
        result = f'Student name - {self.first_name} {self.last_name}\n Grade_Report:\n' \
                 f'  Subject{" " * (max(map(lambda x: len(x[0]), self.grade_report)) - len("Subject"))}|' \
                 f'Marks{" " * (max(map(lambda x: len(x[1]) * 2, self.grade_report)) - len("Marks") - 1) }|' \
                 f'Test_result{" " * (max(map(lambda x: len(x[2]) * 2, self.grade_report)) - len("Test_result")) } ' \
                 f'|Average score for tests\n'
        for i in self.grade_report:


            result += '  ' + str(i[0]) + " " * (max(map(lambda x: len(x[0]), self.grade_report)) - len(str(i[0])) ) + '|'   \
                      + ' '.join(map(str,i[1])) +  ( ' ' * (max(map(lambda x: len(x[1]) * 2 - 1, self.grade_report)) -
                                                            len(i[1]) * 2 + 1 ) )  + '|' \
                      + ' '.join(map(str, i[2])) + (' ' *   ((max(map(lambda x: len(' '.join( map(str,x[2])  )), self.grade_report))) -
                                                             len(' '.join(map(str, i[2]))))    )  + '|' + str(round(statistics.mean(i[2]), 2)) + '\n'

        average_score_on_marks_list = []
        for i in self.grade_report:
            average_score_on_marks_list.extend(i[1])

        result += f'  Average_score_on_marks: {round(statistics.mean(average_score_on_marks_list), 2)}\n'
        return result



class StudentFactory: # фабрика студентов
    def __call__(self, path_db_students):
        list_students = []
        os.chdir(path_db_students)
        files = os.listdir()
        for i in files:
            with open(i, 'r', newline='') as f_1:
                csv_r = list(csv.reader(f_1))[1:]
                grade_report = [[i[0], [int(j) for j in i[1].split()], [int(l) for l in i[2].split()]] for i in csv_r]
                first_name = i.split('_')[0]
                last_name = i.split('_')[1].split('.')[0]
                list_students.append(Student(first_name, last_name, grade_report))

        return list_students


list_st = StudentFactory()('C:\\Users\\pollove\\Desktop\\home_work_12_py_sem\\home_work\\db_students')
for i in list_st:
    print(i.__str__())
# output
'''
  Student name - Ivanov Ivan
   Grade_Report:
    Subject        |Marks            |Test_result|Average score for tests
    mathematics    |5 4 3 5 2 3 4 5 5|25 55 30   |36.67
    physics        |4 4 3 2 5 4 3 3 4|50 69 32 99|62.5
    chemistry      |5 4 3 3 3 4 5 3  |66 99      |82.5
    native_language|4 3 2 2 3 4 5    |90 88 44   |74
    Average_score_on_marks: 3.67

  Student name - Sergeev Sergey
   Grade_Report:
    Subject        |Marks            |Test_result |Average score for tests
    mathematics    |2 2 2 5 2 2 4 5 4|66 99 33    |66
    physics        |2 4 3 2 5 4 3 3 4|33 69 44 100|61.5
    chemistry      |3 5 3 4 3 4 4 4 4|77 100      |88.5
    native_language|2 3 5 2 5 5 5    |90 88 44    |74
    Average_score_on_marks: 3.5'''
