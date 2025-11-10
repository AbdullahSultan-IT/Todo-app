import functions 

import FreeSimpleGUI as sg


label = sg.Text("type in a todo")
inputBox = sg.Input(tooltip="enter a to-do" , key="todo")
botton = sg.Button("Add")


window = sg.Window("My To-Do app" ,
                   layout=[[label],[inputBox ,botton]],
                   font=('Helvetica' ,15)
                   )


while True :

    event,value = window.read()
    print(event)
    print(value)
    
    match event:
        case 'Add':
             todos = functions.get_todos()
             newTodo = value["todo"] + '\n'
             todos.append(newTodo)
             functions.write_todos(todos)
        case sg.WIN_CLOSED:
            break
window.close()


