# Project Directory Tree

## Overview

This project directory is organized using a hierarchical structure to efficiently manage and navigate through various
files and directories. Below is a breakdown of the directory tree along with explanations for each directory and file.

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

**Installation Path:** Ensure that the installation path for Python packages is included in your system's PATH
environment variable. This path typically includes the Scripts directory inside the Python installation directory.

**Shell Restart:** If you're using a shell (like Bash), you might need to restart it to pick up the changes to the PATH
environment variable.

**Installation Location:** Double-check the installation location of the package. If it's not installed in the expected
location, you might need to investigate why the installation path is different.

**Executable Name:** Ensure that the name specified in the `console_scripts` entry point in your `setup.py` matches the
command you're trying to run. In this case, it should be `dir-tree`.

**Permissions:** Make sure that you have the necessary permissions to execute commands from the installed package.

**Virtual Environment:** If you're using a virtual environment, ensure that it is activated when you try to run the
command.

## Directory Tree
```
project_directory/
│
├── src/
│   ├── main/
│   │   ├── java/
│   │   │   ├── com/
│   │   │   │   └── example/
│   │   │   │       └── Main.java
│   │   │   │
│   │   │   ├── resources/
│   │   │   │   └── config/
│   │   │   │       └── application.properties
│   │   │   │
│   │   │   └── webapp/
│   │   │       └── index.html
│   │   │
│   │   └── test/
│   │       ├── java/
│   │       │   └── com/
│   │       │       └── example/
│   │       │           └── MainTest.java
│   │       │
│   │       └── resources/
│   │           └── test_config/
│   │               └── test.properties
│   │
│   └── docs/
│       └── documentation.md
│
├── README.md
│
└── LICENSE
```

## New Feature: Include Hidden Directories

The `dir-tree` tool now supports including hidden directories in the directory tree structure. Hidden directories are
those whose names begin with a dot (`.`), such as `.git` or `.config`. By default, hidden directories are excluded from
the tree structure.

### Usage

To include hidden directories in the tree structure, use the `--hidden` flag when running the `dir-tree` command:

```bash
dir-tree --hidden
```

**Example:**
Consider the following directory structure:

```
my_project/
├── .git/
│   ├── config
│   └── ...
├── src/
│   ├── main.py
│   └── ...
├── tests/
│   ├── test.py
│   └── ...
└── README.md
```

Without the --hidden flag, running dir-tree would output:

```
my_project/
├── src/
│   ├── main.py
│   └── ...
├── tests/
│   ├── test.py
│   └── ...
└── README.md
```

With the `--hidden` flag, hidden directories are included:

```
my_project/
├── .git/
│   ├── config
│   └── ...
├── src/
│   ├── main.py
│   └── ...
├── tests/
│   ├── test.py
│   └── ...
└── README.md
```

**Note:**
Including hidden directories can be useful for inspecting the entire directory structure, including version control
files (e.g., .git) or configuration directories (e.g., .config). However, be cautious when sharing or distributing
directory tree structures that include hidden directories, as they may contain sensitive information.


