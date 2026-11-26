import json
from dataclasses import asdict

from catalog import ClassroomCatalog
from models import Classroom
from exceptions import UnsupportedFormatVersionError, InvalidCatalogFileError, InvalidClassroomError, DuplicateClassroomError

FORMAT_VERSION = 1

def save_catalog(catalog: ClassroomCatalog, filepath: str) -> None:
    items = []
    for obj in catalog:
        obj_dict = asdict(obj)
        items.append(obj_dict)    
    
    res_dict = {"format_version": FORMAT_VERSION,
                "items": items}

    with open(filepath, "w", encoding='utf-8') as file:
        json.dump(res_dict, file, ensure_ascii=False, indent=2)

def load_catalog(catalog: ClassroomCatalog, filepath: str) -> None:
    try:
        with open(filepath, "r", encoding="utf-8") as file:
            obj_data = json.load(file)
    except json.JSONDecodeError:
        raise InvalidCatalogFileError("Повреждённый json-файл")

    except (OSError, UnicodeDecodeError):
        raise InvalidCatalogFileError("Файл не может быть прочитан")

    if not (isinstance(obj_data, dict) and "format_version" in obj_data and "items" in obj_data):
        raise InvalidCatalogFileError("Неверная структура json-файла")
    
    if not isinstance(obj_data["items"], list):
        raise InvalidCatalogFileError("Неверный тип items")

    if isinstance(obj_data["format_version"], bool) or not isinstance(obj_data["format_version"], int):
        raise InvalidCatalogFileError("Неверный тип ключа format_version")

    if obj_data["format_version"] != FORMAT_VERSION:
        raise UnsupportedFormatVersionError("Неподдерживаемый файл")
        
    items = obj_data["items"]
    temp_catalog = ClassroomCatalog()
    required_fields = [
    "item_id",
    "name",
    "category",
    "year",
    "building",
    "capacity"
    ]
    for dict_classroom in items:
        if isinstance(dict_classroom, dict):
            for el in required_fields:
                if el not in dict_classroom:
                    raise InvalidCatalogFileError("Отсутствует поле: " + el)
            for field in dict_classroom:
                if field not in required_fields:
                    raise InvalidCatalogFileError("Лишнее поле")
            try:
                classroom = Classroom(
                    dict_classroom["item_id"],
                    dict_classroom["name"],
                    dict_classroom["category"],
                    dict_classroom["year"],
                    dict_classroom["building"],
                    dict_classroom["capacity"]
                )
                temp_catalog.add(classroom)
            except (InvalidClassroomError, DuplicateClassroomError):
                raise InvalidCatalogFileError("Некорректные тип данных в файле")
        else:
            raise InvalidCatalogFileError("Неверный тип элемента словаря dict_classroom")
    catalog._items = temp_catalog._items
