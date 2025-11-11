import FreeSimpleGUI as sg
import zip_creator 


label1 = sg.Text("select file to compress")
input1 = sg.Input()
button1 = sg.FilesBrowse("choose",key="files")


label2 = sg.Text("select distintion folder")
input2 = sg.Input()
button2 = sg.FolderBrowse("choose",key="folder")
output_lebal = sg.Text(key="output")

compress_button = sg.Button("compress")
window = sg.Window("file compression program" , layout=[[label1,input1,button1],
                                                        [label2,input2,button2],
                                                        [compress_button , output_lebal]])

while True :
    event , values = window.read()
    print(event,values)
    filepaths = values["files"].split(';')
    directionalPath = values["folder"]
    zip_creator.make_archive(filepaths,directionalPath)
    window["output"].update(value="compression completed")
    
    
        
window.read()
window.close()