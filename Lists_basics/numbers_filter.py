n = int(input())
numbers = []
filtered = []

for i in range(n):
    current_number = int(input())
    numbers.append(current_number)

command = input()

if command == "even":
    for num in numbers:
        if num % 2 == 0:
            filtered.append(num)
elif command == "odd":
    for num in numbers:
        if num % 2 != 0:
            filtered.append(num)
elif command == "positive":
    for num in numbers:
        if num >= 0:
            filtered.append(num)
elif command == "negative":
    for num in numbers:
        if num < 0:
            filtered.append(num)

print(filtered)

