money_as_string = input().split(', ')
count_of_beggars = int(input())
money_as_integers = []
for money in money_as_string:
    money_as_integers. append(int(money))
final_sums = []
start_index = 0
for current_beggar in range(count_of_beggars):
    current_beggar_sum = 0
    for current_index in range(start_index, len(money_as_integers), count_of_beggars):
        current_beggar_sum += money_as_integers[current_index]
    final_sums. append(current_beggar_sum)
    start_index += 1
print(final_sums)
