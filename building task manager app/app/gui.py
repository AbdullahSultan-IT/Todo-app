import functions 

import FreeSimpleGUI as sg


label = sg.Text("type in a todo")
inputBox = sg.InputText(tooltip="enter a to-do" , key="todo")
Add_botton = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_todos(), key='todos', enable_events=True , size=[45,10])
edit_botton = sg.Button("Edit")


window = sg.Window("My To-Do app" ,
                   layout=[[label],[inputBox ,Add_botton],
                           [list_box, edit_botton]],
                   font=('Helvetica' ,15)
                   )


while True :

    event,values = window.read()
    print(1 ,event)
    print(2 , values)
    print(3, values["todos"])
    
    match event:
        case 'Add':
             todos = functions.get_todos()
             newTodo = values["todo"] + '\n'
             todos.append(newTodo)
             functions.write_todos(todos)
             window['todos'].update(values=todos)

        case "Edit":
            todo_to_edit = values['todos'][0]
            todo_to_replace = values["todo"]
            
            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = todo_to_replace
            functions.write_todos(todos)
            window['todos'].update(values=todos)
            
        case "todos":
            window['todo'].update(value=values['todos'][0])
            
        case sg.WIN_CLOSED:
            break        
        
window.close()

