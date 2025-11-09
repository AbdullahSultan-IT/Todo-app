import functions 

import FreeSimpleGUI as sg


label = sg.Text("type in a todo")
inputBox = sg.Input(tooltip="enter a to-do")
botton = sg.Button("Insert")


window = sg.Window("My To-Do app" , layout=[[label],[inputBox ,botton]])
window.read()
window.close()


