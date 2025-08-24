while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter a todo: ") + "\n"

            file = open('todos.txt', 'r')   # r = read
            todos = file.readlines()
            file.close()    #NOTE: always close the file.

            todos.append(todo)

            file = open('todos.txt', 'w')   # w = write
            file.writelines(todos)
            file.close()
        case "show" | 'display':
            file = open('todos.txt', 'r')
            todos = file.readlines()
            file.close()

            new_todos = []
            for item in todos:
                new_item = item.strip('\n')
                new_todos.append(new_item)

            for index, item in enumerate(new_todos):
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
