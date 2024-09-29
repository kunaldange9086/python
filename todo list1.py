def todo_list():
    todos = []
    while True:
        todo = input("Enter a task (or 'quit' to exit): ")
        if todo.lower() == 'quit':
            break
        todos.append(todo)
    print("Your To-Do List:")
    for task in todos:
        print(f"- {task}")

todo_list()
