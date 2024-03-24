number = int(input())

for current_num in range(1, number + 1):
    string_of_cn = str(current_num)
    sum_of_numbers = 0
    for digit in string_of_cn:
        sum_of_numbers += int(digit)
    special_num = False

    if sum_of_numbers == 5 or sum_of_numbers == 7 or sum_of_numbers == 11:
        special_num = True
    print(f"{current_num} -> {special_num}")
