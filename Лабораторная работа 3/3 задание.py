# TODO  Напишите функцию count_letters

def count_letters(text):
    # приведу всё к одному регитсру
    lowercase_text = text.lower()
    letters_count = {}
    for letter in lowercase_text:
        if letter.isalpha():
            if letter in letters_count:
                letters_count[letter] += 1   # добавлю к существующей букве - одну букву
            else:
                letters_count[letter] = 1    # если ее нет, присваиваюю ей значение 1

    return letters_count


# TODO Напишите функцию calculate_frequency

def calculate_frequency(count):
    total_letters = sum(count.values()) #Общее количество букв
    frequency = {} #Новый словарь
    for one_letter, count_let in count.items():
        if one_letter.isalpha(): #Проверяю буква ли это
            frequency[one_letter] = count_let/total_letters #Вычисляю частоту
    return frequency

main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""

# TODO Распечатайте в столбик букву и её частоту в тексте
count = count_letters(main_str)
frequency = calculate_frequency(count)

for letter, frequency_letter in frequency.items():
    print(f"{letter}: {frequency_letter:.2f}")
