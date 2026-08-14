import functions

import FreeSimpleGUI as sg

label = sg.Text("Type in a to-do:")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_Button = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_todos(), key='list_todos',
                      enable_events=True, size=[44, 10])
edit_button = sg.Button("Edit")

window = sg.Window("P's To-Do App",
                   layout=[[label],
                           [input_box, add_Button],
                           [list_box, edit_button]],
                   font=('Helvetica', 20))
while True:
    event, values = window.read()
    print(1, event)
    print(2, values)
    print(3, values['list_todos'])

    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['list_todos'].update(values=todos)
        case "Edit":
            todo_to_edit = values['list_todos'][0]
            new_todo = values['todo']

            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            functions.write_todos(todos)
            window['list_todos'].update(values=todos)
        case "list_todos":
            window['todo'].update(value=values['list_todos'][0])
        case sg.WIN_CLOSED:
            break

window.close()

# NOTE: freesimplegui mental pattern
# 1. WIDGETS  ➜  2. LAYOUT  ➜  3. WINDOW  ➜  4. EVENT LOOP
