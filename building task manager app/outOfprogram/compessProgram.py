import FreeSimpleGUI as sg

label1 = sg.Text("select files to compress ")
input1 = sg.Input()
button1 = sg.FilesBrowse("choose file")


label2 = sg.Text("select distintion folder ")
input2 = sg.Input()
button2 = sg.FolderBrowse("choose file")

compress_button = sg.Button("compress")
window = sg.Window("file compression program" , layout=[[label1,input1,button1],
                                                        [label2,input2,button2],
                                                        [compress_button]])
window.read()
window.close()