from parser import create_dir, generate_markdown, create_dir_from_tree, generate_html
import json
import os 

#current directory
root_dir =  os.path.join(os.getcwd(), "..") 
asset_path = os.path.join(root_dir, "assets") 


with open('../templates/sample1.json') as json_file:
    directory_tree = json.load(json_file)

#generate directory
create_dir_from_tree(directory_tree,asset_path, with_seeds = True, with_convention = True)

#generate index.html
generate_html(directory_tree, asset_path,  with_convention = True)