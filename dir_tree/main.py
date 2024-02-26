"""
---------------------------
   Writer: dragon-devs
   Github: https://github.com/dragon-devs
---------------------------
"""
import os


def generate_tree_str(folder_path, indent=''):
   tree_str = ''
   num_dirs = 0
   num_files = 0
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
         subtree, dirs, files = generate_tree_str(item_path, new_indent)
         tree_str += subtree
         num_dirs += dirs + 1
         num_files += files
      else:
         num_files += 1
   return tree_str, num_dirs, num_files


def save_project_structure_to_file(file_path):
   current_directory = os.getcwd()
   tree, num_dirs, num_files = generate_tree_str(current_directory)
   with open(file_path, 'w', encoding='utf-8') as file:
      file.write(f"Project structure for directory: {current_directory}\n\n")
      file.write(tree)
      file.write(f"\n\nTotal directories: {num_dirs}\n")
      file.write(f"Total files: {num_files}\n")
   print(f"Project structure saved to {file_path}")


if __name__ == "__main__":
   save_project_structure_to_file("current_dir_tree.txt")
