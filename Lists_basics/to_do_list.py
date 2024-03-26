def show_menu():
    print('\n=====To-Do List Menu=====')
    print('1.Add tasks')
    print('2.Mark task as completed')
    print('3.View tasks')
    print('4.Quit')


def add_task(todo_list):
    task = input("Enter the task:")
    todo_list.append({'task': task, 'completed': False})
    print(f'Task "{task}" added successfully!!')


def mark_completed(todo_list):
    print('====== Tasks =======')
    display_tasks(todo_list)

    index = int(input('Enter the index of the task to mark as completed!'))

    if 0 <= index < len(todo_list):
        todo_list[index]['completed'] = True
        print("Task marked as completed")
    else:
        print('Invalid index. Please, enter a valid index.')


def display_tasks(todo_list):
    print('====== Tasks =======')
    for i, task in enumerate(todo_list):
        status = '[X]' if task['completed'] else '[ ]'
        print(f"{i}. {status} {task['task']}")


def todo_list_program():
    todo_list = []
    while True:
        show_menu()
        choice = input('Enter your choice (1-4):')

        if choice == '1':
            add_task(todo_list)
        elif choice == '2':
            mark_completed(todo_list)
        elif choice == '3':
            display_tasks(todo_list)
        elif choice == '4':
            print("Exiting the program! Bye !")
            break
        else:
            print("Invalid choice, please enter a number between 1 and 4.")


todo_list_program()
