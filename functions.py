FILEPATH = "todos.txt"

def get_todos(filepath=FILEPATH):
    """Read a text file and return the list of to-do items."""
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


# def write_todos(filepath="todos.txt", todos_arg): ---> wrong!
# non-default parameters should come before default parameters!
def write_todos(todos_arg, filepath=FILEPATH):
    """Write a list of to-do items in a text file."""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


if __name__ == "__main__":
    print("Hello")
    print(get_todos())

# these two lines are only executed when this function.py file is executed directly.
# And these lines are not executed when you execute the other script which imports the functions.py file.
# so this is to control the execution of this script.