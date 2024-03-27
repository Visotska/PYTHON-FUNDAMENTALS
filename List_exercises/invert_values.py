string_of_numbers = input().split()
opposite_numbers = []

for number in string_of_numbers:
    opposite_number = -int(number)
    opposite_numbers.append(opposite_number)

print(opposite_numbers)