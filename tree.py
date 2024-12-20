import pathlib
# import sys
import argparse


from mdtree.tree import tree, exclusion_list


# initialization and help
parser = argparse.ArgumentParser(
    description='''
        Explores and draw the tree of files
        in file or console.
    ''',
    # arguments file support
    fromfile_prefix_chars='@'
    )

# input arguments definition
parser.add_argument('-f', '--folder', type=str, 
    required=False,
    default='.',
    help="Folder's path to be explored."
    )
parser.add_argument('-s', '--styleline', type=str,
    choices=['gross', 'thin', 'double'],
    default='gross', 
    required=False,
    help="Connector's line style"
    )
parser.add_argument('-n', '--name', type=str,
    default=None, 
    required=False,
    help="Custom name for output file."
    )
parser.add_argument('-c','--console', type=str,
    nargs='?',
    default='false',
    required=False,
    help="Shows file tree in console."
    )
parser.add_argument('-b','--block', type=str,
    nargs='?',
    default='false',
    required=False,
    help="Saves filetree as markdown codeblock in file."
    )
parser.add_argument('-e','--exclusion-file', type=str,
    default='.treeignore',
    required=False,
    help="File with excluded files and folders from search."
    )


# arguments reading
args = parser.parse_args()

# absolute path of input folder
directory = pathlib.Path(args.folder).absolute()
folder = str(directory)

# show tree in shell
console = False
if args.console == None:
    console = True

# setting exclusion list from file
if args.exclusion_file == "none":
    excluded = set()
else: 
    excluded = exclusion_list([args.exclusion_file ])

# saves output as markdown codeblock in file
block = False
if args.block == None:
    block = True




special_icons = { 
    # ".py": "🐍",
    }


tree(folder_path=folder, 
    filename=args.name,
    codeblock=block ,
    console=console,
    archive= not console,
    styleline=args.styleline,
    ignore_list=excluded,
    # custom_icons=special_icons,
    )

