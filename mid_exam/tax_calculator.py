vehicle_info = input().split(">>")

total_tax_collected = 0

for vehicle in vehicle_info:
    type_of_car, years, kilometers = vehicle.split()
    years = int(years)
    kilometers = int(kilometers)

    if type_of_car == "family":
        initial_tax = 50
        tax_decline_per_year = 5
        tax_increase_per_distance = 12
    elif type_of_car == "heavyDuty":
        initial_tax = 80
        tax_decline_per_year = 8
        tax_increase_per_distance = 14
    elif type_of_car == "sports":
        initial_tax = 100
        tax_decline_per_year = 9
        tax_increase_per_distance = 18
    else:
        print("Invalid car type.")
        continue

    if type_of_car == "family":
        total_tax = initial_tax - (tax_decline_per_year * years) + (tax_increase_per_distance * (kilometers // 3000))
    elif type_of_car == "heavyDuty":
        total_tax = initial_tax - (tax_decline_per_year * years) + (tax_increase_per_distance * (kilometers // 9000))
    elif type_of_car == "sports":
        total_tax = initial_tax - (tax_decline_per_year * years) + (tax_increase_per_distance * (kilometers // 2000))

    total_tax_collected += total_tax

    print(f"A {type_of_car} car will pay {total_tax:.2f} euros in taxes.")

print(f"The National Revenue Agency will collect {total_tax_collected:.2f} euros in taxes.")
