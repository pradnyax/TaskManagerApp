while True:
    # Get user input & strip space chars from it.
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter a todo: ") + "\n"

            # OPTIMISING THE CODE by using CONTEXT MANAGER - with
            with open('todos.txt', 'r') as file:
                todos = file.readlines()
            # Also, with context manager, you don't need to close the file.

            todos.append(todo)

            with open('todos.txt', 'w') as file:
                file.writelines(todos)

        case "show" | 'display':
            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            for index, item in enumerate(todos):
                item = item.strip('\n')
                row = f"{index + 1}-{item}"
                print(row)
        case "edit":
            number = int(input("Enter the todo no. to edit: "))
            number = number - 1   #because list indexing starts from 0, so when user writes 2, its actually 1. (has done this -1 or +1 on other lines of code too!)
            new_todo = input("Enter new todo: ")
            todos[number] = new_todo
        case 'complete':
            number = int(input("Enter a todo no. to mark complete: "))
            todos.pop(number - 1)
        case "exit":
            break
        # case _:
        #     print("Invalid input! Try again.")

print("Bye!")
