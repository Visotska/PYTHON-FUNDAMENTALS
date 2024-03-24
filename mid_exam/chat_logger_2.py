class ChatLogger:
    def __init__(self):
        self.chat_history = []

    def add_message(self, message):
        self.chat_history.append(message)

    def remove_message(self, message):
        if message in self.chat_history:
            self.chat_history.remove(message)

    def edit_message(self, message, edited_version):
        if message in self.chat_history:
            index = self.chat_history.index(message)
            self.chat_history[index] = edited_version

    def pin_message(self, message):
        if message in self.chat_history:
            self.chat_history.remove(message)
            self.chat_history.append(message)

    def spam_messages(self, *messages):
        self.chat_history.extend(messages)

    def display_chat_history(self):
        for message in self.chat_history:
            print(message)


# Main program
chat_logger = ChatLogger()

while True:
    command = input().split()
    if command[0] == "end":
        break

    if command[0] == "Chat":
        chat_logger.add_message(" ".join(command[1:]))
    elif command[0] == "Remove":
        chat_logger.remove_message(" ".join(command[1:]))
    elif command[0] == "Edit":
        chat_logger.edit_message(command[1], " ".join(command[2:]))
    elif command[0] == "Pin":
        chat_logger.pin_message(" ".join(command[1:]))
    elif command[0] == "Spam":
        chat_logger.spam_messages(*command[1:])

chat_logger.display_chat_history()
