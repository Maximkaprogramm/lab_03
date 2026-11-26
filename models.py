from dataclasses import dataclass
from exceptions import InvalidClassroomError

@dataclass
class Classroom:
    item_id: str
    name: str
    category: str
    year: int
    building: str
    capacity: int

    def __post_init__(self):
        if not isinstance(self.item_id, str) or not self.item_id or len(self.item_id.strip()) <= 0:
            raise InvalidClassroomError("Пустое поле id")
        if not isinstance(self.name, str) or not self.name or len(self.name.strip()) <= 0:
            raise InvalidClassroomError("Неверное наименование")
        if not isinstance(self.category, str) or not self.category or len(self.category.strip()) <= 0:
            raise InvalidClassroomError("Неверная категория")
        if not isinstance(self.building, str) or not self.building or len(self.building.strip()) <= 0:
            raise InvalidClassroomError("Пустое поле building")
        if not isinstance(self.year, int) or isinstance(self.year, bool):
            raise InvalidClassroomError("Неверный тип атрибута year")
        if not isinstance(self.capacity, int) or isinstance(self.capacity, bool):
            raise InvalidClassroomError("Неверный тип атрибута capacity")
        if self.year <= 0:
            raise InvalidClassroomError("Год некорректен")
        if self.capacity <= 0:
            raise InvalidClassroomError("Некорректное число мест в аудитории")


