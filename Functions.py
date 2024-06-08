def get_todos(File):
    with open(File,"r") as archive:
        returni=archive.readlines()

    return returni

def write_todos(new_items,Filee):
    with open(Filee,"w") as file:
        file.writelines(new_items)