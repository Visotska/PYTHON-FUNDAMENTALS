num = int(input())
for first_symbol in range(0, num):
    for second_symbol in range(0, num):
        for third_symbol in range(0, num):
            print(f'{chr(first_symbol+97)}{chr(second_symbol+97)}{chr(third_symbol+97)}')