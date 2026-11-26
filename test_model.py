from models import Classroom
from exceptions import InvalidClassroomError


#Создание допустимой и недопустимой сущности

auditorium = Classroom(
    "A1291",
    "Лекционная аудитория",
    "lecture",
    2012,
    "А",
    100
)

print("Допустимая сущность:", isinstance(auditorium, Classroom))


#Пустой ID
try:
    Classroom("", "Лекционная аудитория", "lecture", 2017, "А", 100)
except InvalidClassroomError:
    print("Пустой ID")


#Некорректный год
try:
    Classroom("B1292", "Компьютерный класс", "computer", -1998, "Б", 30)
except InvalidClassroomError:
    print("Некорректный год")


#Некорректное число мест
try:
    Classroom("A1293", "Семинарская аудитория", "seminar", 2017, "В", 0)
except InvalidClassroomError:
    print("Некорректная вместимость")


#Некорректный тип года
try:
    Classroom("B1294", "Аудитория", "lecture", "2012", "А", 100)
except InvalidClassroomError:
    print("Год должен быть числом" )


#Некорректный тип вместимости
try:
    Classroom("A1295", "Аудитория", "lecture", 1998, "А", "100")
except InvalidClassroomError:
    print("Вместимость должна быть задана числом")


#Проверка нулевой вместимости
try:
    Classroom("A1297", "Аудитория", "lecture", 2012, "А", -15)
except InvalidClassroomError:
    print("Отрицательная вместимость")


#Некорректный тип названия
try:
    Classroom("B1298", 123, "lecture", 2017, "А", 100)
except InvalidClassroomError:
    print("Название должно быть задано строкой")


# Некорректный тип ID
try:
    Classroom(123, "Аудитория", "lecture", 1998, "А", 100)
except InvalidClassroomError:
    print("ID должно быть задано строкой")


#Некорректный тип категории
try:
    Classroom("A1299", "Аудитория", 123, 2012, "А", 100)
except InvalidClassroomError:
    print("Категория должна быть задана строкой")


#Некорректный тип корпуса
try:
    Classroom("B1300", "Аудитория", "lecture", 2017, 123, 100)
except InvalidClassroomError:
    print("Корпус должен быть задан строкой")