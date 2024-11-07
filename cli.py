from main import create
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
            input()
        case "3":
            os.system("clear")
            print("Ви перейшли вкладку до видалення предмета")
            input()
        case "4":
            os.system("clear")
            print("Ви перейшли вкладку до оновлення предмета") 
            input()
        case "5":
            os.system("clear")
            print("Ви вийшли")
            break