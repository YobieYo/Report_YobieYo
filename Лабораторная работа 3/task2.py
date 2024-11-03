# TODO Напишите функцию find_common_participants
def find_common_participants(str1,str2,sep=','):
    a =set(str1.split(sep))
    b = str2.split(sep)
    c = list(a.intersection(b))
    c.sort()
    return c


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой

print(find_common_participants(participants_first_group, participants_second_group, sep='|'))