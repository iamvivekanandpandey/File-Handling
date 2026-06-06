from pathlib import Path


def readfileandfolder():
    path = Path('')
    items = list(path.iterdir())

    for i, item in enumerate(items):
        print(f"{i+1} : {item}")


def createfile():
    try:
        readfileandfolder()
        name = input("Please tell your file name: ")
        p = Path(name)

        if not p.exists():
            with open(p,"w") as fs:
                data = input("What do you want to write in this file: ")
                fs.write(data)

            print("FILE CREATED SUCCESSFULLY")
        else:
            print("This file already exists")

    except Exception as err:
        print(f"An error occured as {err}")


def updatefile():
    try:
        readfileandfolder()
        name = input("Tell me which file do you want to update: ")
        p = Path(name)

        if p.exists() and p.is_file():
            print("Press 1 for changing the name of your File: ")
            print("Press 2 for overwriting the data of your File: ")
            print("Press 3 for appending some content in your File: ")

            res = int(input("Tell me your response: "))

            if res == 1:
                name2 = input("Tell me your new file name: ")
                p2 = Path(name2)

                if not p2.exists():
                    p.rename(p2)
                    print("NAME CHANGED SUCCESSFULLY")
                else:
                    print("File with this name already exists")
            elif res == 2:
                with open(p, 'w') as fs:
                    data = input("Tell me what do you want to write - This will overwrite the data: ")
                    fs.write(data)
                print("DATA OVERWRITE SUCCESSFULLY")
            elif res == 3:
                with open(p, 'a') as fs:
                    data = input("Tell me what do you want to append: ")
                    fs.write(" "+ data)
                print("APPENDED SUCCESSFULLY")
            else:
                print("Invalid Option !")
        else:
            print("No such file exist")

    except Exception as err:
        print(f"An error occured as {err}")


def readfile():
    try:
        readfileandfolder()
        name = input("Which file do you want to read: ")
        p = Path(name)

        if p.exists() and p.is_file():
            with open(p,'r') as fs:
                data = fs.read()
                print(f"\n{data}\n" )
            print("READ SUCCESSFULLY")
        else:
            print("The File doesn't exists")

    except Exception as err:
        print(f"An error occured as {err}")


def deletefile():
    try:
        readfileandfolder()
        name = input("Which file do you want to delete: ")
        p = Path(name)

        if p.exists() and p.is_file():
            p.unlink()
            print("FILE DELETED SUCCESSFULLY")
        else:
            print("No such file exist")
    
    except Exception as err:
        print(f"An error occured as {err}")


def main():
    print("Press 1 for creating a File")
    print("Press 2 for updating a File")
    print("Press 3 for reading a File")
    print("Press 4 for deleting a File")


if __name__ == "__main__":
    while True:
        main()

        try:
            check = int(input("Please tell your response: "))
        except ValueError:
            print("Please enter a valid number !")
            continue

        if check == 1:
            createfile()

        elif check == 2:
            updatefile()

        elif check == 3:
            readfile()

        elif check == 4:
            deletefile()

        else:
            print("Invalid Choice !")

        again = input(
            "\nDo you want to continue? (y/n): "
        ).lower()

        if again != "y":
            print("GOOD BYE !")
            break
