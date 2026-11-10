from pathlib import Path
def fileinfolder():
    path=Path('')
    items=list(path.rglob('*'))
    for i, item in enumerate(items):
        print(f"{i+1} : {item}")

def creat_file():
    fileinfolder()
    try :
        filename=input("Enter the name of the file to create : ")
        p=Path(filename)
        with open(p,'w') as f:
            input_data=input("Enter the data to write in the file : ")
            f.write(input_data)
            print(f"File '{filename}' created successfully.")
    except Exception as e:
        print(f"An error occurred while creating the file: {e}")


def read_file():
    fileinfolder()
    try :
        filename=input("Enter the name of the file to read : ")
        p=Path(filename)
        if p.exists():
            with open(p,'r') as f:
                data=f.read()
                print(f"Contents of '{filename}':\n{data}")
        else:
            print(f"File '{filename}' does not exist.")
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")

def update_file():
    fileinfolder()
    try : 
        filename=input("Enter the name of the file to update : ")
        p=Path(filename)
        if p.exists() and p.is_file():
            print("Enter 1 for changing name of the file")
            print("Enter 2 for overwriting data in the file")
            print("Enter 3 for appending data to the file")
            choice = int(input("Enter your choice : "))


            if choice==1:

                new_filename=input("Enter the new name for the file : ")
                new_p=Path(new_filename)
                if p.exists():
                    p.rename(new_p)
                    print(f"File '{filename}' renamed to '{new_filename}' successfully.")
                else:
                    print(f"File '{filename}' does not exist.")
            elif choice==2:
                
                if p.exists():
                    with open(p,'w') as f:
                        input_data=input("Enter the new data to overwrite the file : ")
                        f.write(input_data)
                    print(f"File '{filename}' overwritten successfully.")
                else:
                    print(f"File '{filename}' does not exist.")
            elif choice==3:
                    if p.exists() and p.is_file():
                        with open(p,'a') as f:
                            input_data=input("Enter the data to append to the file : ")
                            f.write('\n' + input_data)
                        print(f"File '{filename}' updated successfully.")
                    else:
                        print(f"File '{filename}' does not exist.")
            else :
                print("Invalid choice. Please select a valid option.")
        else:
            print(f"File '{filename}' does not exist.")
    except Exception as e:
        print(f"An error occurred while updating the file: {e}")

def delete_file():
    fileinfolder()
    try:
        filename=input("Enter the name of the file to delete : ")
        p=Path(filename)
        if p.exists() and p.is_file():
            p.unlink()
            print(f"File '{filename}' deleted successfully.")
        else:
            print(f"File '{filename}' does not exist.")
    except Exception as e:
        print(f"An error occurred while deleting the file: {e}")


print("press 1 for creating a new file")
print("press 2 for reading an existing file")
print("press 3 for updating an existing file")
print("press 4 for deleting an existing file")
def input_1():
    check = int(input("Enter your choice : "))
    if check==1:
        creat_file()
    elif check==2:
        read_file()
    elif check==3:
        update_file()
    elif check==4:
        delete_file()
    else:
        print("Invalid choice. Please select a valid option.")


input_1()
