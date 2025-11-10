FILEPATH="/Users/abdullah37/STUDY/IT 315/PracticingForPython/day1/building task manager app/app/todos.txt"


def get_todos(filepath=FILEPATH):
    with  open(filepath , "r") as file :
        todos = file.readlines()
    return todos

def write_todos( todos,  filepath=FILEPATH):
    with  open(filepath , "w") as file :
            file.writelines(todos)
            
if __name__ == "__main__" :     
    print("hello im in  func")
    print(get_todos())