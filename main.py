# print("HEllO WORLD")

cars = [
    {"name": "Car1", "mark": "Mark1", "price": 1290000, "speed": 150},
    {"name": "Car2", "mark": "Mark2", "price": 2455566, "speed": 300},
    {"name": "Car3", "mark": "Mark1", "price": 1234800, "speed": 240}
]

# Search
def search_cars(name: str = "", mark: str = "", price: float = 0.00, speed: float = 0) -> list:
    result: list = []
    domain: list = []
    if name:
        domain.append(name)
    if mark:
        domain.append(mark)
    if price:
        domain.append(price)
    if speed:
        domain.append(speed)
    for car in cars:
        car_values = car.values()
        if set(domain).issubset(set(car_values)):
            result.append(car)
    return result

# Create
def create_car(new_car: dict) -> dict:
    cars.append(new_car)
    return new_car

# Read
def read_cars() -> list:
    return cars

def read_car(car: dict) -> list:
    result: list = []
    search_result = search_cars(car.get("name"), car.get("mark"), car.get("price"), car.get("speed"))
    for car in search_result:
        result.append(car)
    return result

# Update
def update_car(name: str, new_car: dict = {}) -> dict:
    car = search_cars(name)[0]
    index = cars.index(car)
    cars.remove(car)
    for key in car:
        if key in new_car:
            car[key] = new_car[key]
    cars.insert(index, car)
    return car

        # Delete
def delete_car(name: str) -> dict:
    carr = search_cars(name)[0]
    cars.remove(carr)
    return carr

# Тест
print(read_cars())
print(update_car(name="Car1",new_car={"price": 312456}))
print(read_cars())