END_COMMAND = 'End'
ADD_COMMAND = 'add'
INSERT_COMMAND = 'insert'
LEAVE_COMMAND = 'leave'


def process_command(wagons, command, *args):
    if command == END_COMMAND:
        print(wagons)
        return wagons, False

    if command == ADD_COMMAND:
        wagons[-1] += args[0]
    elif command == INSERT_COMMAND:
        index, people = args
        wagons[index] += people
    elif command == LEAVE_COMMAND:
        index, people = args
        wagons[index] -= people

    return wagons, True


def main():
    wagons = [0] * int(input())

    while True:
        command_input = input().split()

        if not command_input:
            continue

        command = command_input[0]
        args = list(map(int, command_input[1:]))

        wagons, continue_processing = process_command(wagons, command, *args)

        if not continue_processing:
            break


if __name__ == '__main__':
    main()