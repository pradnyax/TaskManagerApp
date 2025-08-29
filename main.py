def get_todos(filepath):
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_todos(filepath, todos_arg):
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


while True:
    # Get user input & strip space chars from it.
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    # if 'add' in user_action or 'new' in user_action:
    if user_action.startswith("add"):
        todo = user_action[4:]      #list slicing operation

        todos = get_todos("todos.txt")

        todos.append(todo + '\n')

        write_todos("todos.txt", todos)

    # elif "show" in user_action:
    elif user_action.startswith("show"):

        todos = get_todos("todos.txt")

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

            todos = get_todos("todos.txt")

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + '\n'

            write_todos("todos.txt", todos)
        except ValueError:
            print("Invalid command.")
            continue        #continue jumps back to the beginning.

    # elif 'complete' in user_action:
    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])

            todos = get_todos("todos.txt")

            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            write_todos("todos.txt", todos)

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
