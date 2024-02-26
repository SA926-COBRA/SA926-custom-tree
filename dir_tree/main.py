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


def save_project_structure_to_file(file_path):
   current_directory = os.getcwd()
   tree = generate_tree_str(current_directory)
   with open(file_path, 'w', encoding='utf-8') as file:
      file.write(tree)
   print(f"Project structure saved to {file_path}")


if __name__ == "__main__":
   save_project_structure_to_file("project_directory_tree.txt")
