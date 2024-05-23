def z41():
    n = 10
    i = 1
    while i <= n:
        a = int(input("Vvedite chislo "))
        if (a % 3) == 0:
            print("Chislo delitsa na 3")
        else:
             print("Chislo ne delitsa na 3")
        i += 1

def z42():
    try:
        n = 100
        a = int(input("vvedite chislo"))
        b = n / a
        print(b)
    except ValueError:
        print("na str delit nezia")
    except ZeroDivisionError:
        print("na 0 delit nezia")

def z43():
    date = input("Введите дату месяц и год (в формате ДД.ММ.ГГГГ): ")
    day, month, year = map(int,date.split("."))
    if day * month == year % 100:
        print("маг дата!")
    else:
        print(" не явл маг дата.")

def z44():
    try:
        a = input("Введите число: ")
        if len(a) == 6:
            if int(a[0]) + int(a[1]) + int(a[2]) == int(a[3]) + int(a[4]) + int(a[5]):
                print("Счастливое число")
            else:
                print("Несчастливое число")
        else:
            print("Ошибка, введите число из шести цифр")
    except ValueError:
        print("Ошибка, используйте цифры")


def z51():
    a = [2, 7, 12, 19, 23]
    b = int(input("Введите число: "))
    if b in a:
        print("Поздравляю, Вы угадали число!")
    else:
        print("Нет такого числа!")
    print( "Были загаданы числа: ", a)

def z52():
    my_list = [2, 5, 3, 8, 2, 7, 5]
    print("Были загаданы числа: ", my_list)
    b = list()
    c = 0
    for i in my_list:
        if i in b:
            print("Повторяющийся элемент: ", i)
            c += 1
        else:
            b.append(i)
    if c == 0:
        print("Повторений нет")

def z53():
    a = ('пн', 'вт', 'ср', 'чт', 'пт', 'сб', 'вс')
    b_input = input("Какие дни вы хотите выходными: ")
    b = b_input.split(' ')
    print(b)
    b_list = []
    w_list = []
    for i in a:
        if i in b:
            b_list.append(i)
        else:
            w_list.append(i)
    print(b_list)
    print("Ваши выходные дни: ", ', '.join(reversed(b_list)), " - ", len(b_list), "дня")
    print("Ваши рабочие дни: ", ', '.join(w_list), " - ", len(w_list), "дней")


def z54():
    Import random
    g1 = ["Иванов", "Петров", "Сидоров", "Ткаченко", "Авраменко", "Татаренко", "Морозов", "Колесников", "Кузьменко",
          "Беленко"]
    g2 = ["Дубовик", "Васильченко", "Олейниченко", "Крамаренко", "Самойленко", "Акулова", "Захаров", "Бондаренко",
          "Макарова", "Шевченко"]
    t1 = random.sample(g1, 5)
    t2 = random.sample(g2, 5)
    s = tuple(t1 + t2)
    sort = tuple(sorted(s))
    print("Группа 1: ", ', '.join(g1))
    print("Группа 2: ", ', '.join(g2))
    print("Спортивная команда: ", ', '.join(s))
    print("Длина кортежа:", len(s))
    print("Отсортированная команда: ", ', '.join(sort))
    ivanov = s.count('Иванов')
    if ivanov > 0:
        print("Студент Иванов входит в команду.")
        print("Количество раз, которое фамилия Иванов встречается в команде:", ivanov)
    else:
        print("Студент Иванов не входит в команду.")
z54()

def z61():
    a = {
        "Украина": "Киев"
        "Россия": "Москва",
        "Германия": "Берлин",
        "Франция": "Париж",
        "Италия": "Рим",
        "Китай": "Пекин",
        "Япония": "Токио"
    }
    print("Пары страна - столица:")
    for country, capital in a.items():
        print(country, ":", capital)
        country = input("Введите название страны: ")
        if country in a:
            print("Столица страны ", country, ":", a.get(country))
        else:
            print("Такой страны нет в словаре.")
            s = sorted(a.keys())
            print("В алфавитном порядке по стране:")
            for key in s:
                print(key, "-", a[key])

def z62():
    a = {
        'А': 1, 'В': 1, 'Е': 1, 'И': 1, 'Н': 1, 'О': 1, 'Р': 1, 'С': 1, 'Т': 1,
        'Д': 2, 'К': 2, 'Л': 2, 'М': 2, 'П': 2, 'У': 2,
        'Б': 3, 'Г': 3, 'Ё': 3, 'Ь': 3, 'Я': 3,
        'Й': 4, 'Ы': 4,
        'Ж': 5, 'З': 5, 'Х': 5, 'Ц': 5, 'Ч': 5,
        'Ш': 8, 'Э': 8, 'Ю': 8,
        'Ф': 10, 'Щ': 10, 'Ъ': 10
    }
    b = input("Введите слово: ").upper()
    s = sum(a.get(i) for i in b)
    print("Стоимость слова: ", s)

def z63():
    a = set()
    b = {
        "Ткаченко": ["английский", "французский", "украинский"],
        "Пономаренко": ["польский", "украинский", "узбекский"],
        "Татаренко": ["английский", "немецкий", "китайский" ],
        "Шматов": ["русский", "латинский"],
        "Крамаренко": ["итальянский", "китайский", "португальский"]
    }
    for student, b in b.items():
        a.update(b)
        sorted_a = sorted(list(a))
        print("Отсортированный список языков, которые знают студенты:")
        for language in sorted_a:
            print("-", a)
            chinese_speakers = [student for student, b in b.items()
                                if"китайский" in b]
            print("Студенты, которые знают китайский язык:")
            for student in chinese_speakers:
                print("-", student)


from PIL import Image, ImageFilter
import os
def z91():
        output_folder = 'p1'
        os.makedirs(output_folder)

        for filename in os.listdir('.'):
            if filename.endswith('.jpg'):
                with Image.open(filename) as img:
                    pr_img = img.filter(ImageFilter.CONTOUR)
                    pr_img.save(os.path.join(output_folder, 'new_' + filename))

    def z92():
        itogST = 0
        shopping_list = []

        with open('данные.csv', 'r') as file:
            lines = file.readlines()
            for line in lines:
                data = line.strip().split(',')
                if len(data) == 3:
                    product, quantity, price = data
                    cost = int(quantity) * int(price)
                    itogST += cost
                    shopping_list.append(f"{product} - {quantity} шт. за {price} руб.")

        print("Нужно купить:")
        for i in shopping_list:
            print(i)

        print(f"Итоговая сумма: {itogST} руб.")

def z101():
    with open('products.json', encoding='utf-8') as file:
        d = json.load(file)

    for product in d['products']:
        print("Название:", product['name'])
        print("Цена:", product['price'])
        print("Вес:", product['weight'])

        if product['available']:
            print("В наличии")
        else:
            print("Нет в наличии!")

def z102():
    with open('1.json', 'r', encoding='utf-8') as f:
        d = json.load(f)
        d2 = d['products']
        print('Добавление новой записи')
        n = input('введите название продукта: ')
        p = int(input('введите цену: '))
        a = input('товар в наличии?: ')
        w = int(input('введите вес: '))
        newpr = {}
        newpr['name'] = n
        newpr['price'] = p
        if a == 'да':
                newpr['available'] = True
            elif a == 'нет':
                newpr['available'] = False
            else:
                newpr['available'] = 'ошибка ввода значения'
            newpr['weight'] = w
            d['products'].append(newpr)
            with open('1.json', 'w', encoding='utf-8') as f:
                json.dump(d, f, ensure_ascii=False, indent=4)
                print(' ')
                print('итоговый файл:')
                for i in d['products']:
                    print('Название:', i['name'])
                    print('Цена:', i['price'])
                    print('Вес:', i['weight'])
                    if i['available']:
                        print('В наличии')
                    else:
                        print('Нет в наличии')

def z103():
    with open('en-ru.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines()

    ru_en_dict = {}

    for line in lines:
        en_word, ru_translation = line.strip().split(' - ')
        if ru_translation in ru_en_dict:
            ru_en_dict[ru_translation].append(en_word)
        else:
            ru_en_dict[ru_translation] = [en_word]

    with open('ru-en.txt', 'w', encoding='utf-8') as file:
        for ru_word in sorted(ru_en_dict.keys()):
            en_words = ', '.join(sorted(ru_en_dict[ru_word]))
            file.write(f"{ru_word} - {en_words}")








