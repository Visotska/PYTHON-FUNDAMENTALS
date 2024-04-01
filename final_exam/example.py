import re


def message_decryption():
    input_count = int(input())
    pattern = r"^([$%])([A-Z][a-z]{2,})\1: \[([0-9]+)\]\|\[([0-9]+)\]\|\[([0-9]+)\]\|$"

    for i in range(input_count):
        message = input()
        match = re.match(pattern, message)
        if match:
            tag = match.group(2)
            decrypted_message = chr(int(match.group(3))) + chr(int(match.group(4))) + chr(int(match.group(5)))
            print(f"{tag}: {decrypted_message}")
        else:
            print("Valid message not found!")


message_decryption()
