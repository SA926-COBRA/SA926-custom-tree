# Project Directory Tree


## Overview

This project directory is organized using a hierarchical structure to efficiently manage and navigate through various files and directories. Below is a breakdown of the directory tree along with explanations for each directory and file.

## Installation
```
pip install dir-tree-drh
```
then run: 
```
dir-tree
``` 
you will see your current directory tree in the console.

**Saving Directory Tree:**  If you want to save the results of your current directory tree Run this 
```
dir-tree --output file_name.txt
```
it will generate the results in the current directory `file_name.txt`.

**Installation Path:** Ensure that the installation path for Python packages is included in your system's PATH environment variable. This path typically includes the Scripts directory inside the Python installation directory.

**Shell Restart:** If you're using a shell (like Bash), you might need to restart it to pick up the changes to the PATH environment variable.

**Installation Location:** Double-check the installation location of the package. If it's not installed in the expected location, you might need to investigate why the installation path is different.

**Executable Name:** Ensure that the name specified in the `console_scripts` entry point in your `setup.py` matches the command you're trying to run. In this case, it should be `dir-tree`.

**Permissions:** Make sure that you have the necessary permissions to execute commands from the installed package.

**Virtual Environment:** If you're using a virtual environment, ensure that it is activated when you try to run the command.


## Description

- **src/**: This directory contains all the source code for the project.
  - **main/**: The main source directory where production code resides.
    - **java/**: Java source files organized according to the package structure.
      - **com/example/**: Example package structure.
        - **Main.java**: Example main class file.
    - **resources/**: Resource files like configuration files.
      - **config/**: Configuration files for the application.
        - **application.properties**: Example application configuration file.
    - **webapp/**: Web application files.
      - **index.html**: Example HTML file for the web application.
  - **test/**: The directory for test code.
    - **java/**: Test source files organized according to the package structure.
      - **com/example/**: Example package structure.
        - **MainTest.java**: Example test class file.
    - **resources/**: Resource files for tests.
      - **test_config/**: Configuration files for tests.
        - **test.properties**: Example test configuration file.
- **docs/**: Documentation directory containing project documentation.
  - **documentation.md**: Main documentation file.
- **README.md**: The file you're currently reading, providing an overview of the project structure.
- **LICENSE**: License file for the project, outlining usage and distribution rights.


