from models import Classroom
from catalog import ClassroomCatalog
from storage import save_catalog, load_catalog
from exceptions import InvalidCatalogFileError, UnsupportedFormatVersionError
import os
import json


#Round Trip JSON

catalog = ClassroomCatalog()
catalog.add(Classroom(
    "A1291",
    "Лекционная аудитория",
    "lecture",
    2012,
    "Б",
    57
))

catalog.add(Classroom(
    "B1292",
    "Компьютерный класс",
    "computer",
    2017,
    "В",
    31
))

file_path = "test_data.json"

save_catalog(catalog, file_path)
print("Файл сохранён:", os.path.exists(file_path))

# Запоминаем количество объектов
start_count = len(catalog)

# Очищаем каталог
for auditorium in list(catalog):
    catalog.remove(auditorium.item_id)

print("После очистки:", len(catalog))


load_catalog(catalog, file_path)
print("После загрузки:", len(catalog))

# Проверяем восстановленные объекты
for auditorium in catalog:
    print(auditorium.item_id, auditorium.name, auditorium.category,
          auditorium.year, auditorium.building, auditorium.capacity)

print("Количество восстановлено:", len(catalog) == start_count)
print("A1291 восстановлен:", "A1291" in catalog)

os.remove(file_path)


#Повреждённый JSON

catalog = ClassroomCatalog()
catalog.add(Classroom("B1293", "Существующая аудитория",
                  "lecture", 1998, "Г", 67))

file_path = "broken.json"
with open(file_path, "w", encoding="utf-8") as file:
    file.write("некорректный json ")

try:
    load_catalog(catalog, file_path)
except InvalidCatalogFileError:
    print("Повреждённый JSON")

print("B1293 сохранился:", "B1293" in catalog)


#Неподдерживаемая версия

file_path = "version.json"
data = {
    "format_version": 2,
    "items": []
}

with open(file_path, "w", encoding="utf-8") as file:
    json.dump(data, file)

try:
    load_catalog(catalog, file_path)
except UnsupportedFormatVersionError:
    print("Неизвестная версия")

print("B1293 после ошибки сохранился:", "B1293" in catalog)


os.remove("broken.json")
os.remove("version.json")


#Отсутствие изменения при ошибке

catalog = ClassroomCatalog()
catalog.add(Classroom("A1294", "Существующая аудитория",
                  "lecture", 2017, "Д", 57))

file_path = "partial.json"

data = {
    "format_version": 1,
    "items": [
        {
            "item_id": "B1295",
            "name": "Лекционная",
            "category": "lecture",
            "year": 2012,
            "building": "Б",
            "capacity": 31
        },
        {
            "item_id": "A1296",
            "name": "Компьютерная",
            "category": "computer",
            "year": 1998,
            "building": "В",
            "capacity": 67
        },
        {
            "item_id": "B1297",
            "name": "Семинарская",
            "category": "seminar",
            "year": 2017,
            "building": "Г",
            "capacity": -10
        }
    ]
}

with open(file_path, "w", encoding="utf-8") as file:
    json.dump(data, file, ensure_ascii=False, indent=2)

try:
    load_catalog(catalog, file_path)
except InvalidCatalogFileError:
    print("Ошибка загрузки")

print("Количество объектов:", len(catalog))
print("A1294 существует:", "A1294" in catalog)
print("B1295 отсутствует:", "B1295" not in catalog)
print("A1296 отсутствует:", "A1296" not in catalog)

os.remove(file_path)