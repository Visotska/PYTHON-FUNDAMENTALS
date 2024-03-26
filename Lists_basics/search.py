number = int(input())
searched_word = input()
strings = []

for i in range(number):
    current_string = input()
    strings.append(current_string)
print(strings)
for i in range(len(strings)-1, -1, -1):
    element = strings[i]
    if searched_word not in element:
        strings.remove(element)
print(strings)


