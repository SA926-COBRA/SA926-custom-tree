"""
---------------------------
   Writer: dragon-devs
   Github: https://github.com/dragon-devs
---------------------------
"""
import os


def generate_tree_str(folder_path, indent=''):
   tree_str = ''
   items = os.listdir(folder_path)
   for i, item in enumerate(items):
      if i == len(items) - 1:
         branch = '└── '
         new_indent = indent + '    '
      else:
         branch = '├── '
         new_indent = indent + '│   '
      item_path = os.path.join(folder_path, item)
      tree_str += f"{indent}{branch}{item}\n"
      if os.path.isdir(item_path):
         tree_str += generate_tree_str(item_path, new_indent)
   return tree_str


def show_project_structure():
   current_directory = os.getcwd()
   print(f"Project structure for directory: {current_directory}\n")
   print(generate_tree_str(current_directory))


if __name__ == "__main__":
   show_project_structure()