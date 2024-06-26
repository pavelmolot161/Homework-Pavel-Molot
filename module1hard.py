
   # ЗАДАНИЕ "СРЕДНИЙ БАЛ" #

grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bildo', 'Steve', 'Khendrik', 'Aaron'}
meam_1 = sum(grades[0]) / len((grades[0]))
meam_2 = sum(grades[1]) / len((grades[1]))
meam_3 = sum(grades[2]) / len((grades[2]))
meam_4 = sum(grades[3]) / len((grades[3]))
meam_5 = sum(grades[4]) / len((grades[4]))
students_1 = list(students)
students_1.sort()
print(students_1)
students_2 = dict()
students_2[students_1[0]] = meam_1
students_2[students_1[1]] = meam_2
students_2[students_1[2]] = meam_3
students_2[students_1[3]] = meam_4
students_2[students_1[4]] = meam_5
print(students_2)



