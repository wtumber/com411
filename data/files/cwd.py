import os
def cwd():
    path = os.getcwd() 
    print("The current working folder is {}".format(path))
    print("the folder contains the following:")
    for file in os.listdir(path):
        print(file)

    
def run():
    print("Processing...")
    cwd()

run()