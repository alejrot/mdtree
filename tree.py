import pathlib
import sys


from module.tree import tree



if __name__=="__main__":

    try:
        directory = pathlib.Path(sys.argv[1]).absolute()
        folder = str(directory)

        if len(sys.argv) > 2:
            exclusion_file = pathlib.Path(sys.argv[2]).absolute()
            if exclusion_file.is_file()==False:
                print(f"Exclusion file '{exclusion_file}' not found.")
                exclusion_file = ".treeignore"
                print(f"Exclusion file '{exclusion_file}' used instead.")

        else:
            exclusion_file = ".treeignore"



    except IndexError:
        print("Usage: python tree.py <DIRECTORY>")
        print("or:")
        print("Usage: python tree.py <DIRECTORY>  <EXCLUSION_FILE>")

    except FileNotFoundError:
        print(f"Exclusion file '{exclusion_file}' not found ")
        exclusion_file = ".treeignore"

    else:

        special_icons = { 
            ".py": "🐍",
            }

        tree(folder, 
            # console=True,
            # archive=False,
            # styleline="double"
            styleline="thin",
            # ignore=list(excluded ),
            # ignore=excluded ,
            exclusion_files=[exclusion_file],
            custom_icons = special_icons,
            )