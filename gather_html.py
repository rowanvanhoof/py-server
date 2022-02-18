from email.policy import default
import os

def file_lines_toList(filepath):
    
    f = open(filepath, "r")
    result = []
    result = f.readlines()

    print("Folder")

    return result

def init_server_pages(path_to_pages):
    files = os.listdir(path_to_pages)
    pages_dict = {}
    for i in range(len(files)):
        name = files[i]
        path = os.path.join(path_to_pages, name)
        
        pages_dict[files[i]] = file_lines_toList(path)
    
    # files_as_lists = (
    #     list(file_lines_toList(file)) for file in files
    # )

    return pages_dict


