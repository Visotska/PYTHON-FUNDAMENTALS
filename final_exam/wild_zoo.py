animal_info = {}
area_counts = {}

while True:
    command = input()
    if command == "EndDay":
        break

    action, data = command.split(": ")

    if action == "Add":
        name, food_quantity, area = data.split("-")
        food_quantity = int(food_quantity)

        if name not in animal_info:
            animal_info[name] = {"food_quantity": food_quantity, "area": area}
            if area not in area_counts:
                area_counts[area] = 1
            else:
                area_counts[area] += 1
        else:
            animal_info[name]["food_quantity"] += food_quantity

    elif action == "Feed":
        name, food = data.split("-")
        food = int(food)

        if name in animal_info:
            animal_info[name]["food_quantity"] -= food
            if animal_info[name]["food_quantity"] <= 0:
                print(f"{name} was successfully fed")
                area_counts[animal_info[name]["area"]] -= 1
                del animal_info[name]

print("Animals:")
for animal, info in animal_info.items():
    print(f" {animal} -> {info['food_quantity']}g")

print("Areas with hungry animals:")
for area, count in area_counts.items():
    if count > 0:
        print(f" {area}: {count}")