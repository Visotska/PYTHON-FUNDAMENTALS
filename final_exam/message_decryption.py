import re


def message_decryption():
    input_count = int(input())
    pattern = r"([$%])([A-Z][a-z]{2,})\1: (\[(\d+)\]\|){3}$"

    for i in range(input_count):
        message = input()
        match = re.fullmatch(pattern, message)

        if match is None:
            print("Valid message not found!")
            continue

        tag = match.group(2)
        numbers = [int(num) for num in match.group(4).split("|")[:-1]]
        decrypted_message = "".join(chr(num) for num in numbers)

        print(f"{tag}: {decrypted_message}")


message_decryption()
