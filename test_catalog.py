from models import Classroom
from catalog import ClassroomCatalog
from exceptions import DuplicateClassroomError, ClassroomNotFoundError


# Добавление, получение и удаление аудиторий

catalog = ClassroomCatalog()

auditorium = Classroom("A1291", "Лекционная аудитория", "lecture", 2012, "Б", 57)

catalog.add(auditorium)

print("Добавление:", "A1291" in catalog)
print("Получение:", catalog.get("A1291") == auditorium)
print("Количество объектов:", len(catalog))

catalog.remove("A1291")

print("Удаление:", "A1291" not in catalog)
print("Количество после удаления:", len(catalog))


#Проверка дубликата ID

catalog.add(auditorium)

try:
    another_auditorium = Classroom("A1291", "Другая аудитория", "seminar", 2017, "В", 31)
    catalog.add(another_auditorium)
except DuplicateClassroomError:
    print("Дубликат ID: исключение обработано")

print("Количество после попытки дубликата:", len(catalog))


#Поиск по категории и имени

catalog = ClassroomCatalog()

catalog.add(Classroom("B1292", "Лекционная аудитория", "lecture", 2012, "Г", 57))

catalog.add(Classroom("A1293", "Большая лекционная", "lecture", 1998, "Д", 67))

catalog.add(Classroom("B1294", "Компьютерный класс", "computer", 2017, "Е", 31))

found_category = catalog.find_by_category("lecture")
print("Поиск по категории:", [item.item_id for item in found_category])

found_name = catalog.find_by_name("ЛЕКЦИОННАЯ")

print("Несуществующая категория:", len(catalog.find_by_category("laboratory")) == 0)

print("Несуществующее название:", len(catalog.find_by_name("Библиотека")) == 0)

print("Поиск по имени:", [item.item_id for item in found_name])



#Проверка порядка итерации

catalog = ClassroomCatalog()

auditoriums = [
    Classroom("A1295", "Лекционная", "lecture", 2012, "Б", 57),
    Classroom("B1296", "Компьютерная", "computer", 2017, "В", 31),
    Classroom("A1297", "Семинарская", "seminar", 1998, "Г", 67)
]

for auditorium in auditoriums:
    catalog.add(auditorium)

result = [item.item_id for item in catalog]
expected = ["A1295", "B1296", "A1297"]

print("Порядок итерации:", result)
print("Порядок сохранён:", result == expected)
