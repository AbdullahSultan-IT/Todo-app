import functions 
import time 
now = time.strftime("%b %d , %Y %H:%M:%S")
print("it is " , now)
while True:

    usrinput = input("please enter your add or quit or show or edit or complete : ")

    usrinput = usrinput.strip()

   

    if usrinput.startswith("add") :
          
        todo = usrinput[4:] + "\n"
                        
        todos = functions.get_todos()
        
        todos.append(todo)
        
        functions.write_todos(todos)

    elif usrinput.startswith("show"):
          
        todos = functions.get_todos()

        for index , item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index +1} - {item}"
            print(row)

    elif usrinput.startswith("edit") :
        try :
            numofname = int(usrinput[5:])
            
            todos = functions.get_todos()

            NewTodo = input("enter new todo :")

            todos [numofname - 1] = NewTodo + '\n'
            
            functions.write_todos(filepath="files/todos.txt",todos=todos)

        except ValueError :
            print("ERROR !!  enter a number of the todo after the word edit")
            continue

    elif usrinput.startswith("complete"):
        try :
            numofname = int(usrinput[9:])
            
            todos = functions.get_todos()
            
            index = numofname - 1
            
            removed = todos[index].strip("\n")
        except IndexError :
            print("the number is out of range")
            continue
        
            
        todos.pop(numofname - 1)
        
        functions.write_todos(todos)

        message = f" {removed} was assign as completed and removed "
        print(message)

                    
    elif usrinput.startswith("quit") :
        break
    else :
        print("invalid input\n")
        
print(" \n   bey  <3  \n")




