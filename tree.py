import pathlib
# import sys
import argparse


from mdtree.tree import tree, exclusion_list





# initialization and help
parser = argparse.ArgumentParser(
    description='''
        Explores and draw the tree of files
        in file or console.
    ''')
# input arguments definition
parser.add_argument('-f', '--folder', type=str, 
    required=False,
    default='.',
    help="Folder's path to be explored"
    )
parser.add_argument('-s', '--styleline', type=str,
    choices=['gross', 'thin', 'double'],
    default='gross', 
    required=False,
    help="Connector's line style"
    )

parser.add_argument('-c','--console', type=bool,
    choices=['true', 'false'],
    default=False,
    required=False,
    help="Shows file tree in console."
    )




args = parser.parse_args()


directory = pathlib.Path(args.folder).absolute()
folder = str(directory)


special_icons = { 
    # ".py": "🐍",
    }

tree(folder_path=folder, 
    console=args.console,
    # filename=  ,
    # codeblock= ,
    # archive=False,
    styleline=args.styleline,
    # ignore_list=excluded,
    custom_icons=special_icons,
    )

    # try:
    #     directory = pathlib.Path(sys.argv[1]).absolute()
    #     folder = str(directory)

    #     if len(sys.argv) > 2:
    #         exclusion_file = pathlib.Path(sys.argv[2]).absolute()
    #         if sys.argv[2].lower() == "none":
    #             exclusion_file = "none"

    #         elif exclusion_file.is_file()==False:
    #             print(f"Exclusion file '{exclusion_file}' not found.")
    #             exclusion_file = ".treeignore"
    #             print(f"Exclusion file '{exclusion_file}' used instead.")

    #     else:
    #         exclusion_file = ".treeignore"



    # except IndexError:
    #     print("Usage: python tree.py <DIRECTORY>")
    #     print("or:")
    #     print("Usage: python tree.py <DIRECTORY>  <EXCLUSION_FILE>")

    # except FileNotFoundError:
    #     print(f"Exclusion file '{exclusion_file}' not found ")
    #     exclusion_file = ".treeignore"

    # else:

    #     if exclusion_file == "none":
    #         excluded = set()
    #     else: 
    #         excluded = exclusion_list([exclusion_file])


# special_icons = { 
#     # ".py": "🐍",
#     }

# tree(folder, 
#     # console=True,
#     # archive=False,
#     # styleline="double",
#     # styleline="thin",
#     styleline="gross",
#     ignore_list=excluded,
#     custom_icons=special_icons,
#     )