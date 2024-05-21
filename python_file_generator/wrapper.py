from parser import create_dir, generate_markdown, create_dir_from_tree, generate_html
import yaml
from pathlib import Path
import os 
import json
#current directory
root_dir =  os.path.join(os.getcwd(), "./") 
asset_path = os.path.join(root_dir, "assets") 
file_path = os.path.join(root_dir, "templates/from_pyvert.yml") 

#read yml
directory_tree = yaml.safe_load(Path(file_path).read_text())
#f = open(json_path)
#directory_tree = json.load(f)
#generate directory
create_dir_from_tree(directory_tree,asset_path, with_seeds = True, with_convention = True)

#generate index.html
generate_html(directory_tree, asset_path,  with_convention = False)