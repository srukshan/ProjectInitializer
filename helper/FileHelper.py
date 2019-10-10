from pathlib import Path

def isFile(file):
    my_file = Path(file)
    return my_file.is_file()

def isFolder(file):
    my_folder = Path(file)
    return my_folder.is_dir()

def createFolder(file):
    my_folder = Path(file)
    return my_folder.mkdir(parents=True)