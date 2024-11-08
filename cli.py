from main import create, remove, write
from workers import read_csv, serializer
from models import Car
import os
while True:
    os.system("clear")
    print("1 - Створити новий предмет")
    print("2 - Занести предмети з файлу")
    print("3 - Видалити предмет")
    print("4 - Оновити предмет.")
    print("5 - Вийти.")
    user = input()
    match user:
        case "1":
            os.system("clear")
            print("Ви перейшли в нову вкладку")
            keys = [column.key for column in Car.__table__.columns]
            if "id" in keys:
                keys.remove("id")
            data = {}
            for key in keys:
                data[key] = input(f"{key}: ")
            create(Car, data)
            input()
        case "2":
            os.system("clear")
            print("Ви перейшли вкладку занесення предмета до файлу")
            data = read_csv("data.csv")
            serialized_data = serializer(data,["name", "price", "mark", "speed"])
            for car in serialized_data:
                create(Car, car)
                print(f"Створений рядок з такими даними:{car}")
            input()
        case "3":
            os.system("clear")
            print("Ви перейшли вкладку до видалення предмета")
            name = input("Введіт назву машини, яку хочете видалити: ")
            remove(Car, name)
            print(f"Ви вадалили ось цю машину:{name}")
            input()
        case "4":
            os.system("clear")
            print("Ви перейшли вкладку до оновлення предмета")
            name = input("Введіт назву машини, яку хочете видалити: ")
            keys = [column.key for column in Car.__table__.columns]
            if "id" in keys:
                keys.remove("id")
            data = {}
            for key in keys:
                data[key] = input(f"{key}: ")
            write(Car, name, data)
            print(f"Ви оновили ось цю тачку: {name}")
            input()
        case "5":
            os.system("clear")
            print("Ви вийшли")
            break