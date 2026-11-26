
from models import Classroom
from exceptions import ClassroomNotFoundError, DuplicateClassroomError, InvalidClassroomError

class ClassroomCatalog:
    """Итерация каталога учебных аудиторий выполняется в порядке добавления объектов."""
    def __init__(self):
        self._items = {}

    def add(self, item) -> None:
        if isinstance(item, Classroom):
            item_id = item.item_id
            if item_id in self._items:
                raise DuplicateClassroomError("Такой объект уже есть")
            else:
                self._items[item_id] = item
        else:
            raise InvalidClassroomError("Некорректный объект")
        

    def get(self, item_id):
        if item_id not in self._items:
            raise ClassroomNotFoundError("Такой аудитории нет")
        else:
            return self._items[item_id]
    
    def remove(self, item_id):
        if item_id not in self._items:
            raise ClassroomNotFoundError("Данной аудитории нет")
        else:
            del self._items[item_id]

    def find_by_category(self, category):
        res_category = []
        for obj in self._items.values():
            if obj.category == category:
                res_category.append(obj)
        return res_category

    def find_by_name(self, query):
        result = []
        for obj in self._items.values():
            if query.lower() in obj.name.lower():
                result.append(obj)
        return result

    def __len__(self):
        return len(self._items)

    def __iter__(self):
        #Возврат аудитории в порядке добавления в каталог
        return iter(self._items.values())

    def __contains__(self, item_id):
        if item_id in self._items:
            return True
        return False
