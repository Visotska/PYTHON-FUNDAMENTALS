def process_commands():
    spell = input()

    while True:
        command = input()
        if command == "Abracadabra":
            break
        parameters = command.split()

        if parameters[0] == "Abjuration":
            spell = spell.upper()
            print(spell)

        elif parameters[0] == "Necromancy":
            spell = spell.lower()
            print(spell)

        elif parameters[0] == "Illusion":
            index = int(parameters[1])
            letter = parameters[2]
            if 0 <= index < len(spell):
                spell = spell[:index] + letter + spell[index+1:]
                print("Done!")
            else:
                print("The spell was too weak.")

        elif parameters[0] == "Divination":
            first_substring = parameters[1]
            second_substring = parameters[2]
            if first_substring in spell:
                spell = spell.replace(first_substring, second_substring)
                print(spell)

        elif parameters[0] == "Alteration":
            substring = parameters[1]
            if substring in spell:
                spell = spell.replace(substring, "")
                print(spell)
        else:
            print("The spell did not work!")


process_commands()
