import random
import threading
import shutil
import os
from os import path


def test_article():
    articles = os.listdir('./catalog1')
    for article in articles:
        with open('catalog1/' + article, 'r', encoding="utf8") as file:
            for line in file:
                number = line    # дістаємо число з тексту
                break

        source_path = 'catalog1/'+article
        if path.exists(source_path):
            if int(number) % 2 == 0:                  # Сортуємо статті в залежності від того чи парне число
                destination_path = "catalog2"
                shutil.move(source_path, destination_path)
            else:
                destination_path = "catalog3"
                shutil.move(source_path, destination_path)


def sort_article():      # Приймаємо на вході масив зі статтями
    thread = []
    t = threading.Thread(target=test_article)
    thread.append(t)
    t.start()

    for t in thread:
        t.join()


def create_article(count):
    arr = ['Щастя – це талант цінувати те, що у тебе є, а не те, чого немає. – Вуді Аллен',
           'Щоб бути щасливим, треба жити в своєму власному раю! Невже ви думали, що один і той же рай може задовольнити всіх людей без винятку? – Марк Твен',
           'Протягом кожної хвилини, що ви злитеся, ви втрачаєте 60 секунд щастя. – Ральф Уолдо Емерсон',
           'Щастя живе в простих речах – у тому, наприклад, що є людина, яка щоночі просто обіймає тебе. – Марта Кетро',
           'Яка різниця, хто сильніший, хто розумніший, хто красивіший, хто багатший? Адже, в кінцевому підсумку, має значення тільки те, щаслива ти людина чи ні. – Ошо',
           'Люди можуть бути щасливі лише за умови, що вони не вважають щастя метою життя. – Джордж Оруелл',
           'Багато хто шукає щастя в сферах вище свого рівня, інші – нижче. Але щастя одного зросту з людиною. – Конфуцій']

    for i in range(count):
        article = ''
        number = random.randint(1, 1000)
        article += str(number) + ' '
        for _ in range(1000):
            index = random.randint(0, 6)
            article += '\n' + arr[index]

        route = f'catalog1/article{i}.txt'
        with open(route, 'w', encoding="utf8") as file:
            file.write(article)


if __name__ == "__main__":
    create_article(10)
    sort_article()

























