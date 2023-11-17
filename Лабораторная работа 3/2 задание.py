# TODO Напишите функцию find_common_participants
def find_common_participants(participants_first_group, participants_second_group, sep=','):

    participants_first_group = set(participants_first_group.split(sep))

    participants_second_group = set(participants_second_group.split(sep))

    common_participants = participants_first_group.intersection(participants_second_group)

    common_participants = sorted(list(common_participants))

    return common_participants

participants_first_group = "Иванов|Петров|Сидоров"

participants_second_group = "Петров|Сидоров|Смирнов"

print(find_common_participants(participants_first_group, participants_second_group, sep='|'))


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
