def process_todo_notes():
    todo_notes = []

    while True:
        note = input().strip()

        if note == 'End':
            break

        if not note:
            continue

        if '-' not in note:
            print(f"Invalid note format: {note}")
            continue

        todo_notes.append(note)

    sorted_notes = sorted(todo_notes, key=lambda x: int(x.split('-')[0]))
    task_list = [note.split('-', 1)[1] for note in sorted_notes]

    return task_list

result = process_todo_notes()
print(result)
