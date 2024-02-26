import os


def generate_tree_str(folder_path, indent='', include_hidden=False):
   tree_str = ''
   num_dirs = 0
   num_files = 0
   items = os.listdir(folder_path)

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
         item_display = f"{item} <dir>"
         num_dirs += 1
      else:
         item_display = item
         num_files += 1
      tree_str += f"{indent}{branch}{item_display}\n"

      if os.path.isdir(item_path):
         subtree, dirs, files = generate_tree_str(item_path, new_indent, include_hidden)
         tree_str += subtree
         num_dirs += dirs
         num_files += files

   return tree_str, num_dirs, num_files
