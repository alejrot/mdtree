import os
import pathlib
import sys


from module.styles import *

excluded = { ".git", "__pycache__", "build", "cache"}






def explore(directory:str , lineas:list=[] ,nivel:int=0, styleline="gross"):


    ruta_actual = pathlib.Path(directory)

    rutas_internas = sorted(
        ruta_actual.iterdir() ,
        key=lambda path: (path.is_file(), path.name.lower()),
    )
    rutas_internas = list( rutas_internas )

    # quita de elementos excluidos
    for ruta in rutas_internas:
        if ruta.name in excluded:
            rutas_internas.remove(ruta)
            # continue

    # busqueda del último elemento de la lista 
    nr_paths = len(rutas_internas)
    if nr_paths > 0:
        ruta_ultima = rutas_internas[nr_paths-1] 

    # diccionario auxiliar: conteo de elementos internos por directorio
    dict_paths[directory] = nr_paths


    # conteo de elementos en ruta actual
    level_elements=[]
    ruta_padre = ruta_actual
    for i in range(1, nivel+1):
        # print(i)
        ruta_padre = ruta_padre.parent
        # print(ruta_padre)
        level_elements.append(dict_paths[str(ruta_padre)])
    level_elements.reverse()

    # composicion de elementos de arbol
    prefijo=""
    for e in level_elements:
        seq = f"{bar[styleline]} " if e > 1 else "    "
        prefijo += seq

    # composicion de arbol de archivos
    for ruta in rutas_internas:

        suffix = union[styleline] if ruta != ruta_ultima else corner[styleline]
        sublineas = []

        prefix = prefijo + suffix

        if ruta.is_dir():
            icon = icons["folder"]
            linea = f"{prefix} {icon} {ruta.name}\n"
            explore(str(ruta), lineas=sublineas, nivel=nivel+1 , styleline=styleline)

        else:
            if ruta.suffix in icons.keys():
                icon = icons[ruta.suffix]
            elif ruta.suffix in images_list:
                icon = icons["image"]
            elif ruta.suffix in config_list:
                icon = icons["config"]
            elif ruta.suffix in document_list:
                icon = icons["document"]
            else:
                icon = icons["default"]

            linea = f"{prefix} {icon} {ruta.name}\n"

        
        lineas.append(linea)
        lineas.extend(sublineas)

        dict_paths[directory] = dict_paths[str(ruta_actual)] - 1
        




def draw(folder: str, 
    filename:str|None=None, 
    codeblock:bool=True,
    console:bool=False,
    styleline:str="gross",
    ) -> bool:

    print(f"line: {styleline}")

    directory = pathlib.Path(folder).absolute()

    if directory.is_dir() == False:
        print(f"ERROR: {directory.name} is not a dir or it doesn't exist.")
        print("Aborted")
        return False

    root_folder = f"📂 {directory.name}\n"

    result_lines = []

    explore(str(directory), lineas=result_lines, styleline=styleline)

    if console:
        print(root_folder.rstrip())   
        for line in result_lines:
            print(line.rstrip())


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






if __name__=="__main__":

    try:
        directory = pathlib.Path(sys.argv[1]).absolute()
        folder = str(directory)

        excluded_file = "excluded.txt"
        # excluded_file = "excluded.md"
        with open(excluded_file, "r") as file:
            excluded_list = file.readlines()

        for i in range(len(excluded_list)):
            line = excluded_list[i]
            excluded_list[i]= str(line.replace("\n","").strip())



    except IndexError:
        print("[b]Usage:[/] python tree.py <DIRECTORY>")
    else:


        mas = { 
            ".jpg": "🍆",
            ".py": "🐍"

            }

        # icons.update(mas)


        excluded = excluded.union(excluded_list)


        filename = "ImageHelpers.md"
        draw(folder, 
            filename=filename, 
            console=True,
            styleline="double"
            )