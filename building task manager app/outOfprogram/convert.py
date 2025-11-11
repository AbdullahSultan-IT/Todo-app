import FreeSimpleGUI as sg

text1 = sg.Text("enter feet:") 
lebal1 = sg.InputText(key="feet")


text2 = sg.Text("enter inches:") 
lebal2 = sg.InputText(key="inches")

convert_button = sg.Button("convert")
exit_button = sg.Button("exit")

layout = [[text1 , lebal1],
          [text2 , lebal2],
          [convert_button , exit_button]
          ]

window = sg.Window("conveting program" , layout=layout ,font=('Helvetica', 20))

while True :
    event , values = window.read()
    match event:
        case ""