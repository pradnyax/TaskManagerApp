todos = []
while True:
    user_action = input("Type add, show, edit or exit: ")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter a todo: ")
            todos.append(todo)
        case "show" | 'display':
            for index, item in enumerate(todos):
                row = f"{index}-{item}"
                print(row)
        case "edit":
            number = int(input("Enter the todo no. to edit: "))
            number = number - 1   # because list indexing starts from 0, so when user writes 2, its actually 1.
            new_todo = input("Enter new todo: ")
            todos[number] = new_todo
        case "exit":
            break
        # case _:
        #     print("Invalid input! Try again.")

print("Bye!")
