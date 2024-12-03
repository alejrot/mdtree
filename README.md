# MDTree


This program creates a text file with the contents of the desired folder drawed as a tree scheme.
The output file has as name the folder name as default and Markdown extension.

This routines are made with Python 3.

## Shell 




### Basic use

This program needs the path of folder to explore as argument.

```bash
py tree.py  <folder_path> 
```

In example, if the program is used to describe its own file structure:


```bash
py tree.py  .
```

then the program will create a file `mdtree.md` with this content:

```
📂 mdtree
┣━━ 📂 module
┃   ┣━━ 📄 connectors.py
┃   ┣━━ 📄 styles.py
┃   ┗━━ 📄 tree.py
┣━━ 📄 excluded.txt
┣━━ 📄 LICENSE
┣━━ 📄 mdtree.md
┣━━ 📄 README.md
┣━━ 📄 setup.py
┗━━ 📄 tree.py
```

By default this program excludes a list of elements detailed in a hidden text file called `treeignore`.



### Exclusion file
<!-- 
By default this program uses by default a hidden exclusion file called `treeignore` that lists a very few folders and archives to ignore.
 -->

The `treeignore` file can be ignored by specifying another file with excluded elements as second argument:

```bash
py tree.py  <folder_path>  <exclusion_file>
```

In example, with an archive called `excluded.txt` whit the content:
```
.treeignore 

.gitignore
.git 

__pycache__

excluded.txt
mdtree.md
```

when its used as exclusion file:

```bash
py tree.py  .  excluded.txt 
```
then the file tree wil be reduced to:

```
📂 mdtree
┣━━ 📂 module
┃   ┣━━ 📄 connectors.py
┃   ┣━━ 📄 styles.py
┃   ┗━━ 📄 tree.py
┣━━ 📄 LICENSE
┣━━ 📄 README.md
┗━━ 📄 tree.py
```

### No exclusions


If `none` is used as second argument:

```bash
 py tree.py . none 
```

then the program will try to show all the contents, 
except the `git` folder content:

```
📂 mdtree
┣━━ 📂 .git
┣━━ 📂 module
┃   ┣━━ 📂 __pycache__
┃   ┃   ┣━━ 📄 connectors.cpython-313.pyc
┃   ┃   ┣━━ 📄 styles.cpython-313.pyc
┃   ┃   ┗━━ 📄 tree.cpython-313.pyc
┃   ┣━━ 📄 connectors.py
┃   ┣━━ 📄 styles.py
┃   ┗━━ 📄 tree.py
┣━━ 📄 .gitignore
┣━━ 📄 .treeignore
┣━━ 📄 LICENSE
┣━━ 📄 README.md
┗━━ 📄 tree.py
```
