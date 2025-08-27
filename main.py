while True:
    # Get user input & strip space chars from it.
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    # if 'add' in user_action or 'new' in user_action:
    if user_action.startswith("add"):
        todo = user_action[4:]      #list slicing operation

        with open('todos.txt', 'r') as file:
            todos = file.readlines()

        todos.append(todo + '\n')

        with open('todos.txt', 'w') as file:
            file.writelines(todos)

    # elif "show" in user_action:
    elif user_action.startswith("show"):

        with open('todos.txt', 'r') as file:
            todos = file.readlines()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}-{item}"
            print(row)

    # elif "edit" in user_action:
    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            print(number)
            number = number - 1   #because list indexing starts from 0, so when user writes 2, its actually 1. (has done this -1 or +1 on other lines of code too!)

            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + '\n'

            with open('todos.txt', 'w') as file:
                file.writelines(todos)
        except ValueError:
            print("Invalid command.")
            continue        #continue jumps back to the beginning.

    # elif 'complete' in user_action:
    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])

            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            with open('todos.txt', 'w') as file:
                file.writelines(todos)

            message = f"Todo {todo_to_remove} was removed from the list."
            print(message)
        except IndexError:
            print("Invalid! There is no item with that number.")
            continue

    # elif "exit" in user_action:
    elif user_action.startswith("exit"):
        break
    else:
        print("Invalid command!!!")

print("Bye!")
