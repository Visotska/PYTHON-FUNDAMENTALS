n = int(input())
positive = []
negative = []

for _ in range (n):
    current_element = int(input())
    if current_element >= 0:
        positive.append(current_element)
    else:
        negative.append(current_element)

print(positive)
print(negative)
print(f'Count of positives: {len(positive)}'
      f'Sum of negatives: {sum(negative)}')