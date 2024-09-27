# Test Database
toys = [
    {"name": "Toy1", "category": "Category1", "price": 25.15, "amount": 15},
    {"name": "Toy2", "category": "Category2", "price": 13.13, "amount": 3},
    {"name": "Toy3", "category": "Category1", "price": 25.23, "amount": 11}
]

# Search
def search_toys(name: str = "", category: str = "", price: float = 0.00, amount: float = 0) -> list:
    result: list = []
    domain: list = []
    if name:
        domain.append(name)
    if category:
        domain.append(category)
    if price:
        domain.append(price)
    if amount:
        domain.append(amount)
    for toy in toys:
        toy_values = toy.values()
        if set(domain).issubset(set(toy_values)):
            result.append(toy)
    return result

# Create
def create_toy(new_toy: dict) -> dict:
    toys.append(new_toy)
    return new_toy

# Read
def read_toys() -> list:
    return toys

def read_toy(toy: dict) -> list:
    result: list = []
    search_result = search_toys(toy.get("name"), toy.get("category"), toy.get("price"), toy.get("amount"))
    for toy in search_result:
        result.append(toy)
    return result

# Update
def update_toy(name: str, new_toy: dict = {}) -> dict:
    toy = search_toys(name)[0]
    index = toys.index(toy)
    toys.remove(toy)
    new_toy = {}
    for key in toy:
        if key in new_toy:
            toy[key] = new_toy[key]
    toys.insert(index, toy)
    return toy

# Delete
def delete_toy(name: str) -> dict:
    toy = search_toys(name)[0]
    toys.remove(toy)
    return toy


