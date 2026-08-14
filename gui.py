import functions

import FreeSimpleGUI as sg

label = sg.Text("Type in a to-do:")
input_box = sg.InputText(tooltip="Enter todo")
add_Button = sg.Button("Add")

window = sg.Window("P's To-Do App", layout=[[label], [input_box, add_Button]])
window.read()
window.close()

# NOTE: freesimplegui mental pattern
# 1. WIDGETS  ➜  2. LAYOUT  ➜  3. WINDOW  ➜  4. EVENT LOOP
