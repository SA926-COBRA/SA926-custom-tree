import os

import generate_tree


def save_project_structure_to_file(file_path, include_hidden=False):
   current_directory = os.getcwd()
   tree, num_dirs, num_files = generate_tree.generate_tree_str(current_directory, include_hidden=include_hidden)

   with open(file_path, 'w', encoding='utf-8') as file:
      file.write(f"Project structure for directory: {current_directory}\n\n")
      file.write(tree)
      file.write(f"\n\nTotal directories: {num_dirs}\n")
      file.write(f"Total files: {num_files}\n")

   print(f"Project structure saved to {file_path}")
