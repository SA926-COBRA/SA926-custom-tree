"""
---------------------------
   Writer: dragon-devs
   Github: https://github.com/dragon-devs
---------------------------
"""
import os
import argparse

import generate_tree
import save_tree_to_file


def main():
   parser = argparse.ArgumentParser(description='Display directory tree structure')
   parser.add_argument('--output', '-o', metavar='FILE', help='Output file path')
   parser.add_argument('--hidden', action='store_true', help='Include hidden directories')
   args = parser.parse_args()

   if args.output:
      save_tree_to_file.save_project_structure_to_file(args.output, include_hidden=args.hidden)
   else:
      current_directory = os.getcwd()
      tree, num_dirs, num_files = generate_tree.generate_tree_str(current_directory, include_hidden=args.hidden)
      print(tree)
      print(f"Total directories: {num_dirs}")
      print(f"Total files: {num_files}")
      print(f"\nIf you liked it give us a star & follow for more :) ... https://github.com/dragon-devs/dir-tree-drh")


if __name__ == "__main__":
   main()
