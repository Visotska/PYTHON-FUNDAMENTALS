import math

budget = float(input())
students = int(input())
flour_price = float(input())
egg_price = float(input())
apron_price = float(input())



free_flour_packages = students // 5
total_flour_packages = students * flour_price - free_flour_packages * flour_price
total_eggs = students * 10.0
total_aprons = math.ceil(students * 1.20)

total_cost = total_flour_packages + (total_eggs * egg_price) + (total_aprons * apron_price)


if total_cost <= budget:
    print(f"Items purchased for {total_cost:.2f}$.")
else:
    needed_money = total_cost - budget
    print(f"{needed_money:.2f}$ more needed.")
