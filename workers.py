import csv

# name, price, speed, mark
# Car5,5,50,Mark5


# name, mark, price, speed


def read_csv(filename: str) -> list:
    data = []
    with open(filename, newline="") as csvf:
        reader = list(csv.reader(csvf))
        data = reader
    return data


def serializer(data: list[list], keys: list[str]) -> list:
    data_keys = data[0]
    data = data[1:]
    swap_items = []
    return_data = []

    if not len(data_keys) == len(keys):
        return []
    if not data_keys == keys:
        for i in range(len(data_keys)):
            if keys[i] != data_keys[i]:
                swap_items.append((i, keys.index(data_keys[i])))

    for row in data:
        save_row = row.copy()
        for item in swap_items:
            row[item[0]] = save_row[item[1]]

    new_dict = {}
    # ['Car1', 'Mark1', 5, 50]
    # {'name': 'Car1', 'mark': 'Mark1', 'price': 5', 'speed': 50}
    for row in data:
        new_dict = {}
        for key in keys:
            new_dict[key] = row[keys.index(key)]
        return_data.append(new_dict)

    return return_data