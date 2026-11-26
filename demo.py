from models import Classroom
from catalog import ClassroomCatalog
from storage import save_catalog, load_catalog
import os

catalog = ClassroomCatalog()


aud1 = Classroom("B392", "Лекционная аудитория", "lecture", 2012, "B", 120)
aud2 = Classroom("C1012", "Компьютерный класс", "computer", 2018, "C", 17)
aud3 = Classroom("B121", "Семинарская аудитория", "seminar", 2023, "В", 27)


catalog.add(aud1)
catalog.add(aud2)
catalog.add(aud3)

print("Все аудитории из каталога:")

for aud in catalog:
    print(
        aud.item_id,
        aud.name,
        aud.category,
        aud.year,
        aud.building,
        aud.capacity
    )
print()
print("Поиск аудитории категории lecture:")
found = catalog.find_by_category("lecture")

for aud in found:
    print(aud.item_id, aud.name)


print()
print("Поиск аудитории по названию:")
found = catalog.find_by_name("компьютер")

for aud in found:
    print(aud.item_id, aud.name)


print()
print("Получение аудитории по ID:")
aud = catalog.get("B392")
print(aud.name)

print()
print("Удаление аудитории:")
catalog.remove("B121")

print("Количество аудиторий после удаления:", len(catalog))
print("B121 находится в каталоге:", "B121" in catalog)



print()
print("Сохранение каталога в json-файл:")
filepath = "demo_data.json"
save_catalog(catalog, filepath)

print("Каталог сохранён в файл:", filepath)


new_catalog = ClassroomCatalog()
print("Количество объектов до загрузки:", len(new_catalog))



load_catalog(new_catalog, filepath)
print("Количество объектов после загрузки:", len(new_catalog))

print()
print("Аудитории после загрузки:")

for aud in new_catalog:
    print(aud.item_id, aud.name)

os.remove(filepath)