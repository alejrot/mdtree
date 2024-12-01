import pathlib
import sys

from module.styles import *
from module.connectors import *
from module.excluded import excluded 

# auxiliary dictionary that counts inner elements in every folder
# it helps to shape graphic tree
folder_elements = dict()


def explore_tree(directory:str, 
    ignore:set,
    tree_lines:list=[], 
    sublevel:int=0, 
    styleline="gross",
    ):

    actual_path = pathlib.Path(directory)

    # search and filtering of inner elements of folder
    content_list = actual_path.iterdir()
    content_obj = filter( lambda x: x.name not in ignore  , content_list)
    content_list = list(content_obj)

    # sorting content by type and name
    inner_paths = sorted(
        content_list,
        key=lambda path: (path.is_file(), path.name.lower()),
    )
    inner_paths = list( inner_paths )

    # search of last element in list
    nr_paths = len(inner_paths)
    if nr_paths > 0:
        last_path = inner_paths[nr_paths-1] 

    # auxiliary dictionary that counts inner elements in every folder
    folder_elements[directory] = nr_paths


    # element count in actual folder
    level_elements=[]
    parent_path = actual_path
    for i in range(1, sublevel+1):
        parent_path = parent_path.parent
        level_elements.append(folder_elements[str(parent_path)])
    level_elements.reverse()

    # tree element's composition
    tree_sequence =""
    for e in level_elements:
        seq = f"{bar[styleline]} " if e > 1 else "    "
        tree_sequence  += seq


    # tree composition - branch by branch
    for path in inner_paths:

        # list used to keep inner elements of subfolders
        tree_branches = []

        # choosing between union ("┣━━") or corner ("┗━━")
        tree_suffix = union[styleline] if path != last_path else corner[styleline]
        prefix = tree_sequence + tree_suffix

        if path.is_dir():
            # adding folder's icon and connector
            icon = icons["folder"]
            string_line = f"{prefix} {icon} {path.name}\n"


            # recursive call for drawing inner tree branches
            if  path.name != ".git":
                explore_tree(directory=str(path), 
                    ignore=ignore, 
                    tree_lines=tree_branches, 
                    sublevel=sublevel+1 , 
                    styleline=styleline,
                    )

        else:
            # choosing emoji by file extension
            if path.suffix in icons.keys():
                icon = icons[path.suffix]
            elif path.suffix in images_list:
                icon = icons["image"]
            elif path.suffix in config_list:
                icon = icons["config"]
            elif path.suffix in document_list:
                icon = icons["document"]
            else:
                icon = icons["default"]
            # adding file's icon and connector
            string_line = f"{prefix} {icon} {path.name}\n"

        # adding inner elements
        tree_lines.append(string_line)
        tree_lines.extend(tree_branches)

        # every time
        folder_elements[directory] = folder_elements[str(actual_path)] - 1
        

def tree(
    folder_path: str, 
    filename:str|None=None, 
    codeblock:bool=True,
    console:bool=False,
    archive:bool=True,
    styleline:str="gross",
    # ignore:set=excluded, 
    exclusion_files:list=[] , 
    custom_icons:dict=dict(),
    ) -> bool:

    directory = pathlib.Path(folder_path).absolute()

    # it verifies that path in is really a folder
    if directory.is_dir() == False:
        print(f"ERROR: {directory.name} is not a dir or it doesn't exist.")
        print("Aborted")
        return False

    # custom emojis added
    icons.update(custom_icons)

    # 'excluded' updated
    excluded = add_exclusion_list(files=exclusion_files)


    # 
    result_lines = []
    explore_tree(str(directory), 
        tree_lines=result_lines, 
        styleline=styleline,
        ignore=excluded,
        )

    root_folder = f"📂 {directory.name}\n"

    # shell output
    if console:
        print(root_folder.rstrip())   
        for line in result_lines:
            print(line.rstrip())

    # file output
    if archive:

        # directory name as filename - by default
        if filename == None:
            filename = f"{directory.name}.md"

        # saving tree in file
        with open(filename, "w+") as file:
            if codeblock:
                file.write("```\n")
            file.write(root_folder)
            for line in result_lines:
                file.write(line)
            if codeblock:
                file.write("```\n")

    return True




def add_exclusion_list(files: list[str], overwrite:bool=False):

    excluded_list = []
    for f in files:
        with open(f, "r") as file:
            # excluded_list = file.readlines()
            excluded_list.extend( file.readlines() )

    for i in range(len(excluded_list)):
        line = excluded_list[i]
        excluded_list[i]= str(line.replace("\n","").strip())


    if overwrite:
        return set(excluded_list)

    else:
        global excluded
        excluded = excluded.union(set(excluded_list))
        return excluded


