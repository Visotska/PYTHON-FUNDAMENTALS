lost_fights_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

broken_helmets = lost_fights_count // 2
broken_swords = lost_fights_count // 3
broken_shields = lost_fights_count // (2*3)
broken_armors = broken_shields // 2

expenses = helmet_price * broken_helmets +\
           sword_price * broken_swords +\
           shield_price * broken_shields +\
           armor_price * broken_armors

print(f"Gladiator expenses: {expenses:.2f} aureus")
