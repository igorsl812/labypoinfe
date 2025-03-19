# TODO Напишите функцию find_common_participants
def find_common_participants(str1,str2,raz=","):
    got=[]
    l1=str1.split(raz)
    l2 = str2.split(raz)
    for i in l1:
        for j in l2:
            if i==j:
                got.append(i)
    return sorted(got)



participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
a=find_common_participants(participants_first_group,participants_second_group,"|")
print(a)
# TODO Провеьте работу функции с разделителем отличным от запятой
