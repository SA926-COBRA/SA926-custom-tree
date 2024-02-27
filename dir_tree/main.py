import os
import argparse


def generate_tree_str(folder_path, indent='', include_hidden=False):
   tree_str = ''
   num_dirs = 0
   num_files = 0

   try:
      items = os.listdir(folder_path)
   except PermissionError:
      print(f"Permission denied: {folder_path}")
      return tree_str, num_dirs, num_files

   for i, item in enumerate(items):
      if not include_hidden and item.startswith('.'):
         continue

      if i == len(items) - 1:
         branch = '└── '
         new_indent = indent + '    '
      else:
         branch = '├── '
         new_indent = indent + '│   '
      item_path = os.path.join(folder_path, item)

      if os.path.isdir(item_path):
         item_display = f"📂 {item}"
         num_dirs += 1
      else:
         item_display = f"📄 {item}"  # File icon
         num_files += 1
      tree_str += f"{indent}{branch}{item_display}\n"

      if os.path.isdir(item_path):
         subtree, dirs, files = generate_tree_str(item_path, new_indent, include_hidden)
         tree_str += subtree
         num_dirs += dirs
         num_files += files

   return tree_str, num_dirs, num_files


def save_project_structure_to_file(file_path, include_hidden=False):
   current_directory = os.getcwd()
   tree, num_dirs, num_files = generate_tree_str(current_directory, include_hidden=include_hidden)

   with open(file_path, 'w', encoding='utf-8') as file:
      file.write(f"Project structure for directory: {current_directory}\n\n")
      file.write(tree)
      file.write(f"\n\nTotal directories 📂: {num_dirs}\n")
      file.write(f"Total files 📄: {num_files}\n")

   print(f"Project structure saved to {file_path}")

def main():
   parser = argparse.ArgumentParser(description='Display directory tree structure')
   parser.add_argument('--output', '-o', metavar='FILE', help='Output file path')
   parser.add_argument('--hidden', action='store_true', help='Include hidden directories')
   args = parser.parse_args()

   if args.output:
      save_project_structure_to_file(args.output, include_hidden=args.hidden)
   else:
      current_directory = os.getcwd()
      tree, num_dirs, num_files = generate_tree_str(current_directory, include_hidden=args.hidden)
      print(tree)
      print(f"Total directories 📂: {num_dirs}")
      print(f"Total files 📄: {num_files}")
      print(f"\nIf you liked it give us a star & follow for more :) ... https://github.com/dragon-devs/dir-tree-drh")


if __name__ == "__main__":
   main()
